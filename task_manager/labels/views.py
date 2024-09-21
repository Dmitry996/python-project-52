from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from task_manager.mixins import PermissionMixin
from .models import Label
from .forms import LabelForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class LabelMixin(SuccessMessageMixin,
                 LoginRequiredMixin,
                 PermissionMixin):
    model = Label
    success_url = reverse_lazy('labels')


class ListLabelsView(LabelMixin, ListView):
    template_name = 'labels/labels.html'


class CreateLabelView(LabelMixin, CreateView):
    form_class = LabelForm
    template_name = 'form.html'
    success_message = _('Label successfully created')
    extra_context = {'title': _('Create label'), 'button': _('Create')}


class UpdateLabelView(LabelMixin, UpdateView):
    form_class = LabelForm
    template_name = 'form.html'
    success_message = _('Label successfully changed')
    extra_context = {'title': _('Update label'), 'button': _('Change')}


class DeleteLabelView(LabelMixin, DeleteView):
    template_name = 'labels/delete.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(
                self.request,
                _('Label successfully deleted')
            )
            return redirect(reverse_lazy('labels'))

        except ProtectedError:
            messages.error(
                self.request,
                _("It is not possible to delete the label because it is in use")
            )
            return redirect(reverse_lazy('labels'))
