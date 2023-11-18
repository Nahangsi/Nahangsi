from django.urls import path
from . import views

urlpatterns = [
   # 게시글 전체 조회 && 작성
   path('articles/', views.article_list),
   # 게시글 상세 조회 && 수정 && 삭제 && 좋아요
   path('articles/<int:article_pk>/', views.article_detail),
   # 댓글 전체 조회 
   path('comments/', views.comment_list),
   # 댓글 상세 조회, 수정, 삭제
   path('comments/<int:comment_pk>/', views.comment_detail),
   # 댓글 생성
   path('articles/<int:article_pk>/comments/', views.comment_create),
   # # 게시물 좋아요
   # path('articles/<int:article_pk>/likes/', views.likes),
]
