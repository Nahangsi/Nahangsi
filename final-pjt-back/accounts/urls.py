from django.urls import path, include
from .import views
from .views import CustomRegisterView, CustomUserDetailsView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer




urlpatterns = [
    # 기본 auth 기능
    path('', include('dj_rest_auth.urls')),
    # 회원가입
     path('signup/', CustomRegisterView.as_view()),
    # 유저 정보 조회
    path('user_info/', views.user_info),
    # 유저 정보 업데이트
    path('user_detail/', CustomUserDetailsView.as_view()),
    # 유저 탈퇴
    path('user_delete/', views.user_delete),
    # 비밀번호 바꾸기
    path('change_password/', views.change_password),
]