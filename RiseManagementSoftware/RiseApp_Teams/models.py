from django.db import models
from django.contrib.auth.models import User as user
# Create your models here.
class Team(models.Model):
    title = models.CharField(max_length=50)
    members = models.ForeignKey(user, on_delete=models.CASCADE)
    def __str__(self):
        return self.title