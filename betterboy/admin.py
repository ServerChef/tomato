from django.contrib import admin

from .models import Site, Plugin

admin.site.register(Site)
admin.site.register(Plugin)
