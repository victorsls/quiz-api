from rest_framework.viewsets import ModelViewSet

from api.quiz.models import Question, Answer
from api.quiz.serializers import QuestionSerializer, AnswerSerializer


class QuestionViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing Question.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing Answer.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
