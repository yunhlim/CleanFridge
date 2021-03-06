# Generated by Django 3.2.12 on 2022-06-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('qnt', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'recipe_ingredient',
                'managed': False,
            },
        ),
    ]
