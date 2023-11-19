
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


class UserSerailzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'money', 'salary', 'financial_products', 'primary_bank', 'savings_goal', 'occupation', 'date_joined', 'last_login']


class CustomUserDetailSerializer(UserSerailzer):
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.CharField(), required=False)
    primary_bank = serializers.CharField(required=False)
    savings_goal = serializers.CharField(required=False)
    occupation = serializers.CharField(required=False)

    class Meta(UserSerailzer.Meta):
        fields = ['id', 'username', 'email', 'age', 'money', 'salary', 'financial_products', 'primary_bank', 'savings_goal', 'occupation']
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        data_dict['age'] = self.validated_data.get('age', None)
        data_dict['money'] = self.validated_data.get('money', None)
        data_dict['salary'] = self.validated_data.get('salary', None)
        data_dict['financial_products'] = self.validated_data.get('financial_products', None)
        data_dict['primary_bank'] = self.validated_data.get('primary_bank', None)
        data_dict['savings_goal'] = self.validated_data.get('savings_goal', None)
        data_dict['occupation'] = self.validated_data.get('occupation', None)

        return data_dict
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.age = validated_data.get('age', instance.age)
        instance.money = validated_data.get('money', instance.money)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.financial_products = validated_data.get('financial_products', instance.financial_products)
        instance.primary_bank = validated_data.get('primary_bank', instance.primary_bank)
        instance.savings_goal = validated_data.get('savings_goal', instance.savings_goal)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.save()

        return instance
    
    def save(self):
        user = super().save()
        user.age = self.cleaned_data.get('age')
        user.money = self.cleaned_data.get('money')
        user.salary = self.cleaned_data.get('salary')
        user.financial_products = self.cleaned_data.get('financial_products')
        user.primary_bank = self.cleaned_data.get('primary_bank')
        user.savings_goal = self.cleaned_data.get('savings_goal')
        user.occupation = self.cleaned_data.get('occupation')
        user.save()
        return user