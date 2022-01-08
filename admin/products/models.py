from django.db import models
from django.db.models.base import Model

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass
