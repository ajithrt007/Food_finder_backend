# Generated by Django 5.0.4 on 2024-04-24 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuisinesrest',
            old_name='restaurent',
            new_name='restaurant',
        ),
    ]
