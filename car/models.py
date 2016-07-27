from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Engine(models.Model):
    name = models.CharField(max_length=255, blank=True, db_index=True)
    capacity = models.FloatField(max_length=10)
    number_of_cylinders = models.IntegerField(blank=True, null=True)
    valves = models.IntegerField()
    rpm = models.IntegerField()
    horsepower = models.IntegerField()

    def __str__(self):
        return self.name


class Dye(models.Model):
    kind = models.CharField(max_length=15)
    colour = models.CharField(max_length=30)


class Wheels(models.Model):
    brand = models.CharField(max_length=30)
    kind = models.CharField(max_length=30)  # metal, alloy, titanium
    diagonal = models.FloatField(max_length=3)
    width = models.FloatField(max_length=3)


class Car(models.Model):
    mark = models.CharField(max_length=30)
    series = models.CharField(max_length=30)
    engine = models.ForeignKey(Engine)
    color = models.ForeignKey(Dye)
    manufacturer_country = models.CharField(max_length=30)
    wheels = models.ManyToManyField(Wheels)
    options = models.TextField(max_length=300)

    def __str__(self):
        return "{} - {}".format(self.mark, self.series)
