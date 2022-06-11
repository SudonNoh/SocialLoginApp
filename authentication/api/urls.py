from django.contrib import admin
from django.urls import path, include
from authentication.api.views import NaverLogin

urlpatterns = [
    path('naver/', NaverLogin.as_view(), name='naver_login')
]