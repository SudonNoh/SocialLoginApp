"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import keys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY, MAIN_DOMAIN, NAVER_CLIENT_KEY, NAVER_SECRET_KEY, KAKAO_REST_API_KEY, KAKAO_SECRET_KEY, STATE = keys.secret_key(
    BASE_DIR)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # for 'dj_rest_auth.registration'
    'django.contrib.sites',

    # DRF(pip install djangorestframework)
    'rest_framework',
    'rest_framework.authtoken',

    # for 'dj_rest_auth.registration'
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Naver
    # from django.conf import settings
    # SocialApp.objects.create(provider="Naver", name="Naver", client_id=settings.NAVER_CLIENT_KEY, secret=settings.NAVER_SECRET_KEY)
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',

    # Social Login(pip install dj-rest-auth)
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # App
    'authentication',

    # Extensions
    'django_extensions',
]

# site 자동 변경에 대해서
# python manage.py shell_plus
# site = Site.objects.first()
# localhost:8000
# site 의 id로 개발서버인 127.0.0.1:800을 사용하고 싶으면
# Site model의 id를 해당 url로 입력해주면 된다.
SITE_ID = 3

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}

REST_USE_JWT = True

JWT_AUTH_COOKIE = 'token'
JWT_AUTH_REFRESH_COOKIE = 'refresh-token'


# 참고 (https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html)
SIMPLE_JWT = {
    # Access token 의 lifetime
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    # Refresh token 의 lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    # Refresh token과 Access token 을 새로운 시간에 맞춰 발행
    # 만약 BLACKLIST_AFTER_ROTATION 이 True 인 경우 사용된 Refresh token 은 자동으로 blacklist 에 추가
    'ROTATE_REFRESH_TOKENS': False,
    # 이 기능을 사용하려면 settings.py 의 INSTALLED_APPS 에 'rest_framework_simplejwt.token_blacklist' 를 추가
    'BLACKLIST_AFTER_ROTATION': False,
    # 설정되면 auth_user table 에 last_login field 가 업데이트 됨
    'UPDATE_LAST_LOGIN': False,
    # Token 의 알고리즘
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,

    'AUTH_HEADER_TYPES': ('token',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}

# OSError [Errno 99] 안나오도록 하기 위해서 설정
# rest_auth 가 email verification 을 위한 신호를 보내서 생기는 오류
ACCOUNT_EMAIL_VERIFICATION = 'none'

AUTH_USER_MODEL = 'authentication.User'
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'authentication.api.serializers.UserSerializer',
}
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'authentication.api.serializers.UserRegistrationSerializer',
}
ACCOUNT_ADAPTER = 'authentication.api.adapters.UserAdapter'

SOCIALACCOUNT_PROVIDERS = {
    'kakao': {
        'APP':{
            'client_id':KAKAO_REST_API_KEY,
            'secret':KAKAO_SECRET_KEY,
            'key':''
        }
    },
    'naver': {
        'APP':{
            'client_id':NAVER_CLIENT_KEY,
            'secret':NAVER_SECRET_KEY,
            'key':''
        }
    }
}
