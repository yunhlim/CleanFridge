# Generated by Django 3.2.12 on 2022-06-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipeingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeProcess',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField()),
                ('content', models.CharField(max_length=256)),
                ('image_url', models.CharField(blank=True, max_length=64, null=True)),
                ('tip', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'recipe_process',
                'managed': False,
            },
        ),
    ]