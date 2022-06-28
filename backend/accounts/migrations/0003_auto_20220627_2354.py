# Generated by Django 3.2.12 on 2022-06-27 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='ingredients',
            field=models.ManyToManyField(through='accounts.Fridge', to='accounts.Ingredient'),
        ),
    ]