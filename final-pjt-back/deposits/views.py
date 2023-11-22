from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import requests
from .serializers import *
from .models import *
from rest_framework import generics
from django.db.models import OuterRef, Subquery, Max

# API_KEY = settings.API_KEY
# 데이터 저장

@api_view(['GET'])
def save_deposit_products(request):
    api_key = '6cc8ddad19f72e1c6dac77032a46a8a8'
    url = f'http://finlife.fss.or.kr/finlifeapi/'
    params = {
        'auth' : api_key,
        'topFinGrpNo' : '020000',
        'pageNo' : 1,
    }
    deposit = 'depositProductsSearch.json'

    deposit_response = requests.get(url + deposit, params=params).json()
    deposit_base_list = deposit_response.get('result').get('baseList')
    deposit_option_list = deposit_response.get('result').get('optionList')

    deposit_base_serializer = DepositProductsSerializer(data=deposit_base_list, many=True)
    if deposit_base_serializer.is_valid(raise_exception=True):
        deposit_base_serializer.save()

    for deposit_option in deposit_option_list:
        deposit_option_serializer = DepositOptionsSerializer(data=deposit_option)
        if deposit_option_serializer.is_valid(raise_exception=True):
            deposit_product = DepositProducts.objects.get(fin_prdt_cd=deposit_option['fin_prdt_cd'])
            deposit_option_serializer.save(product=deposit_product)

    saving = 'savingProductsSearch.json'

    saving_response = requests.get(url + saving, params=params).json()
    saving_base_list = saving_response.get('result').get('baseList')
    saving_option_list = saving_response.get('result').get('optionList')

    saving_base_serializer = SavingProductsSerializer(data=saving_base_list, many=True)
    if saving_base_serializer.is_valid(raise_exception=True):
        saving_base_serializer.save()

    for saving_option in saving_option_list:
        saving_option_serializer = SavingOptionsSerializer(data=saving_option)
        if saving_option_serializer.is_valid(raise_exception=True):
            saving_product = SavingProducts.objects.get(fin_prdt_cd=saving_option['fin_prdt_cd'])
            saving_option_serializer.save(product=saving_product)
    return Response(saving_option_serializer.data, status=status.HTTP_200_OK)


# 정기 예금 상품 목록 반환
@api_view(['GET'])
def deposit_products(request):
    depositproducts = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(depositproducts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 특정 예금 상품의 옵션 리스트 반환
@api_view(["GET"])
def deposit_product_options(request, fin_prdt_cd):
    depositoptions = DepositOptions.objects.filter(product__fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(depositoptions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 적금 상품 목록 반환
@api_view(['GET'])
def saving_products(request):
    savingproducts = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(savingproducts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 특정 적금 상품의 옵션 리스트 반환
@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    savingoptions = SavingOptions.objects.filter(product__fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionsSerializer(savingoptions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 예금 상품 최고 우대 금리, 저축금리 정렬해서 반환
class DepositProductsSortView(generics.ListAPIView):
    # queryset = DepositProducts.objects.all().order_by('-product_intr_rate')
    serializer_class = DepositProductsSortSerializer

    def get_queryset(self):
        # DepositOptions를 상품별로 그룹화하고 각 그룹에서 최대 intr_rate를 가져오기
        max_intr_rates_subquery = DepositOptions.objects.filter(
            product=OuterRef('pk')
        ).values('product').annotate(max_intr_rate=Max('intr_rate')).values('max_intr_rate')[:1]

        # 모든 DepositOptions를 가져오면서 최대 intr_rate로 정렬하기
        sorted_deposit_options = DepositOptions.objects.annotate(
            max_intr_rate=Subquery(max_intr_rates_subquery)
        ).order_by('-max_intr_rate')

        # 정렬된 DepositOptions를 기준으로 DepositProducts 가져오기
        deposit_products_ids = sorted_deposit_options.values_list('product', flat=True)
        deposit_products = DepositProducts.objects.filter(pk__in=deposit_products_ids)

        return deposit_products

# 적금 상품 최고 우대 금리, 저축금리 정렬해서 반환
class SavingProductsSortView(generics.ListAPIView):
    serializer_class = SavingProductsSortSerializer