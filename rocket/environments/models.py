from django.db import models

from projects.models import Project


class Environment(models.Model):
    name = models.CharField(max_length=500)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
