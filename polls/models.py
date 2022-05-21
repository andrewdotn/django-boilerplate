from django.db import models
from django.db.models import CASCADE

DEFAULT_MAX_LENGTH = 255


class Question(models.Model):
    subject = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def answer_count(self):
        return self.answer_set.count()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    subject = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return self.subject


class Vote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
