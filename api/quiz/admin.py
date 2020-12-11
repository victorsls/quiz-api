from django.contrib import admin

from api.quiz.models import Category, Question, Answer, Quiz

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
