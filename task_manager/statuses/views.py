from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from task_manager.utils import PermissionMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import Statuse
from .forms import StatusForm


class StatusesView(PermissionMixin, LoginRequiredMixin, SuccessMessageMixin):
    model = Statuse
    form_class = StatusForm
    success_url = reverse_lazy('statuses')


class ListStatusesView(StatusesView, ListView):
    template_name = 'statuses/statuses.html'


class CreateStatusView(StatusesView, CreateView):
    extra_context = {'title': _('Statuses'), 'button': _('Create')}
    template_name = 'form.html'
    success_message = _('Status successfully created')


class UpdateStatusView(StatusesView, UpdateView):
    template_name = 'form.html'
    extra_context = {'title': _('Statuses'), 'button': _('Change')}
    success_message = _('Status successfully changed')


class DeleteStatusView(StatusesView, DeleteView):
    template_name = 'statuses/delete.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(
                self.request,
                _('Status successfully deleted')
            )
            return redirect(reverse_lazy('statuses'))

        except ProtectedError:
            messages.error(
                self.request,
                _("It is not possible to delete the status because it is in use")  
            )
            return redirect(reverse_lazy('statuses'))
