from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = 'form.html'
    extra_context = {'title': _('Login'), 'button': _('Login')}
    next_page = reverse_lazy('home')
    success_message = _('Successfully login')


class LogoutView(SuccessMessageMixin, views.LogoutView):
    next_page = reverse_lazy('home')
    success_message = _('Successfully logout')
