from django.shortcuts import render
from rest_framework import generics
from QuestionSystem.models import Question,Answer
from django.db.models import Q
from QuestionSystem.serializers import QuestionListSerializer,AnswerListSerializer
class QuestionListAPI(generics.ListAPIView):
    serializer_class=QuestionListSerializer
    def get_queryset(self,*args,**kwargs):
        queryset=Question.objects.all()
        query=self.request.GET.get("q")
        return queryset
        # if query:
        #     queryset=queryset.filter(
        #         Q(name_icontains=query) | Q(description_icontains=query)
        #     ).distinct()
        # return queryset
class AnswerListAPI(generics.ListAPIView):
    serializer_class=AnswerListSerializer
    def get_queryset(self,*args,**kwargs):
        query=self.request.GET.get("question")
        queryset=Answer.objects.filter(question=query)
        return queryset

