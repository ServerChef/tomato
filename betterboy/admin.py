from django.contrib import admin

from .models import WebSite, Plugin

admin.site.register(WebSite)
admin.site.register(Plugin)
