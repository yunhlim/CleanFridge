from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ingredient'