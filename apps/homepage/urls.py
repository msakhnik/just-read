from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.homepage.views',
    url(r'^$', 'index', name='homepage_index'),
)