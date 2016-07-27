from django.conf.urls import patterns, url
from django.contrib import admin

import car.views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),

    url(r'^$', car.views.test)
)
