from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.views import UserDetailsView

# 회원 가입 시리얼라이저 커스텀
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)



#회원 정보 시리얼라이저 커스텀
class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def user_update(request):
    user = request.user
    serializer = CustomUserDetailsSerializer(user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)