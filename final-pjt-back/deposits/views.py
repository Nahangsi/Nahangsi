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
    depositoptions = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer(depositoptions, many=True)
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
    savingoptions = SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer(savingoptions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 사용자별 금융 상품 추천 결과 반환
@api_view(['GET'])
def recommendation(request):
    # 사용자가 선택한 상품의 fin_prdt_cd를 받아옴
    fin_prdt_cd = request.GET.get('fin_prdt_cd')
    # 해당 상품의 상품군을 받아옴
    fin_prdt_cd_group = fin_prdt_cd[:2]
    # 해당 상품의 금리를 받아옴
    fin_prdt_cd_interest = DepositOptions.objects.get(fin_prdt_cd=fin_prdt_cd).intr_rate
    # 해당 상품의 만기를 받아옴
    fin_prdt_cd_mtrt_int = DepositOptions.objects.get(fin_prdt_cd=fin_prdt_cd).mtrt_int
    # 해당 상품의 가입금액을 받아옴
    fin_prdt_cd_join_member = DepositOptions.objects.get(fin_prdt_cd=fin_prdt_cd).join_member
    # 해당 상품의 가입기간을 받아옴
    fin_prdt_cd_save_trm = DepositOptions.objects.get(fin_prdt_cd=fin_prdt_cd).save_trm
    # 해당 상품의 가입방법을 받아옴
    fin_prdt_cd_intr_rate_type = DepositOptions.objects.get(fin_prdt_cd=fin_prdt_cd).intr_rate_type

    # 해당 상품의 상품군과 금리가 같은 상품을 추천
    fin_prdt_cd_group_list = DepositOptions.objects.filter(fin_prdt_cd__startswith=fin_prdt_cd_group, intr_rate=fin_prdt_cd_interest).exclude(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(fin_prdt_cd_group_list, many=True)
    
    
