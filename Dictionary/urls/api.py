from Dictionary.views import api
from django.conf.urls import url

urlpatterns = (
    url(r'^word/$', api.WordList.as_view(), name='word.api_list'),
    url(r'^word/(?P<pk>\d+)/$', api.WordDetail.as_view(), name='word.api_detail'),
)