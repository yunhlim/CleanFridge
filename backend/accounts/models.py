from django.db import models
from django.contrib.auth.models import AbstractUser


class Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ingredient'


class User(AbstractUser):
    ingredients = models.ManyToManyField(Ingredient, through='Fridge')


class Fridge(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expiration_date = models.DateField()