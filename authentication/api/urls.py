from django.contrib import admin
from django.urls import path, include
from authentication.api.views import KakaoLoginAPIView, KakaoCallbackAPIView


urlpatterns = [
    path('kakao/login/', KakaoLoginAPIView.as_view()),
    path('kakao/callback', KakaoCallbackAPIView.as_view()),
]
