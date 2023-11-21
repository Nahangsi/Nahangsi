# 11-17 10:56 경범 회원가입 커스텀 기능 추가

from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model


options =  [
    "우리SUPER주거래적금", "WON적금", "퍼스트가계적금", "내손안에 적금"
    "마이(My)적금", "영플러스적금", "내가만든 보너스적금", "IM스마트적금"
    "2030부산월드엑스포적금", "펫 적금", "저탄소 실천\n적금",
    "내맘대로 \n적금", "너만Solo\n적금", "해피라이프_여행스케치적금V",
    "여행스케치_남도투어적금", "VIP플러스적금", "텔레파시적금", "jBANK 저금통적금", 
    "더탐나는적금3", "MZ플랜적금", "탐이나요적금", "JB 다이렉트적금(자유적립식)",
    "JB 카드 재테크 적금\n(정기적립식)", "행복Dream적금", "BNK더조은자유적금",
    "BNK 위더스(With-us)자유적금", "주거래프리미엄적금", "IBK썸통장(자유적립식)",
    "IBK D-day적금(자유적립식)", "IBK탄소제로적금(자유적립식)", "IBK중기근로자우대적금\n(자유적립식)",
    "KDBdream 자유적금", "정기적금", "KDB Hi 자유적금", "KB국민프리미엄적금(정액)"
    "KB반려행복적금", "KB 특★한 적금", "신한 알.쏠 적금", "NH올원e 미니적금",
    "NH1934월복리적금", "NH내가Green초록세상적금", "NH고향사랑기부적금",
    "NH직장인월복리적금", "주거래하나 월복리적금", "내맘적금", "코드K 자유적금",
    "주거래우대 자유적금", "Sh평생주거래우대적금", "Sh해양플라스틱Zero!적금\n(정액적립식)", "헤이(Hey)적금(정액적립식)",
    "Sh월복리자유적금", "Sh해양플라스틱Zero!적금\n(자유적립식)", "헤이(Hey)적금(자유적립식)",
    "Sh수산물을좋아海적금", "카카오뱅크 자유적금", "카카오뱅크 26주적금", "토스뱅크 키워봐요 적금",
    "토스뱅크 굴비 적금", "토스뱅크 자유 적금", "토스뱅크 아이 적금",

    "WON플러스예금", "e-그린세이브예금", "DGB주거래우대예금(첫만남고객형)",
    "DGB행복파트너예금(일반형)", "DGB함께예금", "IM스마트예금", "LIVE정기예금",
    "더(The) 특판 정기예금", "더(The) 레벨업 정기예금", "미즈월복리정기예금", "스마트모아Dream정기예금",
    "굿스타트예금", "The플러스예금", "제주Dream\n정기예금\n(개인/만기\n지급식)",   
    "J정기예금\n(만기지급식)", "JB 다이렉트예금통장\n(만기일시지급식)", "JB 123 정기예금\n (만기일시지급식)",
    "BNK더조은정기예금", "BNK주거래우대정기예금", "IBK평생한가족통장(실세금리정기예금)",
    "i-ONE놀이터예금", "1석7조통장(정기예금)", "정기예금", "KDB 정기예금",
    "KB Star 정기예금", "쏠편한 정기예금", "NH왈츠회전예금 II", "NH내가Green초록세상예금",
    "NH올원e예금", "NH고향사랑기부예금", "하나의정기예금", "코드K 정기예금", "Sh평생주거래우대예금\n(만기일시지급식)",
    "Sh해양플라스틱Zero!예금\n(만기일시지급식)", "헤이(Hey)정기예금", "Sh첫만남우대예금",
    "카카오뱅크 정기예금", "토스뱅크 먼저 이자 받는 정기예금"
]

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
    # financial_products = serializers.StringRelatedField(required=False)
    # financial_products = serializers.ListField(child=serializers.MultipleChoiceField(options), required=False)
    # financial_products = serializers.ListField(child=serializers.CharField(max_length=355), required=False)
    financial_products = serializers.ListField(child=serializers.CharField(max_length=355), required=False)
    # financial_products = serializers.MultipleChoiceField(choices=options, required=False)
    primary_bank = serializers.CharField(required=False, max_length = 255)
    savings_goal = serializers.CharField(required=False, max_length = 50)
    occupation = serializers.CharField(required=False, max_length = 50)
    savings_term = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        obj = self.validated_data['financial_products']
        print(obj)
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
    