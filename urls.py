# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # For the comments
    (r'^comments/', include('django.contrib.comments.urls')),

    # the blog
    (r'^', include('ere.blog.urls')),

    # debug app
    (r'^debug', include('ere.debug.urls')),
    # authentication
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

# used to serve static content when using the development server
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
            url(r'^~ere/site_media/(?P<path>.*)$', 'serve',
                {'document_root': settings.MEDIA_ROOT}),
    )

