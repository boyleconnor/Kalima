from Dictionary import views
from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^word/$', views.WordList.as_view(), name='word.list'),
    url(r'^word/(?P<pk>\d+)/$', views.WordDetail.as_view(), name='word.detail'),
    url(r'^pattern/$', views.PatternList.as_view(), name='pattern.list'),
    url(r'^pattern/(?P<pk>\d+)/$', views.PatternDetail.as_view(), name='pattern.detail'),
    url(r'^apply/$', views.PatternApply.as_view(), name='apply')
)
