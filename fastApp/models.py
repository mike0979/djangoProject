from django.db import models

# Create your models here.

class Table(models.Model):
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=200)