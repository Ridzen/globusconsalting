from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Questionnaire(models.Model):
    """Модель для анкеты"""
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    experience = RichTextUploadingField(default=None)
    city = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    question = RichTextUploadingField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'questionnare_db'
        verbose_name_plural = 'Анкеты'
        verbose_name = "Анкета"

    def __str__(self):
        return self.name
