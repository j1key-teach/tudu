from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    STATUS_CHOICES = [
        ('todo', 'todo'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name
