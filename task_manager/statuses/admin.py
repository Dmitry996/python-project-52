from django.contrib import admin
from .models import Statuse


@admin.register(Statuse)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'created_at')
