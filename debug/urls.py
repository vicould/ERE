# -*- coding:utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('ere.debug.views',
                       (r'^$', 'main_debug'),
                      )

