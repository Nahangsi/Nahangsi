from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


# 게시글 전체 조회 && 작성
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글 상세 조회 && 수정 && 삭제
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUSET)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        user = request.user
        if user in article.like_users.all():
            article.like_users.remove(user)
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            article.like_users.add(user)
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)

    
# 댓글 전체 조회
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 댓글 상세 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # 일단 먼저 게시글 조회
    article = Article.objects.get(pk=article_pk)
    # 사용자가 입력한 뎃글의 content가 있을거심
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
    # if serializer.is_valid(): => 기본이 False라 실패했을때의 경우를 적어줘야 한다..
        serializer.save(article.article) # article 클래스의 article을 넣어준다(commit=False와 기능 같음)
        # 생성된 결과물을 리턴, 생성에 대한 성공 메세지 또한 return
        return Response(serializer.data, status=status.HTTP_201_CREATED)
