from django.db import models
from .url_data import UrlData

class DomainData(models.Model):
    url_id = models.ForeignKey(UrlData, on_delete=models.CASCADE, related_name='domains')
    domain = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    emails = models.JSONField(default=list)
    phone_numbers = models.JSONField(default=list)
    social_media_links = models.JSONField(default=list)
    mail_status = models.CharField(max_length=50, blank=True, null=True)
    mx_records = models.JSONField(default=list, blank=True)
    mail_provider = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain
