from django.contrib import admin
from .models import Task


@admin.register(Task)
class StatusAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'created_at')