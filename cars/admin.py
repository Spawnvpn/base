from cars.models import Car, Engine, Dye, Wheels
from django.contrib import admin


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Engine)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Dye)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Wheels)
class CarAdmin(admin.ModelAdmin):
    pass
