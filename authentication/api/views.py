from django.shortcuts import render
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# Create your views here.
class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter