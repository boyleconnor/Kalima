from django.conf.urls import patterns, include, url
from django.contrib import admin
from Kalima.views import DefaultView

urlpatterns = patterns('',
    url(r'^auth/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dictionary/', include('Dictionary.urls', namespace='dictionary')),
    url(r'^search/', include('haystack.urls')),
    url(r'^$', DefaultView.as_view()),
)
