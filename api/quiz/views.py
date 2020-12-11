from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.quiz.models import Question, Answer, Quiz
from api.quiz.serializers import QuestionSerializer, AnswerSerializer, QuizSerializer, AnswerQuizSerializer


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


class StartQuizView(CreateAPIView):
    """
    A simple APIView to start the quiz
    """
    queryset = Quiz.objects.none()
    serializer_class = QuizSerializer


class AnswerQuizView(CreateAPIView):
    """
    A simple APIView to send quiz answers
    """
    queryset = Quiz.objects.none()
    serializer_class = AnswerQuizSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(**request.data)
        data = {'success': 'Your answers have been sent successfully and soon the score will enter the Ranking.'}
        return Response(data, status=status.HTTP_200_OK)
