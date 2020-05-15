from django.db import models
import uuid


class Task(models.Model):
    user = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500)
    done = models.BooleanField(default=False)
    unique_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self):
        return f'ID: {self.unique_id}, CREATED: {self.created}'
