from django.contrib import admin

from .models import Environment


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'project',
        'branch',
    )
    list_filter = (
        'project',
    )
