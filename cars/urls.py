from django.conf.urls import url
from django.contrib import admin

import cars.views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view=cars.views.CarList.as_view(), name='car_list'),
    url(r'^/cars/(?P<pk>\d+)/$', view=cars.views.CarDetail.as_view(), name='car_detail'),
]
