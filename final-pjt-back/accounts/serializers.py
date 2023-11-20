# 11-17 10:56 경범 회원가입 커스텀 기능 추가

from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model


# 회원가입 시리얼라이저 커스텀
class CustomRegisterSerializer(RegisterSerializer):
# 기본 설정 필드: username, password, email
# 추가할 필드들을 정의합니다.
# write_only 필드 :보여주지 않고, 쓰기만 가능한 필드
    password1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    # 값은 텍스트로 받지만 저장은인티져로 하는듯? 금융코드로
    financial_products = serializers.ListField(child=serializers.CharField(max_length = 255), required=False)
    primary_bank = serializers.CharField(required=False, max_length = 255)
    savings_goal = serializers.CharField(required=False, max_length = 50)
    occupation = serializers.CharField(required=False, max_length = 50)
    savings_term = serializers.IntegerField(required=False)

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
        'savings_term' : self.validated_data.get('savings_term', '')
    }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


# 유저 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'age', 'money', 'salary', 'financial_products', 'primary_bank', 'savings_goal', 'occupation', 'savings_term']


# 유저 수정 시리얼라이저
class CustomUserDetailsSerializer(UserDetailsSerializer):
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.CharField(max_length=50), required=False)
    primary_bank = serializers.CharField(required=False)
    savings_goal = serializers.CharField(required=False)
    occupation = serializers.CharField(required=False)
    savings_term = serializers.IntegerField(required=False)

    class Meta(UserDetailsSerializer.Meta):
        # 기본적으로 pk, username, email, first_name, last_name 출력함(UserDetailsSerializer.Meta.fields)
        fields = UserDetailsSerializer.Meta.fields + ('age', 'money', 'salary', 'financial_products', 'primary_bank', 'savings_goal', 'occupation', 'savings_term')
        # 안 넣으면 빈값 허용 한딩...
        read_only_fields = ('username',)

    def get_cleaned_data(self):
        data_dict  = {}
        # data_dict = super().get_cleaned_data()

        data_dict['age'] = self.validated_data.get('age', None)
        data_dict['money'] = self.validated_data.get('money', None)
        data_dict['salary'] = self.validated_data.get('salary', None)
        data_dict['financial_products'] = self.validated_data.get('financial_products', None)
        data_dict['primary_bank'] = self.validated_data.get('primary_bank', None)
        data_dict['savings_goal'] = self.validated_data.get('savings_goal', None)
        data_dict['occupation'] = self.validated_data.get('occupation', None)
        data_dict['savings_term'] = self.validated_data.get('savings_term', None)

        return data_dict
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.age = validated_data.get('age', None)
        instance.money = validated_data.get('money', instance.money)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.financial_products = validated_data.get('financial_products', instance.financial_products)
        instance.primary_bank = validated_data.get('primary_bank', instance.primary_bank)
        instance.savings_goal = validated_data.get('savings_goal', instance.savings_goal)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.savings_term = validated_data.get('savings_term', instance.savings_term)
        instance.save()

        return instance
    
    def save(self):
        user = super().save()
        user.age = self.validated_data.get('age')
        user.money = self.validated_data.get('money')
        user.salary = self.validated_data.get('salary')
        user.financial_products = self.validated_data.get('financial_products')
        user.primary_bank = self.validated_data.get('primary_bank')
        user.savings_goal = self.validated_data.get('savings_goal')
        user.occupation = self.validated_data.get('occupation')
        user.savings_term = self.validated_data.get('savings_term')
        user.save()

        return user
    