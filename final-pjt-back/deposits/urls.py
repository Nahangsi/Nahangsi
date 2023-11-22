# url 입니당
from django.urls import path
from . import views
from .views import DepositProductsSortView, SavingProductsSortView

urlpatterns = [
   # 금융 상품 가져오는 url
   path('save-deposit-product/', views.save_deposit_products),
   # 정기 예금 상품 목록 반환 
   path('deposit-product/', views.deposit_products),
   # 특정 예금 상품의 옵션 리스트 반환
   path('deposit-product/<str:fin_prdt_cd>/', views.deposit_product_options),
   # 적금 상품 목록 반환
   path('saving-product/', views.saving_products),
   # 특정 적금 상품 상세 정보 반환
   path('saving-product/<str:fin_prdt_cd>/', views.saving_product_options),
<<<<<<< HEAD
   # 예금 상품 최고 우대 금리, 저축금리 정렬해서 반환
   path('deposit-product-sort/', DepositProductsSortView.as_view()),
   # 적금 상품 최고 우대 금리, 저축금리 정렬해서 반환
   path('saving-product-sort/', SavingProductsSortView.as_view()),
=======
   # 예금 상품 중복 없이 반환
   path('get_info/', views.get_info),
   # 적금 상품 중복 없이 반환
   path('get_info2/', views.get_info2),
>>>>>>> fa6a661173855b4afbb32b5aa2ba05591c5121e2
]

