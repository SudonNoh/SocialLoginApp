from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
import urllib
import requests
from authentication.models import User
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

MAIN_DOMAIN = settings.MAIN_DOMAIN


class KakaoLoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        kakao_rest_api_key = settings.KAKAO_REST_API_KEY
        redirect_uri = MAIN_DOMAIN + "/user/kakao/callback"

        return redirect(
            f'https://kauth.kakao.com/oauth/authorize?client_id={kakao_rest_api_key}&redirect_uri={redirect_uri}&response_type=code'
        )

# 초기 단계에서의 callback 함수
# class KakaoCallbackAPIView(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, *args, **kwargs):
#         params = urllib.parse.urlencode(request.GET)
#         return redirect(f'http://127.0.0.1:8000/account/registration/')


class KakaoException(Exception):
    pass


class KakaoCallbackAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            kakao_rest_api_key = settings.KAKAO_REST_API_KEY
            redirect_uri = settings.MAIN_DOMAIN + "/user/kakao/callback"
            user_token = request.GET.get("code")
            grant_type = 'authorization_code'

            parameter = f"grant_type={grant_type}&client_id={kakao_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"

            # post request
            token_request = requests.get(
                f"https://kauth.kakao.com/oauth/token?{parameter}"
            )
            token_response_json = token_request.json()
            error = token_response_json.get("error", None)

            # if there is an error from token_request
            if error is not None:
                raise KakaoException()
            access_token = token_response_json.get("access_token")

            # post request
            profile_request = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={"Authorization": f"Bearer {access_token}"},
            )
            profile_json = profile_request.json()

            # parsing profile json
            kakao_account = profile_json.get("kakao_account")
            
            email = kakao_account["email"]
            if email is None:
                raise KakaoException()

            profile = kakao_account["profile"]
            nickname = profile["nickname"]

            try:
                user_in_db = User.objects.get(email=email)
                if user_in_db is not None:
                    raise KakaoException()
                else:
                    # DB에 없는 상태인데 직접 user/registration 으로 로그인 한 경우를
                    # 처리하는 로직을 만들어야 할듯 함.
                    # 현재 로직으로는 진입하지 않음
                    data = {'code': user_token, 'access_token': access_token}
                    accept = requests.post(
                        f"{MAIN_DOMAIN}/user/kakao/login/finish/", data=data
                    )
                    accept_json = accept.json()
                    accept_jwt = accept_json.get("token")

                    # profile info update
                    User.objects.get(email=email).update(
                        username=nickname,
                        email=email,
                    )

            except User.DoesNotExist:
                data = {'code': user_token, 'access_token': access_token}
                accept = requests.post(
                    f"{MAIN_DOMAIN}/user/kakao/login/finish", data=data
                )
                accept_json = accept.json()
                accept_jwt = accept_json.get("token")

                User.objects.get(email=email).update(
                    username=nickname,
                    email=email,
                )
                return redirect(MAIN_DOMAIN+"/user/registration/")

        except KakaoException:
            return redirect(MAIN_DOMAIN+"/admin/")

class KakaoToDjangoLoginView(SocialLoginView):
    adapter_class = kakao_views.KakaoOAuth2Adapter
    client_clss = OAuth2Client