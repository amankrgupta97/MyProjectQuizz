from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics 
from quiz.models import Quiz
from quiz.serializers import QuizListSerializer


class QuizListAPI(generics.ListAPIView):
    serializer_class = QuizListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Quiz.objects.filter(roll_out=True)
        #queryset = Quiz.objects.filter(roll_out=True).exclude(quiztaker_user=self.request.user)
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(Q(name_icontains=query) | Q(description_icontains=query)).distinct()

        return queryset