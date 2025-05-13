from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class TaskStatus(models.TextChoices):
    RUNNING = 'running', 'Running'
    DONE = 'done', 'Done'

class ToDoTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices=TaskStatus.choices,default=TaskStatus.RUNNING.value)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.task} by {self.user} - {self.status}"