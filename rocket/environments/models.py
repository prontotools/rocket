from django.db import models

from projects.models import Project


class Environment(models.Model):
    name = models.CharField(max_length=500)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    branch = models.CharField(
        max_length=100,
        default='develop'
    )

    def __str__(self):
        return f'{self.project.name}: {self.name}'
