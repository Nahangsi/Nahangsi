from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import *
from .models import *

# Create your views here.

# 11-17 13:51 경범 api에서 금융상품 정보를 저장할 수 있는 코드 작성

def getdepositsinfo_from_api(request):
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
            deposit_option_serializer.save(fin_prdt_cd=deposit_product)

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
            saving_option_serializer.save(fin_prdt_cd=saving_product)
    return Response(saving_option_serializer.data)
        

        