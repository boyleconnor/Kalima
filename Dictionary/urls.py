from django.conf.urls import patterns, include, url
from Dictionary.views import WordCreate, WordDetail, WordUpdate, WordDelete, Home

urlpatterns = patterns('',
    url(r'word/add/$', WordCreate.as_view(), name='word.create'),
    url(r'word/(?P<pk>\d+)/$', WordDetail.as_view(), name='word.detail'),
    url(r'word/(?P<pk>\d+)/edit/$', WordUpdate.as_view(), name='word.update'),
    url(r'word/(?P<pk>\d+)/delete/$', WordDelete.as_view(), name='word.delete'),
    url(r'$', Home.as_view(), name='home'),
)