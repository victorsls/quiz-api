from rest_framework.serializers import ModelSerializer

from api.quiz.models import Question, Answer


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['text', 'answers', 'right_answer']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text']
