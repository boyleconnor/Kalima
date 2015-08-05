from Inflections import views
from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^inflection/$', views.InflectionList.as_view(), name='inflection.list'),
    url(r'^inflection/(?P<pk>\d+)/$', views.InflectionDetail.as_view(), name='inflection.detail'),
    url(r'^stem/$', views.StemList.as_view(), name='stem.list'),
    url(r'^stem/(?P<pk>\d+)/$', views.StemDetail.as_view(), name='stem.detail'),
    url(r'^stemmer/$', views.StemmerList.as_view(), name='stemmer.list'),
    url(r'^stemmer/(?P<pk>\d+)/$', views.StemmerDetail.as_view(), name='stemmer.detail'),
    url(r'^paradigm/$', views.ParadigmList.as_view(), name='paradigm.list'),
    url(r'^paradigm/(?P<pk>\d+)/$', views.ParadigmDetail.as_view(), name='paradigm.detail'),
    url(r'^inflecter/$', views.InflecterList.as_view(), name='inflecter.list'),
    url(r'^inflecter/(?P<pk>\d+)/$', views.InflecterDetail.as_view(), name='inflecter.detail'),
)
