from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.quiz.views import AnswerViewSet, QuestionViewSet, StartQuizView, AnswerQuizView

router = DefaultRouter()
router.register(r'answer', AnswerViewSet)
router.register(r'question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('start-quiz', StartQuizView.as_view(), name='start_quiz'),
    path('answer-quiz', AnswerQuizView.as_view(), name='answer_quiz')
]

app_name = 'quiz'
