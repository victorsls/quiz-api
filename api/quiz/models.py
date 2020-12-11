from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    text = models.TextField('Question text')
    answers = models.ManyToManyField('Answer', related_name='answers')
    right_answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'question'
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Answer(models.Model):
    text = models.TextField('Answer text')

    class Meta:
        db_table = 'answer'
        verbose_name = 'answer'
        verbose_name_plural = 'answers'


class Quiz(models.Model):
    questions = models.ManyToManyField('Question', related_name='questions')
    points = models.IntegerField('Points')
    player = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'quiz'
        verbose_name = 'quiz'
        verbose_name_plural = 'quizzes'
