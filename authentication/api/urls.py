from django.contrib import admin
from django.urls import path, include
from authentication.api.views import KakaoLoginAPIView, KakaoCallbackAPIView, KakaoToDjangoLoginView


urlpatterns = [
    path('kakao/login/', KakaoLoginAPIView.as_view()),
    path('kakao/callback', KakaoCallbackAPIView.as_view()),
    path('kakao/login/finish', KakaoToDjangoLoginView.as_view()),
]
