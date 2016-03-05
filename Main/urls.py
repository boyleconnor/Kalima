from django.conf.urls import patterns, include, url
from Main.views import HomeView, WordView, AddWordView, PatternView


urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home'),
    url('^word/(?P<pk>\d+)/$', WordView.as_view(), name='word'),
    url('^word/add/$', AddWordView.as_view(), name='add_word'),
    url('^pattern/(?P<pk>\d+)/$', PatternView.as_view(), name='pattern'),
)
