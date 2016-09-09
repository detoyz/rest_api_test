from django.conf.urls import patterns, include, url
from rest_api.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rest_api_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', rest_api)
    # url(r'^admin/', include(admin.site.urls)),
)
