from django.db import models


class Site(models.Model):
    site_title = models.CharField(max_length=200)
    create_time = models.DateTimeField("Create Time")


class Plugin(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    software_name = models.CharField(max_length=200)
    create_time = models.DateTimeField("Create Time")
