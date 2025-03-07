from django.db import models
from .url_data import UrlData
from .raw_data import RawData

class ScrapedData(models.Model):
    url_id = models.ForeignKey(UrlData, on_delete=models.CASCADE, related_name='scraped_data')
    raw_id = models.ForeignKey(RawData, on_delete=models.CASCADE, related_name='scraped_entries')
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    social_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scraped data for {self.url_id} - {self.name}"
