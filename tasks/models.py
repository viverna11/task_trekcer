from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]
    PRIORYTI_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('hight', 'Hight')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORYTI_CHOICES, default="medium")
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    def __str__(self):
        return f"{self.title} with priority {self.priority}"



