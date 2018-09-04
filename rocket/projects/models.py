from django.db import models


class Project(models.Model):
    name = models.SlugField(max_length=500)
    slug = models.SlugField(max_length=500)
    description = models.TextField(null=True, blank=True)
