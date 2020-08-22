from rest_framework import serializers
from QuestionSystem.models import Question, Answer
class QuestionListSerializer(serializers.ModelSerializer):
    # question_count=serializers.SerializerMethodField()
    class Meta:
        model=Question
        fields = '__all__'
class AnswerListSerializer(serializers.ModelSerializer):
    # question_count=serializers.SerializerMethodField()
    class Meta:
        model=Answer
        fields = '__all__'
