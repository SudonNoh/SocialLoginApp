from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
import urllib

class KakaoLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, *args, **kwargs):
        kakao_rest_api_key = settings.KAKAO_REST_API_KEY
        redirect_uri = "http://127.0.0.1:8000/user/kakao/callback"
        
        return redirect(
            f'https://kauth.kakao.com/oauth/authorize?client_id={kakao_rest_api_key}&redirect_uri={redirect_uri}&response_type=code'
        )
        
class KakaoCallbackAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request, *args, **kwargs):
        params = urllib.parse.urlencode(request.GET)
        return redirect(f'http://127.0.0.1:8000/user/kakao/callback?{params}')