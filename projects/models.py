from django.conf import settings
from django.db import models

USER_MODEL = settings.AUTH_USER_MODEL


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(USER_MODEL, related_name="projects")

    def __str__(self):
        return self.name
