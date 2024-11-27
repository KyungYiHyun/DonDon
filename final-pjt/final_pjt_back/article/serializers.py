from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
user = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at', 'user_nickname',)

class ArticleSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at', 'user_nickname',)

    
class CommentListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'article', 'content', 'created_at', 'updated_at', 'user_nickname',)

class CommentSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'article', 'content', 'created_at', 'updated_at', 'user_nickname',)
