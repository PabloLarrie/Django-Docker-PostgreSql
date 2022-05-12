from django.db import models


class Country(models.Model):
    countryname = models.CharField(max_length=50)
    stores_count = models.IntegerField(default=0)


class Manager(models.Model):
    name = models.CharField(max_length=150)


class Store(models.Model):
    storename = models.CharField(max_length=50)
    workers_count = models.IntegerField(default=1)
    square_meters = models.IntegerField(default=1)
    location = models.CharField(max_length=150)
    managers = models.ManyToManyField("repertoire.Manager", related_name="store_managers")


class CountryStores(models.Model):
    country = models.ForeignKey("repertoire.Country", on_delete=models.CASCADE, related_name="country_stores")
    stores = models.ManyToManyField("repertoire.Store", related_name="country_stores")
