from rest_framework import serializers

from apps.questionnaire.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = "__all__"

    def create(self, validated_data):
        new_questionnaire = Questionnaire.objects.create(**validated_data)
        return new_questionnaire