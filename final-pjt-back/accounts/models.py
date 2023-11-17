from django.db import models
from django.contrib.auth.models import AbstractUser

# 11-17 10:56 경범 User 모델 내용 추가
# 주거래은행 , 저축목표, 직종 추가
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    ## 밑으로는 선택사항
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True) # 연봉
    salary = models.IntegerField(blank=True, null=True) # 자산
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True) # 가입 상품
    primary_bank = models.CharField(blank=True, max_length=50, null=True) # 주 거래은행
    savings_goal = models.CharField(blank=True, max_length=50, null=True) # 저축 목표
    occupation = models.CharField(blank=True, max_length=50, null=True) # 직종

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'