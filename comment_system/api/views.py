from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
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


class APIComments(APIView):
    """ Creates comment to an article """
    def post(self, request, id):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data['article'] = id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class APIAddComments(APIView):
    """ Returns the article and comments up to the third level of nesting """
    def post(self, request, id, parent_id):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        parent = get_object_or_404(Comment, id=parent_id)
        request.data['article'] = id
        request.data['parent'] = parent_id
        request.data['number'] = parent.number + 1
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class APIViewComment(APIView):
    def get(self, request):
        """ Getting all nested comments for a level 3 comment """
        comment = Comment.objects.filter(
            article=request.data.get('article'),
            number=3)
        serializer = ViewCommentSerializer(comment, many=True)
        return Response(serializer.data)
