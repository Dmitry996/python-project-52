from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Statuse
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name=_('Task name'))

    description = models.TextField(verbose_name=_('Description'))

    statuse = models.ForeignKey(Statuse, on_delete=models.PROTECT,
                                null=True, verbose_name=_('Status'))

    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               null=True, verbose_name=_('Author'))

    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 verbose_name=_('Executor'))

    created_at = models.DateTimeField(auto_now_add=True)

    labels = ''
