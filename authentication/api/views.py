from django.http import JsonResponse
from django.shortcuts import redirect, render
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from requests import JSONDecodeError
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

state = "state="+getattr(settings, 'STATE')

BASE_URL = 'http://127.0.0.1:8000/'
NAVER_CALLBACK_URI = BASE_URL + 'accounts/naver/login/callback'


def naver_login(request):
    client_id = getattr(settings, "NAVER_CLIENT_KEY")
    print(1)
    return redirect(
        f"https://nid.naver.com/oauth2.0/authorize/?client_id={client_id}&response_type=code&redirect_uri={NAVER_CALLBACK_URI}&{state}"
    )


# def naver_callback(request):
#     client_id = "client_id="+getattr(settings, "NAVER_CLIENT_KEY")
#     client_secret = "client_secret="+getattr(settings, "NAVER_SECRET_KEY")
#     code = "code="+request.GET.get('code')
#     grant_type = "grant_type=authorization_code"

#     token_req = request.post(
#         f"https://nid.naver.com/oauth2.0/token?{client_id}&{client_secret}&{code}&{grant_type}&{state}"
#     )
#     token_req_json = token_req.json()
#     error = token_req_json.get('error')
#     if error is not None:
#         raise JSONDecodeError(error)
#     access_token = token_req_json.get("access_token")
#     print(access_token)
#     return JsonResponse(access_token)


# class NaverLogin(SocialLoginView):
#     adapter_class = NaverOAuth2Adapter
#     client_class = OAuth2Client
#     callback_url = NAVER_CALLBACK_URI
