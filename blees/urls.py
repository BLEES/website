from django.conf.urls import patterns, include, url

from blees import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^graphs/(?P<room_name>.+)$', views.room_last_week, name='graphs'),
                       url(r'^measurement/(?P<room>.+)$', views.add_measurement),
                       )