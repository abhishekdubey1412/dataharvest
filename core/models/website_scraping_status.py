from django.db import models, IntegrityError

class WebsiteScrapingStatus(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    url = models.URLField(unique=True)
    pagination_enabled = models.BooleanField(default=False)
    scraping_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending"
    )

    def __str__(self):
        return f"{self.url} - {self.get_scraping_status_display()}"

def create_website(url, pagination_enabled=False, scraping_status="pending"):
    try:
        return WebsiteScrapingStatus.objects.create(
            url=url,
            pagination_enabled=pagination_enabled,
            scraping_status=scraping_status
        )
    except IntegrityError:
        return "Website with this URL already exists."

def edit_website(url, pagination_enabled=None, scraping_status=None):
    try:
        website = WebsiteScrapingStatus.objects.get(url=url)
        if pagination_enabled is not None:
            website.pagination_enabled = pagination_enabled
        if scraping_status is not None:
            website.scraping_status = scraping_status
        website.save()
        return website
    except WebsiteScrapingStatus.DoesNotExist:
        return "Website not found."

def delete_website(url):
    try:
        website = WebsiteScrapingStatus.objects.get(url=url)
        website.delete()
        return "Website deleted successfully."
    except WebsiteScrapingStatus.DoesNotExist:
        return "Website not found."

def filter_websites(scraping_status=None, pagination_enabled=None, url=None, website_id=None):
    filters = {}

    if scraping_status is not None:
        filters["scraping_status"] = scraping_status

    if pagination_enabled is not None:
        filters["pagination_enabled"] = pagination_enabled

    if url is not None:
        filters["url"] = url

    if website_id is not None:
        filters["id"] = website_id

    return (
        WebsiteScrapingStatus.objects.order_by('id') 
        if not filters 
        else WebsiteScrapingStatus.objects.filter(**filters).order_by('id')
    )

def get_pending_urls():
    """Return a list of URLs that have status 'pending'."""
    return list(WebsiteScrapingStatus.objects.filter(scraping_status="pending").values_list("url", flat=True))