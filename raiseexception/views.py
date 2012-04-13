# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

from raiseexception import DeliberateException


def raise_exception(request):
    """
    Always throws an exception - useful for checking that exception logging is
    working
    """
    raise DeliberateException()
