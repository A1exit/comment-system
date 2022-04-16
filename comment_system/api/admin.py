from django.contrib import admin

from .models import Article, Comment

admin.site.register(Comment)
admin.site.register(Article)
