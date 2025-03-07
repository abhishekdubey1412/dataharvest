from django.contrib import admin
from django.contrib.auth.models import Group
from api.models.url_data import UrlData
from api.models.domain_data import DomainData
from api.models.raw_data import RawData
from api.models.scraped_data import ScrapedData

admin.site.unregister(Group)

@admin.register(UrlData)
class UrlDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'pagination_enabled', 'scraping_status')
    search_fields = ('url',)
    list_filter = ('scraping_status',)

@admin.register(DomainData)
class DomainDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_id', 'domain', 'title', 'mail_provider', 'created_at')
    search_fields = ('domain', 'title', 'mail_provider')
    list_filter = ('mail_provider', 'created_at')

@admin.register(RawData)
class RawDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_id', 'scraped_at')
    search_fields = ('url_id__url',)
    list_filter = ('scraped_at',)

@admin.register(ScrapedData)
class ScrapedDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_id', 'raw_id', 'name', 'email', 'phone', 'designation', 'created_at')
    search_fields = ('name', 'email', 'phone', 'designation')
    list_filter = ('created_at',)
