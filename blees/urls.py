from django.conf.urls import patterns, include, url

from blees import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^measurement/(?P<room>.+)$', views.add_measurement),
                       )