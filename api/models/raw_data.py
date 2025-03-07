from django.db import models
from .url_data import UrlData

class RawData(models.Model):
    url_id = models.ForeignKey(UrlData, on_delete=models.CASCADE, related_name='raw_data')
    tables_data = models.JSONField(null=True, blank=True)
    raw_data = models.TextField(null=True, blank=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Raw data for {self.url_id}"

