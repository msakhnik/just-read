from django.conf.urls.defaults import *

urlpatterns = patterns('apps.data.views',
    url(r'^create/$', 'create', name = 'data_create'),
)
