from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
    url('^html/', include('Dictionary.urls.html')),
    url('^api/', include('Dictionary.urls.api', namespace='api')),
)