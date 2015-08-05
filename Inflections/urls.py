from Inflections import views
from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^inflection/$', views.InflectionList.as_view(), name='inflection.list'),
    url(r'^inflection/(?P<pk>\d+)/$', views.InflectionDetail.as_view(), name='inflection.detail'),
)
