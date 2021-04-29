from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    entry_date = models.DateField()
    scale_feeling = models.IntegerField()
    goal_today = models.TextField()
    negative = models.TextField()
    overcome = models.TextField()
    goal_tomorrow = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}\'s entry #{self.id} on {self.entry_date}'
