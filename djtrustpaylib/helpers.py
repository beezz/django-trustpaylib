# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Helping functions for djtrustpaylib.
"""

from urlparse import urlparse


def parse_referer(request):
    """
    Returns extracted (scheme, host) tuple from REFERER
    header or None.
    """
    if 'HTTP_REFERER' in request.META:
        return urlparse(request.META['HTTP_REFERER'])[:2]
    else:
        return None
