from Dictionary.forms import WordSearchForm
from django.conf.urls import patterns, include, url
from Dictionary.views import WordCreate, WordDetail, WordUpdate, WordDelete, Home, WordSearch, DeriverDetail, \
    DeriverCreate, DeriverUpdate, DeriverApply
from haystack.views import search_view_factory

urlpatterns = patterns('',
    url(r'word/search/$', WordSearch.as_view(), name='word.search'),
    url(r'word/add/$', WordCreate.as_view(), name='word.create'),
    url(r'word/(?P<pk>\d+)/$', WordDetail.as_view(), name='word.detail'),
    url(r'word/(?P<pk>\d+)/edit/$', WordUpdate.as_view(), name='word.update'),
    url(r'word/(?P<pk>\d+)/delete/$', WordDelete.as_view(), name='word.delete'),
    url(r'deriver/add/', DeriverCreate.as_view(), name='deriver.create'),
    url(r'deriver/(?P<pk>\d+)/$', DeriverDetail.as_view(), name='deriver.detail'),
    url(r'deriver/(?P<pk>\d+)/edit/$', DeriverUpdate.as_view(), name='deriver.update'),
    url(r'deriver/(?P<pk>\d+)/apply/$', DeriverApply.as_view(), name='deriver.apply'),
    url(r'$', Home.as_view(), name='home'),
)