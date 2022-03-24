from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=3)
    due_date = models.DateField()

    def __str__(self) -> str:
        return self.title