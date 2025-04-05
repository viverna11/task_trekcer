from django import forms
from django.forms.widgets import DateTimeInput
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "descr",
            "status",
            "priority",
            "due_date",
        ]
        widgets = {
            'due_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "All"),
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'media']
        widjets = {
            'media' : forms.FileInput()
        }
        