from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UserAccessMixin:

    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                messages.error(self.request, _
                               ('You are not logged in! Please log in.'))
            )
            return redirect('login')

        elif not self.has_permission():
            messages.error(
                request,
                messages.error(self.request, _
                               ("You do not have the rights to change another user."))  # noqa: E501
            )
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class PermissionMixin:
    redirect_field_name = None

    def has_permission(self) -> bool:
        return self.get_object().author.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                messages.error(self.request, _
                               ('You are not logged in! Please log in.'))
            )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
