from django.urls import path, include
from quiz.api import QuizListAPI


urlpatterns = [
    path("quizzes/", QuizListAPI.as_view())
]
