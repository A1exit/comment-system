from api.yasg import urlpatterns as doc_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls'))
]

urlpatterns += doc_urls
