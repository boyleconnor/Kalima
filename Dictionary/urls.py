from django.conf.urls import patterns, include, url
from django.contrib import admin
from Dictionary.views import WordCreate, WordDetail, WordUpdate, WordDelete

urlpatterns = patterns('',
    url(r'word/add/$', WordCreate.as_view(), name='word.create'),
    url(r'word/(?P<pk>\d+)/$', WordDetail.as_view(), name='word.detail'),
    url(r'word/(?P<pk>\d+)/edit/$', WordUpdate.as_view(), name='word.update'),
    url(r'word/(?P<pk>\d+)/delete/$', WordDelete.as_view(), name='word.delete')
)