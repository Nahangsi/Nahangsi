# 11-17 13:$4 경범 수정 시리얼라이저 코드 생성
from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions

# 정기 예금 상품 
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
        
# 정기 예금 옵션 
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)

# 정기 적금상품
class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
        
# 정기 적금 옵션
class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)