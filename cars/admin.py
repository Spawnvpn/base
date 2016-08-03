from cars.models import Car, Engine, Dye, Wheels
from django.contrib import admin


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['mark', 'series', 'engine', 'color', 'wheels', 'cost', 'year', 'manufacturer_country']
    list_editable = ('series', 'engine', 'color', 'wheels', 'cost', 'year', 'manufacturer_country')


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'number_of_cylinders', 'horsepower', ]
    list_editable = ('capacity', 'number_of_cylinders', 'horsepower')


@admin.register(Dye)
class DyeAdmin(admin.ModelAdmin):
    pass


@admin.register(Wheels)
class WheelsAdmin(admin.ModelAdmin):
    pass
