import re
import dns.resolver
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from api.models.domain_data import DomainData as DomainDataModel

class DomainData:
    EXCLUDED_TAGS = {
        "header", "footer", "style", "noscript", "nav", "iframe", 
        "input", "svg", "aside", "button", "link", "meta", "picture", 
        "source", "object", "embed", "param", "canvas", "map", "area"
    }

    SOCIAL_MEDIA_DOMAINS = {
        "facebook.com", "twitter.com", "linkedin.com", "instagram.com",
        "youtube.com", "t.me", "whatsapp.com", "threads.net", "x.com"
    }

    EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    PHONE_REGEX = r"\+?\d{1,4}[\s-]?\(?\d{2,5}\)?[\s-]?\d{2,5}[\s-]?\d{2,5}"

    MAIL_PROVIDER_MAP = {
        "google.com": "Google (Gmail)", "l.google.com": "Google (Gmail)",
        "outlook.com": "Microsoft (Outlook)", "hotmail.com": "Microsoft (Outlook)",
        "yahoo.com": "Yahoo Mail", "zoho.com": "Zoho Mail",
        "icloud.com": "Apple iCloud Mail", "protonmail.com": "ProtonMail"
    }

    @staticmethod
    def get_mx_records(domain):
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            mx_records = [r.exchange.to_text().strip('.') for r in answers]
            
            if not mx_records:
                return [], "No MX Records Found", 0

            provider_name = "Unknown Provider"
            for record in mx_records:
                domain_parts = record.split(".")
                for i in range(len(domain_parts) - 1):
                    subdomain = ".".join(domain_parts[i:])
                    if subdomain in DomainData.MAIL_PROVIDER_MAP:
                        provider_name = DomainData.MAIL_PROVIDER_MAP[subdomain]
                        break
                if provider_name != "Unknown Provider":
                    break

            return mx_records, provider_name, 1
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return [], "No MX Records Found", 0
        except Exception:
            return [], "Error Retrieving MX Records", 0

    @staticmethod
    def extract_contact_data(soup):
        social_links, emails, phone_numbers = set(), set(), set()
        
        for tag in DomainData.EXCLUDED_TAGS:
            for element in soup.find_all(tag):
                for a in element.find_all("a", href=True):
                    href = a["href"].strip().lower()
                    if href.startswith("mailto:"):
                        emails.add(href.replace("mailto:", ""))
                    elif href.startswith(("tel:", "ph:")):
                        phone_numbers.add(href.replace("tel:", "").replace("ph:", ""))
                    elif any(domain in href for domain in DomainData.SOCIAL_MEDIA_DOMAINS):
                        social_links.add(href)
                
                text = element.get_text(" ", strip=True)
                emails.update(re.findall(DomainData.EMAIL_REGEX, text))
                phone_numbers.update(re.findall(DomainData.PHONE_REGEX, text))
        
        return social_links, emails, phone_numbers

    @staticmethod
    def get_domain_data(soup):
        title = soup.title.string.strip() if soup.title else ""
        description = ""
        
        for meta in soup.find_all("meta"):
            if meta.get("name") == "description" or meta.get("property") in ["og:description", "twitter:description"]:
                if meta.get("content"):
                    description = meta["content"].strip()
                    break
        
        return title, description

    @staticmethod
    def extract_data(driver, url_id):
        """Extracts domain data and saves it using Django models."""
        domain = urlparse(driver.current_url).netloc.split("www.")[-1].lower()

        soup = BeautifulSoup(driver.page_source, "html.parser")
        title, description = DomainData.get_domain_data(soup)
        social_links, emails, phone_numbers = DomainData.extract_contact_data(soup)
        mx_records, mail_provider, mail_status = DomainData.get_mx_records(domain)

        # Save Domain Data using your Django API model
        domain_entry, created = DomainDataModel.objects.get_or_create(
            domain=domain,
            defaults={
                "url_id": url_id,  # Storing the URL ID
                "title": title,
                "emails": list(emails),
                "phone_numbers": list(phone_numbers),
                "social_media_links": list(social_links),
                "mx_records": mx_records,
                "mail_status": mail_status,
                "mail_provider": mail_provider,
                "description": description,
            },
        )

        if created:
            print(f"Domain data for {domain} successfully saved with URL ID {url_id}.")
        else:
            print(f"Domain data for {domain} already exists and was not updated.")
