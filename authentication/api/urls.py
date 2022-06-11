from django.contrib import admin
from django.urls import path, include
# from authentication.api.views import NaverLogin, naver_login, naver_callback
from authentication.api.views import naver_login

urlpatterns = [
    path('naver/login/', naver_login, name='naver_login'),
    # path('naver/callback/', naver_callback, name='naver_callback'),
    # path('naver/login/django/', NaverLogin.as_view(), name='naver_login_todjango'),
]