from django.urls import path, re_path 
from quiz.api import MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUserAnswer, SubmitQuizAPI


urlpatterns = [
    path("my-quizzes/", MyQuizListAPI.as_view()),
    path("quizzes/", QuizListAPI.as_view()),
    path("save-answer/", SaveUserAnswer.as_view()),
    re_path("quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view()),
    re_path("quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view()),
]
