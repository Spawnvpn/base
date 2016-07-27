from car.models import Car
from django.contrib import admin


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
