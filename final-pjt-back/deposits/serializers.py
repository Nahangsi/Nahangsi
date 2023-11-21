from rest_framework import serializers
from .models import *

class DepositOptionslistSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        

# 예금 상품
class DepositProductsSerializer(serializers.ModelSerializer):
    depositoptions_set = DepositOptionslistSerializer(many=True, read_only=True)
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

class SavingOptionslistSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavingOptions
        fields = '__all__'

# 적금 상품 + 그 상품 옵션까지한꺼번에
class SavingProductsSerializer(serializers.ModelSerializer):
    savingoptions_set = SavingOptionslistSerializer(many=True, read_only=True)

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


