# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('raiseexception.views',
    url(r'^raise-exception$', 'raise_exception', name='raise-exception'),
)
