from rest_framework import serializers

from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    child_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'article',
            'number',
            'parent',
            'child_comment',
        )

    def get_child_comment(self, obj):
        queryset = Comment.objects.filter(parent=obj, number__lte=3)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            'id',
            'text',
            'comments'
        )

    def get_comments(self, obj):
        queryset = Comment.objects.filter(article=obj, parent=None)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class ViewCommentSerializer(serializers.ModelSerializer):
    child_comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'article',
            'number',
            'parent',
            'child_comment',
        )

    def get_child_comment(self, obj):
        queryset = Comment.objects.filter(parent=obj)
        serializer = ViewCommentSerializer(queryset, many=True)
        return serializer.data
