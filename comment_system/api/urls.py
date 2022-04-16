from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import APIAddComments, APIComments, APIViewComment, ArticleViewSet

router = SimpleRouter()

router.register('article', ArticleViewSet, basename='article')


urlpatterns = [
    path('', include(router.urls)),
    path('article/<int:id>/comment/<int:parent_id>/',
         APIAddComments.as_view()),
    path('article/<int:id>/comment/', APIComments.as_view()),
    path('comments/', APIViewComment.as_view())
]
