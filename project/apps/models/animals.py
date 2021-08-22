from django.db import models
from django.db.models.deletion import CASCADE

from apps.models.user import User


class Animal(models.Model):
    name = models.CharField(max_length=10, blank=True)
    owner = models.ForeignKey(User, on_delete=CASCADE)


class Pet(Animal):
    # Pet model has name and owner fields from Animal.
    # But Pet model and Animal model will create different tables for each.
    pet_register_num = models.IntegerField()
