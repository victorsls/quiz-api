from rest_framework import serializers

from api.quiz.exceptions import (
    MinimumQuestionsException, MissingQuestionsException, QuizAnsweredException, QuizNotFound
)
from api.quiz.models import Question, Answer, Quiz


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text', 'answers', 'right_answer', 'category']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['text', 'answers']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(read_only=True, many=True)

    def validate(self, attrs):
        if Question.objects.filter(category=attrs.get('category')).count() < 10:
            raise MinimumQuestionsException()
        return attrs

    def create(self, validated_data):
        category = validated_data.get('category')
        validated_data.update({
            'player': self.context['request'].user,
            'category': category
        })
        quiz = Quiz.objects.create(**validated_data)
        quiz.set_random_questions(category)
        return quiz

    class Meta:
        model = Quiz
        fields = ['id', 'category', 'questions']


class AnswerQuizSerializer(serializers.ModelSerializer):
    quiz_id = serializers.IntegerField(required=True, read_only=False)

    def validate(self, attrs):
        try:
            quiz = Quiz.objects.get(id=attrs.get('quiz_id'))
            if quiz.questions.count() > len(attrs.get('answers')):
                raise MissingQuestionsException()
            if quiz.answers.count() > 0:
                raise QuizAnsweredException()
        except Quiz.DoesNotExist:
            raise QuizNotFound()
        return attrs

    def save(self, **kwargs):
        quiz = Quiz.objects.get(id=kwargs.get('quiz_id'))
        quiz.set_answers(kwargs.get('answers'))
        quiz.calculate_score()

    class Meta:
        model = Quiz
        fields = ['answers', 'quiz_id']
