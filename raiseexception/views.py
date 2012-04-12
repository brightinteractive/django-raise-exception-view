# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com


class DeliberateException(Exception):
    """Exception that is deliberately raised to check that error logging is
    working."""

    def __init__(self, *args, **kwargs):
        super(DeliberateException, self).__init__(*args, **kwargs)

def raise_exception(request):
    """
    Always throws an exception - useful for checking that exception logging is
    working
    """
    raise DeliberateException()
