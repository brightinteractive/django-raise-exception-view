# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from __future__ import absolute_import

from .views import raise_exception

try:
    from django.conf.urls.defaults import patterns, url
    urlpatterns = patterns('raiseexception.views', url(r'^raise-exception$', 'raise_exception', name='raise-exception'),)

except ImportError:
    # django > 1.8
    from django.conf.urls import url
    urlpatterns = [url(r'^raise-exception$', raise_exception, name='raise-exception'),]


