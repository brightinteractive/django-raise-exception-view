# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from __future__ import absolute_import

from django.test import TestCase
from django.core.urlresolvers import reverse
from .views import raise_exception
from raiseexception import DeliberateException


class RaiseExceptionViewTests(TestCase):
    def test_view_raises_exception(self):
        self.assertRaises(
            DeliberateException,
            raise_exception,
            request=None)


class RaiseExceptionUrlTests(TestCase):
    def test_url_raises_exception(self):
        self.assertRaises(
            DeliberateException,
            self._call_raise_exception_view)

    def _call_raise_exception_view(self):
        self.client.get(reverse('raise-exception'))
