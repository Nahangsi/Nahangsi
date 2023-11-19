
# 11-17 10:56 경범 회원가입 커스텀 기능 추가

from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.CharField(), required=False)
    primary_bank = serializers.CharField(required=False)
    savings_goal = serializers.CharField(required=False)
    occupation = serializers.CharField(required=False)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'age': self.validated_data.get('age', ''),
            'money': self.validated_data.get('money', ''),
            'salary': self.validated_data.get('salary', ''),
            'financial_products': self.validated_data.get('financial_products', ''),
            'primary_bank': self.validated_data.get('primary_bank', ''),
            'savings_goal': self.validated_data.get('savings_goal', ''),
            'occupation': self.validated_data.get('occupation', ''),
            }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user

class CustomUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 사용자 모델 설정
        fields = ('id', 'username', 'email', 'age', 'money', 'salary', 'financial_products', 'primary_bank', 'savings_goal', 'occupation')  # 필요한 필드들 추가

    # 필요한 경우 추가적인 유효성 검사 또는 필드 조작을 위한 메소드들을 정의할 수 있습니다.

