from django.db import models


class Environment(models.Model):
    name = models.CharField(max_length=500)
