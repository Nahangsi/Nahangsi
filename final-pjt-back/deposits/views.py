from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import requests
from .serializers import *
from .models import *

API_KEY = settings.API_KEY

@api_view(['GET'])
def save_deposit_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1,
    }
    response = requests.get(url, params=params).json()

    products = response.get('result').get('baseList')
    # print(products[0])
    if not DepositProducts.objects.all():
        for product_li in products:
            save_data = {
                'fin_prdt_cd' : product_li.get('fin_prdt_cd'),
                'kor_co_nm' : product_li.get('kor_co_nm'),
                'fln_prdt_nm' : product_li.get('fin_prdt_nm'),
                'etc_note' : product_li.get('etc_note'),
                'join_deny' : product_li.get('join_deny'), 
                'join_member' : product_li.get('join_deny'),
                'join_way' : product_li.get('join_way'),
                'spcl_cnd' : product_li.get('spcl_cnd'),
            }
            serializer = DepositProductsSerializer(data=save_data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    
    if not DepositOptions.objects.all():
        options = response.get('result').get('optionList')
        for option_li in options:
            product = DepositProducts.objects.get(fin_prdt_cd=option_li.get('fin_prdt_cd'))
            save_data = {
                'fin_prdt_cd' : option_li.get('fin_prdt_cd') if option_li.get('fin_prdt_cd') != None else -1 ,
                'intr_rate_type_nm' : option_li.get('intr_rate_type_nm') if option_li.get('intr_rate_type_nm') != None else -1 ,
                'intr_rate' : option_li.get('intr_rate') if option_li.get('intr_rate') != None else -1,
                'intr_rate2' : option_li.get('intr_rate2') if option_li.get('intr_rate2') != None else -1,
                'save_trm' : option_li.get('save_trm') if option_li.get('save_trm') != None else -1,
            }
            serializer = DepositOptionsSerializer(data=save_data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save(product = product)

    return JsonResponse(response)

