from django.contrib import admin

from .models import (
    Project,
    ProjectGroup,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'description',
        'project_group',
        'token',
    )
    list_filter = (
        'project_group',
    )


@admin.register(ProjectGroup)
class ProjectGroupAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'description',
    )
