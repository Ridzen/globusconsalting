from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# from django.contrib.auth import get_user_model

# Create your models here.


class PostCategories(models.Model):
    """Модель для категории постов"""
    title = models.CharField(max_length=255, unique=False)

    class Meta:
        verbose_name_plural = 'Категории постов'
        verbose_name = 'Категория поста'

    def __str__(self):
        return self.title


class Post(models.Model):
    """ Модель для постов """
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField()
    tag = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(
        to=PostCategories, on_delete=models.CASCADE, related_name='post',
        default=None, null=True
    )
    in_archive = models.BooleanField(default=False)

    class Meta:
        db_table = 'posts_db'
        verbose_name_plural = 'Посты'
        verbose_name = "Пост"

    def __str__(self):
        return self.title
