from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article',)

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class ArticleCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'   
