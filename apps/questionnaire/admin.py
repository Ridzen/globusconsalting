from django.contrib import admin
from apps.questionnaire.models import Questionnaire


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass
