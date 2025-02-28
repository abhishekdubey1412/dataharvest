from django.db import models, IntegrityError
from .website_scraping_status import WebsiteScrapingStatus

class DomainData(models.Model):
    domain = models.CharField(max_length=255, unique=True)
    website_id = models.ForeignKey(WebsiteScrapingStatus, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255, blank=True, null=True)
    mx_records = models.JSONField(default=list, blank=True)
    mail_status = models.CharField(max_length=50, blank=True, null=True)
    mail_provider = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.domain

class DomainEmail(models.Model):
    domain_data = models.ForeignKey(DomainData, on_delete=models.CASCADE, related_name="emails")
    email = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class DomainNumber(models.Model):
    domain_data = models.ForeignKey(DomainData, on_delete=models.CASCADE, related_name="phone_numbers")
    phone_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number
    
class DomainSocialLink(models.Model):
    domain_data = models.ForeignKey(DomainData, on_delete=models.CASCADE, related_name="social_links")
    social_media_link = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.social_media_link

def create_domain_data(domain, website_id, title=None, emails=None, phone_numbers=None, 
                       social_media_links=None, mx_records=None, mail_status=None, 
                       mail_provider=None, company_description=None):
    try:
        website_instance = WebsiteScrapingStatus.objects.get(id=website_id)
        domain_instance = DomainData.objects.create(
            domain=domain,
            website_id=website_instance,
            title=title or "",
            mail_status=mail_status,
            mail_provider=mail_provider,
            company_description=company_description
        )

        # Add related emails
        if emails:
            DomainEmail.objects.bulk_create([
                DomainEmail(domain_data=domain_instance, email=email)
                for email in set(emails)
            ])

        # Add related phone numbers
        if phone_numbers:
            DomainNumber.objects.bulk_create([
                DomainNumber(domain_data=domain_instance, phone_number=number)
                for number in set(phone_numbers)
            ])

        # Add related social media links
        if social_media_links:
            DomainSocialLink.objects.bulk_create([
                DomainSocialLink(domain_data=domain_instance, social_media_link=link)
                for link in set(social_media_links)
            ])

        return domain_instance

    except WebsiteScrapingStatus.DoesNotExist:
        return "WebsiteScrapingStatus not found."
    except IntegrityError:
        return "Domain already exists."

def edit_domain_data(domain, website_scraping_status=None, emails=None, phone_numbers=None, 
                      social_media_links=None, **kwargs):
    try:
        domain_instance = DomainData.objects.get(domain=domain)

        if website_scraping_status:
            if isinstance(website_scraping_status, WebsiteScrapingStatus):
                domain_instance.website_id = website_scraping_status
            else:
                domain_instance.website_id = WebsiteScrapingStatus.objects.get(id=website_scraping_status)

        for key, value in kwargs.items():
            setattr(domain_instance, key, value)

        domain_instance.save()

        # Update emails
        if emails is not None:
            DomainEmail.objects.filter(domain_data=domain_instance).delete()
            DomainEmail.objects.bulk_create([
                DomainEmail(domain_data=domain_instance, email=email)
                for email in set(emails)
            ])

        # Update phone numbers
        if phone_numbers is not None:
            DomainNumber.objects.filter(domain_data=domain_instance).delete()
            DomainNumber.objects.bulk_create([
                DomainNumber(domain_data=domain_instance, phone_number=number)
                for number in set(phone_numbers)
            ])

        # Update social media links
        if social_media_links is not None:
            DomainSocialLink.objects.filter(domain_data=domain_instance).delete()
            DomainSocialLink.objects.bulk_create([
                DomainSocialLink(domain_data=domain_instance, social_media_link=link)
                for link in set(social_media_links)
            ])

        return domain_instance

    except DomainData.DoesNotExist:
        return "Domain not found."
    except WebsiteScrapingStatus.DoesNotExist:
        return "WebsiteScrapingStatus not found."

def delete_domain_data(domain=None, domain_id=None):
    try:
        if domain:
            domain_instance = DomainData.objects.get(domain=domain)
        elif domain_id:
            domain_instance = DomainData.objects.get(id=domain_id)
        else:
            return "Either domain or domain_id must be provided."

        domain_instance.delete()
        return "Domain deleted successfully."
    except DomainData.DoesNotExist:
        return "Domain not found."

def filter_domain(domain=None, domain_id=None, website_scraping_status=None, **kwargs):
    filters = {}

    if domain:
        filters["domain"] = domain

    if domain_id:
        filters["id"] = domain_id

    if website_scraping_status:
        if isinstance(website_scraping_status, WebsiteScrapingStatus):
            filters["website_id"] = website_scraping_status.id
        else:
            filters["website_id"] = website_scraping_status

    filters.update(kwargs)

    domain_data_queryset = DomainData.objects.filter(**filters) if filters else DomainData.objects.all()

    domain_data_with_relations = []
    for domain_data in domain_data_queryset:
        domain_emails = list(domain_data.emails.values_list("email", flat=True))
        domain_numbers = list(domain_data.phone_numbers.values_list("phone_number", flat=True))
        domain_social_links = list(domain_data.social_links.values_list("social_media_link", flat=True))

        domain_data_with_relations.append({
            "id": domain_data.id,
            "domain": domain_data.domain,
            "website_id": domain_data.website_id.id if domain_data.website_id else None,
            "title": domain_data.title,
            "company_description": domain_data.company_description,
            "mx_records": domain_data.mx_records,
            "mail_status": domain_data.mail_status,
            "mail_provider": domain_data.mail_provider,
            "created_at": domain_data.created_at,
            "updated_at": domain_data.updated_at,
            "emails": domain_emails,
            "phone_numbers": domain_numbers,
            "social_media_links": domain_social_links,
        })

    return domain_data_with_relations

def is_domain_scraped(domain):
    """Returns True if the domain is already scraped and exists in the database."""
    return DomainData.objects.filter(domain=domain).exists()