from django.db import models
from django.utils import timezone

from datetime import timedelta

# Create your models here.

class Question(models.Model):
    def __str__(self):
        return self.question_text

    def is_recent(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self) -> str:
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

