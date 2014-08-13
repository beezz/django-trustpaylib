# -*- coding: utf-8 -*-
# vim:fenc=utf-8


from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _

import trustpaylib



class TrustPayRequestForm(forms.Form):

    amount = forms.DecimalField(
        min_value=0.1,
        max_digits=8,
        decimal_places=2)

    language = forms.ChoiceField(
        choices=[(c, c) for c in trustpaylib.LANGUAGES],
    )

    country = forms.ChoiceField(
        choices=[c for c in zip(
            trustpaylib.COUNTRIES,
            trustpaylib.COUNTRIES_VERBOSE)],
    )

    currency = forms.ChoiceField(
        choices=[(c, c) for c in trustpaylib.CURRENCIES],
    )


