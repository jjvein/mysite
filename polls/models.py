from __future__ import unicode_literals
import datetime
from django.db import models

from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_recently_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Person(models.Model):
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField(default = 0)



