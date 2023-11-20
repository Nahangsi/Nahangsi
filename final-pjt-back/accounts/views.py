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
from django.contrib.auth.hashers import check_password

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

    def perform_update(self, serializer):
        serializer.save()



# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# @api_view(['PUT'])
# def user_update(request):
#     user = request.user
#     serializer = CustomUserDetailsSerializer(user, data=request.data, partial=True)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)

@api_view(['POST'])
def user_delete(request):
    user = request.user
    # vue에서 보낸 비밀번호
    password = request.data.get('password1', '')

    if user.is_authenticated:
        # 저장된 비밀번호와 입력된 비밀번호 일치 여부 확인
        if password and check_password(password, user.password):
            user.delete()
            return Response({'delete' : f'{user}님의 계정이 삭제되었습니다.'})
        else:
            return Response({'errer' : '틀린 비밀번호입니다!! 다시 도전해주세요 :)'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def change_password(request):
    user = request.user
    old_password = request.data.get('old_password', '')  # 이전 비밀번호
    new_password = request.data.get('new_password', '')  # 새로운 비밀번호

    if user.is_authenticated:
        # 이전 비밀번호와 현재 비밀번호가 일치하는지 확인
        if old_password and check_password(old_password, user.password):
            if new_password:
                user.set_password(new_password)
                user.save()
                return Response({'success' : f'{user}님의 비밀번호 변경완료 !'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': '새로운 비밀번호를 확인해주세요!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '이전 비밀번호를 확인해주세요!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)