from django.contrib import admin
from .models import WebsiteScrapingStatus, DomainData, RawData

@admin.register(WebsiteScrapingStatus)
class WebsiteScrapingStatusAdmin(admin.ModelAdmin):
    list_display = ("url", "pagination_enabled", "scraping_status")
    list_filter = ("pagination_enabled", "scraping_status")
    search_fields = ("url",)

@admin.register(DomainData)
class DomainDataAdmin(admin.ModelAdmin):
    list_display = ("domain", "title", "mail_status", "mail_provider", "created_at", "updated_at")
    search_fields = ("domain", "title", "mail_provider")
    list_filter = ("mail_status", "mail_provider")

@admin.register(RawData)
class RawDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'scraped_at')  # Fields to display in the list view
    search_fields = ('url', 'data')  # Enables search by URL and data
    list_filter = ('scraped_at',)  # Allows filtering by scrape date
    ordering = ('-scraped_at',)  # Orders by newest first