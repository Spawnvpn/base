from django.conf.urls import patterns, url
from django.contrib import admin

import car.views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$', car.views.view_all),
    url(r'^id(?P<id>\d)/$', car.views.different),
)
