from django.db import models

class UrlData(models.Model):
    SCRAPING_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    url = models.URLField(unique=True)
    pagination_enabled = models.BooleanField(default=False)
    scraping_status = models.CharField(
        max_length=20, 
        choices=SCRAPING_STATUS_CHOICES, 
        default='pending'
    )

    def __str__(self):
        return self.url
