from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin

class TaskView():
    pass


class ListTasksView(ListView):
    pass


class CreateTaskView(CreateView):
    pass


class UpdateTaskView(UpdateView):
    pass


class DeleteTaskView(DeleteView):
    pass
