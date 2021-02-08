from django.db import models
from django.contrib.auth.models import User as user
import rest_framework
from RiseApp_Teams.models import Team
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, default=1)
    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.title


