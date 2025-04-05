from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]
    PRIORITY_CHOICES = [
        ("low", "low"),
        ("medium", "medium"),
        ("high", "high"),
        ("critical", "critical"),
    ]
    title = models.CharField(max_length=100)
    descr = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return f"{self.title} with priority {self.priority}"
    

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='comments/', blank=True, null=True)

    def __str__(self):
        return f"time: {self.created_at}, author: {self.author}"