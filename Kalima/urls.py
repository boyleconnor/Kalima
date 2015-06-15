from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render


urlpatterns = patterns('',
    url(r'^auth/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dictionary/', include('Dictionary.urls', namespace='dictionary')),
)


def handler403(request):
    if request.user.is_authenticated():
        return render(request, 'errors/403.html')
    return redirect_to_login(request.path)