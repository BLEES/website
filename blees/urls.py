from django.conf.urls import patterns, include, url

from blees import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )