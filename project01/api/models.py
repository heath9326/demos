from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime

# Create your models here.


class ToDo(models.Model):
    title = models.TextField(default='')
    body = models.TextField(default='', max_length='300')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True)

    objects = models.Manager()

    def __str__(self):
        return f'ToDo [{self.id}]: <{self.title}>'

    @property
    def json(self):
        return dict(
            id=self.id,
            title=self.title,
            body=self.body,
            completed=self.completed,
            created_at=self.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
            completed_at=self.completed_at.strftime("%m/%d/%Y, %H:%M:%S"),
        )
