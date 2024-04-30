from django.db import models

# Create your models here.
class Country(models.Model):
    country_code=models.IntegerField(unique=True)
    country=models.CharField(max_length=120)

class City(models.Model):
    city=models.CharField(max_length=220)
    city_code=models.IntegerField(unique=True)

class Currency(models.Model):
    currency=models.CharField(max_length=50)

class Restaurants(models.Model):
    id = models.AutoField(primary_key=True)
    rest_id=models.IntegerField(unique=True)
    name=models.CharField(max_length=200)
    country_code=models.ForeignKey(Country,on_delete=models.CASCADE,to_field="country_code")
    city_code=models.ForeignKey(City,on_delete=models.CASCADE,to_field="city_code")
    address=models.CharField(max_length=300)
    locality=models.CharField(max_length=300)
    longitude=models.FloatField()
    lattitude=models.FloatField()
    avg_cost=models.FloatField()
    currency=models.ForeignKey(Currency,on_delete=models.CASCADE)
    has_table=models.BooleanField()
    has_delivery=models.BooleanField()
    is_delivering=models.BooleanField()
    switch_to=models.BooleanField()
    price_range=models.IntegerField()
    rating=models.FloatField()
    rating_color=models.CharField(max_length=50)
    rating_txt=models.CharField(max_length=50)
    votes=models.IntegerField()

class Cuisines(models.Model):
    cuisine=models.CharField(max_length=50)

class CuisinesRest(models.Model):
    cuisine=models.ForeignKey(Cuisines,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurants,on_delete=models.CASCADE,to_field="rest_id")