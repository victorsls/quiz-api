# Generated by Django 3.1.4 on 2020-12-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20201211_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='points',
        ),
        migrations.AddField(
            model_name='quiz',
            name='answers',
            field=models.ManyToManyField(related_name='quiz_answers', to='quiz.Answer'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Score'),
        ),
    ]
