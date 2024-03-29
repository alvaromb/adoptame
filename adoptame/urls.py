# Static files on development
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from web.models import *
from web.views import *

urlpatterns = patterns('',
    # Home
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<page>\d+)$', HomeView.as_view()),

    # Accounts
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Animal
    url(r'^animal/(?P<pk>\d+)', AnimalView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
