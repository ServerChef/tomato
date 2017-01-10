from django import forms
from betterboy.models import *

__all__ = ['WebSiteForm']


class WebSiteForm(forms.Form):
    site_title = forms.CharField(label="Website name", max_length=200)

    def to_model(self):
        return WebSite(**self.data)
