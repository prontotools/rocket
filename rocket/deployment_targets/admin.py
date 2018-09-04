from django.contrib import admin

from .models import DeploymentTarget


@admin.register(DeploymentTarget)
class DeploymentTargetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ip',
        'environment',
    )
    list_filter = (
        'environment',
    )
