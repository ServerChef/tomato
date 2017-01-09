from django.db import models


class WebSite(models.Model):
    site_title = models.CharField(max_length=200)
    create_time = models.DateTimeField("Create Time")

    def __str__(self):
        return self.site_title


class Plugin(models.Model):
    site = models.ForeignKey(WebSite, on_delete=models.CASCADE)
    software_name = models.CharField(max_length=200)
    create_time = models.DateTimeField("Create Time")

    def __str__(self):
        return self.software_name
