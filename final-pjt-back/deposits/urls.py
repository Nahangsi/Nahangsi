from django.urls import path
from . import views

urlpatterns = [
   # 금융 상품 가져오는 url
   path('save-deposit-products/', views.save_deposit_products),

]
