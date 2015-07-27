from Dictionary import views
from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^word/$', views.WordListJSON.as_view(), name='word.list'),
    url(r'^word/(?P<pk>\d+)/$', views.WordDetailJSON.as_view(), name='word.detail'),
    url(r'^word/html/$', views.WordListHTML.as_view(), name='word.list.html'),
    url(r'^word/(?P<pk>\d+)/html/$', views.WordDetailHTML.as_view(), name='word.detail.html'),
    url(r'^pattern/$', views.PatternListJSON.as_view(), name='pattern.list'),
    url(r'^pattern/(?P<pk>\d+)/$', views.PatternDetailJSON.as_view(), name='pattern.detail'),
    url(r'^apply/$', views.PatternApplyJSON.as_view(), name='apply')
)
