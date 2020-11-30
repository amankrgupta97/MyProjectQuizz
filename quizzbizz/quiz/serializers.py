from quiz.models import Quiz
from rest_framework import serializers


class QuizListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = ["id", "name", "description", "image", "slug","questions_count"]
        read_only_fields = ["questions_count"]
    
    def get_questions_count(self, obj):
        return obj.question_set.all().count()