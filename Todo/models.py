from re import T
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
