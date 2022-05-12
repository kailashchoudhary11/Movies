from django.db import models

# Create your models here.
class Saved(models.Model):
    name = models.CharField(max_length=10000)
    