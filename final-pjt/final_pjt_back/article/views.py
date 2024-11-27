from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Comment
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
# Create your views here.


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':  # 게시글 전체조회
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST': # 게시글 생성
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def article_detail(request,article_pk):
    article = Article.objects.get(pk = article_pk)
    if request.method == 'GET': # 게시글 상세조회
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT': # 게시글 수정
        if article.user != request.user:
            return Response({"게시글 수정 권한이 없습니다."},status=status.HTTP_403_FORBIDDEN)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': # 게시글 삭제
        if article.user != request.user:
            return Response({"게시글 삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        article.delete()
        message = {'article_delete' : f'{article_pk}번의 {article.title}글 삭제 완료'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def comment_list(request, article_pk):
    if request.method == 'GET': # 댓글 전체 조회
        article = get_object_or_404(Article, pk = article_pk)
        comments = Comment.objects.filter(article=article)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    if request.method == 'POST': # 댓글 생성
        article = get_object_or_404(Article, pk= article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article,user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT','DELETE'])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'PUT':  # 댓글 수정 - Comment 테이블에 userId 있다고 가정
        if comment.user != request.user:
            return Response({"댓글 수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': # 댓글 삭제 - Comment 테이블에 userId 있다고 가정
        if comment.user != request.user:
            return Response({"댓글 삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        message = {'comment_delete' : f'{comment_pk}번 댓글 삭제 완료'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)