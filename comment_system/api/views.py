from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Comment
from .serializers import (ArticleSerializer, CommentSerializer,
                          ViewCommentSerializer)


class ArticleViewSet(viewsets.ModelViewSet):
    """creates and returns an article"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get', 'post']


class CommentsViewSet(viewsets.ModelViewSet):
    """ Creates comment to an article """
    serializer_class = CommentSerializer
    http_method_names = ['post']
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        article = get_object_or_404(Article, id=self.kwargs.get('article_id'))
        serializer.save(article=article)


class AddCommentViewSet(viewsets.ModelViewSet):
    """ Creates comment to comment """
    serializer_class = CommentSerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        article = get_object_or_404(Article, id=self.kwargs.get('article_id'))
        parent_comment = get_object_or_404(Comment, id=self.kwargs.get(
            'parent_id'))
        serializer.save(
            article=article,
            number=parent_comment.number + 1,
            parent=parent_comment,
        )


class APIViewComment(APIView):
    def get(self, request):
        """ Getting all nested comments for a level 3 comment """
        comment = Comment.objects.filter(
            article=request.data.get('article'),
            number=3)
        serializer = ViewCommentSerializer(comment, many=True)
        return Response(serializer.data)


class ViewCommentViewSet(viewsets.ModelViewSet):
    """ Getting all nested comments for a level 3 comment """
    serializer_class = ViewCommentSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Comment.objects.filter(
            article=self.request.data.get('article'),
            number=4)
