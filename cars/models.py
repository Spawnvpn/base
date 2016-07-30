from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Engine(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    capacity = models.FloatField(max_length=10)
    number_of_cylinders = models.IntegerField(null=True, blank=True)
    valves = models.IntegerField(null=True, blank=True)
    rpm = models.IntegerField(null=True, blank=True)
    horsepower = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})


class Dye(models.Model):
    kind = models.CharField(max_length=15, null=True, blank=True)
    colour = models.CharField(max_length=30)

    def __str__(self):
        return self.colour

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})


class Wheels(models.Model):
    brand = models.CharField(max_length=30)
    kind = models.CharField(max_length=30)  # metal, alloy, titanium
    diagonal = models.FloatField(max_length=3, null=True, blank=True)
    width = models.FloatField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})


class Car(models.Model):
    mark = models.CharField(max_length=30)
    series = models.CharField(max_length=30)
    body = models.CharField(max_length=10, null=True, blank=True)
    engine = models.ForeignKey(Engine)
    color = models.ForeignKey(Dye)
    manufacturer_country = models.CharField(max_length=30, null=True, blank=True)
    wheels = models.ForeignKey(Wheels)
    cost = models.FloatField(max_length=20, null=True, blank=True)
    options = models.TextField(max_length=300, null=True, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return "{} - {}".format(self.mark, self.series)

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})
