from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from tasks import models


class TaskListView(ListView):
    model = models.Task
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = 'task'