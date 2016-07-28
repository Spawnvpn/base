from django.http import HttpResponse

from .models import *


def view_all(request):
    qs = Car.objects.all()
    qs = qs.filter()
    qs = qs.exclude()
    qs.order_by()

    return HttpResponse(qs)


def different(request, id):
    qs = Car.objects.get(id=id)
    return HttpResponse(qs)
