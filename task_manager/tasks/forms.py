from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name',
                  'description',
                  'statuse',
                  'executor',
                  'labels'
                  )
