from django.urls import path
from . import views

urlpatterns = [
   # 금융 상품 가져오는 url
   path('save-deposit-products/', views.save_deposit_products),
   # 정기 예금 상품 목록 반환 
   path('deposit-products/', views.deposit_products),
   # 정기 예금 상품 상세 정보 반환
   path('deposit-products/<int:product_id>/', views.deposit_product_detail),
   # 적금 상품 목록 반환
   path('saving-products/', views.saving_products),
   # 적금 상품 상세 정보 반환
   path('saving-products/<int:product_id>/', views.saving_product_detail),
]
