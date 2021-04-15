from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    entry_date = models.DateField()
    scale_feeling = models.IntegerField()
    goal_today = models.TextField()
    negative = models.TextField()
    overcome = models.TextField()
    goal_tomorrow = models.TextField()

    def __str__(self):
        return f'Entry #{self.id}'
