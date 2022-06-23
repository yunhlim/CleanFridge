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