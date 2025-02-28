# Main and Table Data Collection
# def get_cleaned_content(soup):
#     body = soup.find("body")
#     soup = BeautifulSoup(str(body), 'html.parser')

#     tags_to_remove = [
#         "header", "footer", "script", "style", "noscript", "nav", "iframe", 
#         "input", "svg", "aside", "button", "link", "meta", "picture", 
#         "source", "object", "embed", "param", "canvas", "map", "area"
#     ]

#     for tags in tags_to_remove:
#         for tag in soup.find_all(tags):
#             tag.decompose()
    
#     for pagination in soup.find_all(class_=lambda x: x is not None and isinstance(x, str) and "pagination" in x.lower()):
#         pagination.decompose()

#     for tag in soup.find_all(True):
#         if tag.text == "" or tag.text ==  None:
#             tag.decompose()
    
#     for tag in soup.find_all(True):
#         for attribute in ['onload', 'onclick']:
#             del tag[attribute]

#     return soup

# def extract_tables_from_soup(soup):
#     tables = soup.find_all("table")
#     all_table_data = {}

#     for index, table in enumerate(tables):
#         rows = []
#         headers = []

#         header_row = table.find("tr")
#         if header_row:
#             headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]

#         for row in table.find_all("tr")[1:]:
#             cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
#             if cols:
#                 rows.append(cols)

#         table_dicts = []
#         if headers and rows:
#             for row in rows:
#                 if len(row) == len(headers):
#                     table_dicts.append(dict(zip(headers, row)))
#             all_table_data[f"table_{index+1}"] = table_dicts
#         else:
#             all_table_data[f"table_{index+1}"] = rows
        
#         table.decompose()
    
#     return all_table_data, soup

# def get_all_table_data(driver):
#     all_data = {}

#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     all_table_data, main_soup = extract_tables_from_soup(soup)
#     all_data.update(all_table_data)

#     iframes = driver.find_elements(By.TAG_NAME, "iframe")
#     for index, iframe in enumerate(iframes):
#         driver.switch_to.frame(iframe)
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         iframe_table_data, iframe_soup = extract_tables_from_soup(soup)
#         all_data.update({f"iframe_{index+1}": iframe_table_data})

#         iframe_soup = get_cleaned_content(iframe_soup)

#         body_tag = iframe_soup.find('body')
#         if body_tag:
#             for child in body_tag.find_all(recursive=False):
#                 style = child.get('style', '')
#                 if 'display: none' in style or 'visibility: hidden' in style:
#                     child.decompose()
            
#             body_text = body_tag.get_text(strip=True)
#             if body_text:
#                 all_data[f'iframe_{index+1}_body_content'] = body_text

#         driver.switch_to.default_content()

#     main_soup = get_cleaned_content(main_soup)
#     if main_soup.text.strip():
#         body_tag = main_soup.find('body')
#         if body_tag:
#             for child in body_tag.find_all(recursive=False):
#                 style = child.get('style', '')
#                 if 'display: none' in style or 'visibility: hidden' in style:
#                     child.decompose()

#             main_body_text = body_tag.get_text(strip=True)
#             if main_body_text:
#                 all_data['main_body_content'] = main_body_text

#     all_data = {k: v for k, v in all_data.items() if v}

#     return all_data

import re
import dns.resolver
from bs4 import BeautifulSoup
from urllib.parse import urlparse

EXCLUDED_TAGS = {
    "header", "footer", "script", "style", "noscript", "nav", "iframe", 
    "input", "svg", "aside", "button", "link", "meta", "picture", 
    "source", "object", "embed", "param", "canvas", "map", "area"
}

SOCIAL_MEDIA_DOMAINS = {
    "facebook.com", "twitter.com", "linkedin.com", "instagram.com",
    "youtube.com", "t.me", "whatsapp.com", "threads.net", "x.com"
}

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
PHONE_REGEX = r"\+?\d{1,4}[\s-]?\(?\d{2,5}\)?[\s-]?\d{2,5}[\s-]?\d{2,5}"

def get_mx_records(domain):
    mail_provider_map = {
        "google.com": "Google (Gmail)", "l.google.com": "Google (Gmail)", "outlook.com": "Microsoft (Outlook)",
        "hotmail.com": "Microsoft (Outlook)", "yahoo.com": "Yahoo Mail", "zoho.com": "Zoho Mail",
        "icloud.com": "Apple iCloud Mail", "protonmail.com": "ProtonMail"
    }

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
                if subdomain in mail_provider_map:
                    provider_name = mail_provider_map[subdomain]
                    break
            if provider_name != "Unknown Provider":
                break

        return mx_records, provider_name, 1
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return [], "No MX Records Found", 0
    except Exception:
        return [], "Error Retrieving MX Records", 0

def get_cleaned_soup(soup):
    """Removes EXCLUDED_TAGS from soup and returns cleaned soup."""
    for tag in EXCLUDED_TAGS:
        for element in soup.find_all(tag):
            element.decompose()
    return soup

def extract_contact_data(soup):
    """Extracts contact links, social links, emails, and phone numbers from EXCLUDED_TAGS, then removes those elements."""
    contact_links = set()
    social_links = set()
    emails = set()
    phone_numbers = set()

    # Extract data from excluded elements
    for tag in EXCLUDED_TAGS:
        for element in soup.find_all(tag):
            # Extract links
            for a in element.find_all("a", href=True):
                href = a["href"].strip().lower()
                
                if href.startswith(("mailto:", "tel:", "ph:")):
                    contact_links.add(href)
                
                elif any(domain in href for domain in SOCIAL_MEDIA_DOMAINS):
                    social_links.add(href)

            # Extract emails and phone numbers from text inside excluded tags
            text = element.get_text(" ", strip=True)
            emails.update(re.findall(EMAIL_REGEX, text))
            phone_numbers.update(re.findall(PHONE_REGEX, text))

    soup = get_cleaned_soup(soup)
    return soup, contact_links, social_links, emails, phone_numbers

def get_domain_data(soup):
    """Extracts the title and meta description from the given BeautifulSoup object."""
    title = soup.title.string.strip() if soup.title else ""

    description = ""
    meta_tags = soup.find_all("meta")  # Get all meta tags for debugging

    for meta in meta_tags:
        if meta.get("name") == "description" or meta.get("property") in ["og:description", "twitter:description"]:
            if meta.get("content"):
                description = meta["content"].strip()
                break  # Stop after finding the first valid description

    return title, description

def extract_data(driver):
    """Extracts all contact information from a webpage."""
    soup = BeautifulSoup(driver.page_source, "html.parser")
    title, description = get_domain_data(soup)
    cleaned_soup, contact_links, social_links, emails, phone_numbers = extract_contact_data(soup)
    mx_records, mail_provider, mail_status = get_mx_records(urlparse(driver.current_url).netloc.split("www.")[-1].lower())

    return {
        "Domain": urlparse(driver.current_url).netloc.split("www.")[-1],
        "MX Records": mx_records,
        "Mail Provider": mail_provider,
        "Mail Status": mail_status,
        "title": title,
        "description": description,
        "contact_links": contact_links,
        "social_links": social_links,
        "emails": emails,
        "phone_numbers": phone_numbers
    }