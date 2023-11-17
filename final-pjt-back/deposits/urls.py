# 11-17 13:32 경범 url 생성
from django.urls import path
from . import views

urlpatterns = [
   # api에서부터 금융상품 가져오는 url 
   path('getdepositsinfo/', views.getdepositsinfo_from_api),

]
