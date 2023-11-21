from rest_framework import serializers
from .models import *

# 예금 상품
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

# 예금 옵션
class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

# 적금 상품
class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

# 적금 옵션 
class SavingOptionsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)

# 예금 상품 이름만 뽑아올 시리얼라이저
class SelectDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = ('fin_prdt_nm',)

# 적금 상품 이름만 뽑아올 시리얼라이저
class SelectSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = ('fin_prdt_nm',)
