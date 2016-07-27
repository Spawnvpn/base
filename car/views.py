from django.http import HttpResponse

from .models import *


def test(request):
    qs = Car.objects.all()
    qs = qs.filter()
    qs = qs.exclude()
    qs.order_by()

    return HttpResponse("OK")
