from django.conf.urls import patterns, include, url
from Main.views import HomeView, WordView, PatternView


urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home'),
    url('^word/(?P<pk>\d+)/$', WordView.as_view(), name='word'),
    url('^pattern/(?P<pk>\d+)/$', PatternView.as_view(), name='pattern'),
)
