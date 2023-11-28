from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(models.Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()