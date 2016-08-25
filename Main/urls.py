from django.conf.urls import patterns, include, url
from Main.views import HomeView, WordView, AddWordView, view_pattern, add_pattern, apply_pattern, edit_pattern, delete_pattern


urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home'),
    url('^word/(?P<pk>\d+)/$', WordView.as_view(), name='word'),
    url('^word/add/$', AddWordView.as_view(), name='add_word'),
    url('^pattern/(?P<pk>\d+)/$', view_pattern, name='pattern'),
    url('^pattern/add/$', add_pattern, name='add_pattern'),
    url('^pattern/(?P<pk>\d+)/apply/$', apply_pattern, name='apply_pattern'),
    url('^pattern/(?P<pk>\d+)/edit/$', edit_pattern, name='edit_pattern'),
    url('^pattern/(?P<pk>\d+)/delete/$', delete_pattern, name='delete_pattern'),
)
