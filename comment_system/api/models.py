from django.db import models


class Article(models.Model):
    text = models.TextField(
        verbose_name='Text'
    )


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name='comments',
        verbose_name='Article',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name='Comment_text'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='child_comment'
    )
    number = models.PositiveIntegerField(
        default=1,
        verbose_name='number'
    )
