from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Question(models.Model):
    text = models.TextField('Question text')
    answers = models.ManyToManyField('Answer', related_name='answers')
    right_answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'question'
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Answer(models.Model):
    text = models.TextField('Answer text')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'answer'
        verbose_name = 'answer'
        verbose_name_plural = 'answers'


class Quiz(models.Model):
    questions = models.ManyToManyField('Question', related_name='quiz_questions')
    answers = models.ManyToManyField('Answer', related_name='quiz_answers')
    score = models.IntegerField('Score', default=0)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.player.username} - {self.score}'

    def set_random_questions(self, category):
        self.questions.set(Question.objects.order_by('?').filter(category=category).values_list('id', flat=True)[:10])

    def set_answers(self, answers):
        self.answers.set(answers)

    def calculate_score(self):
        answers = self.answers.all()
        for index, question in enumerate(self.questions.all()):
            if question.right_answer == answers[index]:
                self.score += 1
            else:
                self.score -= 1
        if self.score < 0:
            self.score = 0
        self.save()

    class Meta:
        db_table = 'quiz'
        verbose_name = 'quiz'
        verbose_name_plural = 'quizzes'
