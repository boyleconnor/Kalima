from django.conf.urls import patterns, include, url
from Main.views import HomeView, WordView


urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home'),
    url('^word/(?P<pk>\d+)/$', WordView.as_view(), name='word'),
)
