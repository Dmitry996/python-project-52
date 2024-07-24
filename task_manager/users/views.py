from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from .forms import UserForm
from django.contrib.auth import get_user_model
from task_manager.utils import UserAccessMixin


class UsersView(SuccessMessageMixin):
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('users')


class ListUsersView(UsersView, ListView):
    template_name = 'users/users.html'


class CreateUserView(UsersView, CreateView):
    template_name = "form.html"
    extra_context = {'title': _('Registration'), 'button': _('Register')}
    success_message = _('The user has been successfully registered')


class UpdateUserView(UsersView, UserAccessMixin, UpdateView):
    template_name = "form.html"
    extra_context = {'title': _('Changing the user'), 'button': _('Change')}
    success_message = _('The user has been successfully changed')


class DeleteUserView(UsersView, UserAccessMixin, DeleteView):
    template_name = 'users/delete.html'
    success_message = _('The user has been successfully deleted')
