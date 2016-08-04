from cars.models import Car, Engine, Dye, Wheels
from django.contrib import admin


class CarListFilter(admin.SimpleListFilter):
    title = "Filter"
    parameter_name = "cost"

    def lookups(self, request, model_admin):
        # return [('12000', 'in 12000')]
        qs = model_admin.get_queryset(request)
        if qs.filter(cost__gt=10000, cost__lte=25000).exists():
            yield ('10000s', 'in 10000')

    def queryset(self, request, queryset):
        if self.value == '10000s':
            return queryset.filter(cost__gte=10000, cost__lte=25000)


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
