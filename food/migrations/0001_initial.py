# Generated by Django 5.0.4 on 2024-04-24 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=220)),
                ('city_code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.IntegerField(unique=True)),
                ('country', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('locality', models.CharField(max_length=300)),
                ('longitude', models.CharField(max_length=50)),
                ('lattitude', models.CharField(max_length=50)),
                ('avg_cost', models.FloatField()),
                ('has_table', models.BooleanField()),
                ('has_delivery', models.BooleanField()),
                ('is_delivering', models.BooleanField()),
                ('switch_to', models.BooleanField()),
                ('price_range', models.IntegerField()),
                ('rating', models.FloatField()),
                ('rating_color', models.CharField(max_length=50)),
                ('rating_txt', models.CharField(max_length=50)),
                ('votes', models.IntegerField()),
                ('city_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.city')),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.currency')),
            ],
        ),
        migrations.CreateModel(
            name='CuisinesRest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.cuisines')),
                ('restaurent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.restaurants')),
            ],
        ),
    ]
