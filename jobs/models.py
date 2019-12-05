from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=1200, null=True, blank=True)
    seniority = models.CharField(max_length=120, null=True, blank=True)
    employment = models.CharField(max_length=120, null=True, blank=True)
    about_us = models.URLField(max_length=120, null=True, blank=True)
    role = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
