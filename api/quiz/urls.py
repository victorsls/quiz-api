from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.quiz.views import AnswerViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'answer', AnswerViewSet)
router.register(r'question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'quiz'
