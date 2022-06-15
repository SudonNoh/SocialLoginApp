from rest_framework import serializers
from authentication.models import User

from dj_rest_auth.registration.serializers import RegisterSerializer

# 회원가입이 완료된 후에 리턴 값에 관여
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]


class UserRegistrationSerializer(RegisterSerializer):
    # 기본 필드: username, password1, password2, email
    # 추가 필드: phone_number
    # phone_number = serializers.CharField(max_length=128)
    
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # data['phone_number'] = self.validated_data.get('phone_number', '')
        
        return data
