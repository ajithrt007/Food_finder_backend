# Generated by Django 5.0.4 on 2024-04-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_restaurants_rest_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='rest_id',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
