from django.conf.urls import patterns, include, url
from apps.homepage.feeds import ArchiveFeed
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from justread import settings
from sitemaps import justreadSitemap, SiteSitemap

admin.autodiscover()

sitemaps = {
    'justread': justreadSitemap,
    'pages': SiteSitemap(['homepage_contact', 'homepage_archive'])
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'justread.views.home', name='home'),
    # url(r'^justread/', include('justread.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', include('apps.homepage.urls')),
    (r'^', include('apps.accounts.urls')),
    url(r'^sitemap.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #url(r'^login/$', login, kwargs = {'template_name': 'homepage/login.html'}, name='homepage_login'),
    #url(r'^logout/$', logout, name='homepage_logout'),
    #url(r'^about/$', 'apps.homepage.views.about', name='homepage_about'),
    url(r'^contact/$', 'apps.homepage.views.contact', name='homepage_contact'),
    #url(r'^profile/$', 'apps.homepage.views.profile', name='homepage_profile'),
    url(r'^archive/$', 'apps.homepage.views.archive', name='homepage_archive'),
    url(r'^feed/archive/$', ArchiveFeed()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^about/$', 'django.contrib.flatpages.views.flatpage', kwargs = {'url': '/about/'}, name = 'homepage_about'),
    (r'^feed/archive/$', ArchiveFeed()),
)