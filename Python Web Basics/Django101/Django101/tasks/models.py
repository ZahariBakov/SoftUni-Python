from django.db import models


class Task(models.Model):
    # varchar
    title = models.CharField(max_length=30)
    # text
    description = models.TextField()
    # integer
    priority = models.IntegerField(default=1)
