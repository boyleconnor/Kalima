from django.conf.urls import patterns, include, url
from Main.views import HomeView


urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home'),
)
