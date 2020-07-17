# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com


__version__ = '1.0.2'


class DeliberateException(Exception):
    """Exception that is deliberately raised to check that error logging is
    working."""

    def __init__(self, *args, **kwargs):
        super(DeliberateException, self).__init__(*args, **kwargs)
