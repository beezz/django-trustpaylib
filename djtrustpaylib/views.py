#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from django.views.generic import FormView

from .helpers import parse_referer
from .forms import TrustPayRequestForm


class TransactionView(FormView):
    form_class = TrustPayRequestForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(TransactionView, self).get_context_data(*args, **kwargs)

        uri_parts = parse_referer(self.request)
        if uri_parts is not None:
            scheme, host = uri_parts
            print scheme
            print host

        return ctx
