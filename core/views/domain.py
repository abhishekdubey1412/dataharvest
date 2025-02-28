from urllib.parse import urlparse
from django.http import JsonResponse
from core.models.raw_data import get_raw_data
from core.models.domain_data import filter_domain
from core.models.website_scraping_status import filter_websites

def domain_data(request, id):
    """Returns domain data and scraping status in JSON format"""
    website_data = filter_websites(website_id=id).first()
    if not website_data:
        return JsonResponse({"error": "Website not found"}, status=404)

    url = website_data.url
    domain = urlparse(url).netloc.split("www.")[-1].lower()
    domain_data_list = filter_domain(domain=domain)

    data = []
    for domain_data in domain_data_list:
        try:
            website_status = filter_websites(website_id=domain_data["website_id"]).first()
        except Exception:
            website_status = None

        data.append({
            "domain": domain_data["domain"],
            "scraping_status": website_status.scraping_status if website_status else None,
            "title": domain_data["title"],
            "emails": domain_data["emails"],
            "phone_numbers": domain_data["phone_numbers"],
            "social_media_links": domain_data["social_media_links"],
            "mx_records": domain_data["mx_records"],
            "mail_status": domain_data["mail_status"],
            "mail_provider": domain_data["mail_provider"],
            "company_description": domain_data["company_description"],
            "created_at": domain_data["created_at"],
            "updated_at": domain_data["updated_at"],
        })

    return JsonResponse(data, safe=False)

def staff_data(request, id):
    """Returns RawData details in JSON format"""
    website_data = filter_websites(website_id=id)
    url = website_data.first().url
    raw_data_entries = get_raw_data(url=url)
    
    if not raw_data_entries.exists():
        return JsonResponse({"error": "No RawData found for this URL"}, status=404)
    
    data = [
            {
                "id": entry.id,
                "url": entry.url,
                "data": entry.data,
                "scraped_at": entry.scraped_at,
            }
            for entry in raw_data_entries
        ]
    return JsonResponse(data, safe=False)