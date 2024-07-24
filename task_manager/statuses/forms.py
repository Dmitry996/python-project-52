from django import forms
from .models import Statuse


class StatusForm(forms.ModelForm):

    class Meta:
        model = Statuse
        fields = ('name',)
