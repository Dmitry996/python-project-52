from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import PermissionMixin


class TaskMixin(SuccessMessageMixin, LoginRequiredMixin, PermissionMixin):
    model = Task
    success_url = reverse_lazy('tasks')


class TaskView(TaskMixin, DetailView):
    template_name = 'tasks/detail.html'


class ListTasksView(TaskMixin, ListView):
    template_name = 'tasks/tasks.html'


class CreateTaskView(TaskMixin, CreateView):
    template_name = 'form.html'
    form_class = TaskForm
    success_message = _('The task has been successfully created')
    extra_context = {'title': _('Create task'), 'button': _('Create')}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(TaskMixin, UpdateView):
    template_name = 'form.html'
    form_class = TaskForm
    extra_context = {'title': _('Update task'), 'button': _('Change')}
    success_message = _('The task has been successfully changed')


class DeleteTaskView(TaskMixin, DeleteView):
    template_name = 'tasks/delete.html'
    success_message = _('Task successfully deleted')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                _("You are not logged in! Please log in.")
            )
            return self.handle_no_permission()

        elif not self.has_permission():
            messages.error(
                request,
                _("Only the author of the task can delete it.")
            )
            return redirect('home_tasks')
        return super().dispatch(request, *args, **kwargs)
