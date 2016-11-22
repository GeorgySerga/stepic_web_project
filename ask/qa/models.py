from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        self.oder_by('added_at')
    def popular():
        self.oder_by('likes')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author")
    likes = models.ManyToManyField(User, related_name="question_like", blank=True)
    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __str__(self):
        return 'Answer by {}'.format(self.author)