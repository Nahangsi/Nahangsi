from django.urls import path, include
from .import views
from .views import CustomRegisterView, CustomUserDetailsView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

urlpatterns = [
    # 유저 정보 조회
    path('user_info/', views.user_info),
    # 유저 정보 업데이트
    # path('user_detail/', CustomUserDetailsView.as_view())
    path('user_update/', views.user_update),
]