from django.db import models

# Create your models here.
class Dummy(models.Model):
    name = models.CharField(max_length=10, blank=True)
