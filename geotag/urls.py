from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geotag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^geoGrading/', include('geoGrading.urls', namespace='geoGrading')),
    url(r'^admin/', include(admin.site.urls)),
)
