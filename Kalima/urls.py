from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Kalima.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'dictionary', include('Dictionary.urls', namespace='dictionary')),

    url(r'^admin/', include(admin.site.urls)),
)
