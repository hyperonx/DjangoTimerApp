from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    task_name = models.CharField(max_length=40)
    # complete = models.BooleanField(default=False)
    # time = models.DurationField()
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.task_name
