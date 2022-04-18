from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (AddCommentViewSet, ArticleViewSet, CommentsViewSet,
                    ViewCommentViewSet)

router = SimpleRouter()

router.register('article', ArticleViewSet, basename='article')
router.register(r"article/(?P<article_id>\d+)/comment/(?P<parent_id>\d+)",
                AddCommentViewSet, basename="comments_to_comment",)
router.register(r'article/(?P<article_id>\d+)/comment', CommentsViewSet,
                basename='comments_to_article',)
router.register('comments', ViewCommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
