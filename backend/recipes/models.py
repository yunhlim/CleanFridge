from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    summary = models.CharField(max_length=254)
    nation = models.CharField(max_length=10)
    type = models.CharField(max_length=30)
    cooking_time = models.IntegerField()
    calorie = models.IntegerField(blank=True, null=True)
    qnt = models.IntegerField()
    level = models.CharField(max_length=10)
    price = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'recipe'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    qnt = models.CharField(max_length=20)
    type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'recipe_ingredient'


class RecipeProcess(models.Model):
    id = models.BigAutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)
    order = models.IntegerField()
    content = models.CharField(max_length=256)
    image_url = models.CharField(max_length=64, blank=True, null=True)
    tip = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_process'