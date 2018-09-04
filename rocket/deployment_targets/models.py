from django.db import models

from environments.models import Environment


class DeploymentTarget(models.Model):
    name = models.CharField(max_length=500)
    ip = models.CharField(max_length=100)
    environment = models.ForeignKey(
        Environment,
        on_delete=models.CASCADE
    )
