from django.conf.urls import url
from django.contrib import admin

import cars.views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view=cars.views.CarListView.as_view(), name='car_list'),
    url(r'^cars/(?P<pk>\d+)/$', view=cars.views.CarDetailView.as_view(), name='car_detail'),
    url(r'^cars/create/$', view=cars.views.CarCreateView.as_view(), name='car_create'),
    url(r'^cars/(?P<pk>\d+)/update/$', view=cars.views.CarUpdateView.as_view(), name='car_update'),
    url(r'^cars/(?P<pk>\d+)/delete/$', view=cars.views.CarDeleteView.as_view(), name='car_delete'),
]
