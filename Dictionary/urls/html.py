from django.conf.urls import patterns, include, url
from Dictionary.views.html import WordCreate, WordDetail, WordUpdate, WordDelete, Home, WordSearch, PatternDetail, \
    PatternCreate, PatternUpdate, PatternApply

urlpatterns = patterns('',
    url(r'^search/$', WordSearch.as_view(), name='word.search'),
    url(r'^word/add/$', WordCreate.as_view(), name='word.create'),
    url(r'^word/(?P<pk>\d+)/$', WordDetail.as_view(), name='word.detail'),
    url(r'^word/(?P<pk>\d+)/edit/$', WordUpdate.as_view(), name='word.update'),
    url(r'^word/(?P<pk>\d+)/delete/$', WordDelete.as_view(), name='word.delete'),
    url(r'^pattern/add/', PatternCreate.as_view(), name='pattern.create'),
    url(r'^pattern/(?P<pk>\d+)/$', PatternDetail.as_view(), name='pattern.detail'),
    url(r'^pattern/(?P<pk>\d+)/edit/$', PatternUpdate.as_view(), name='pattern.update'),
    url(r'^pattern/(?P<pk>\d+)/apply/$', PatternApply.as_view(), name='pattern.apply'),
    url(r'^$', Home.as_view(), name='home'),
)