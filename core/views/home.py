import threading
import pandas as pd
from urllib.parse import urlparse
from django.contrib import messages
from scraper.main import run_scraping
from django.shortcuts import render, redirect
from core.models.website_scraping_status import (
    create_website, edit_website, filter_websites, get_pending_urls
)
from core.models.domain_data import filter_domain, is_domain_scraped

RESTRICTED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}
scraping_lock = threading.Lock()

def is_valid_url(url):
    """Check if a URL has a restricted file extension."""
    return not any(url.lower().endswith(ext) for ext in RESTRICTED_EXTENSIONS)

def scrape_url(url):
    """Run scraping in a separate thread and update status."""
    with scraping_lock:
        try:
            domain = urlparse(url).netloc.split("www.")[-1].lower()
            if is_domain_scraped(domain):
                print(f"Skipping {url}, already scraped.")
                edit_website(url, scraping_status="completed")
                process_next_url()
                return

            website_id = edit_website(url, scraping_status="in_progress")
            run_scraping(url, website_id.id, headless=True,)
            edit_website(url, scraping_status="completed")

        except Exception as e:
            print(e)
            edit_website(url, scraping_status="failed")
        
        process_next_url()

def process_next_url():
    """Fetch the next pending URL and start processing."""
    pending_urls = get_pending_urls()
    if pending_urls:
        next_url = pending_urls[0]
        threading.Thread(target=scrape_url, args=(next_url,)).start()
    else:
        print("All URLs processed. No pending URLs left.")

def home_view(request):
    """Handles website scraping requests and file uploads."""
    if request.method == "POST":
        website_url = request.POST.get("url")
        pagination_enabled = request.POST.get("pagination") == "on"
        uploaded_file = request.FILES.get("excel_file")
        urls_to_process = []

        # Process a single URL input
        if website_url:
            if not is_valid_url(website_url.strip()):
                messages.error(request, "Invalid URL! URLs ending with restricted file extensions are not allowed.")
                return redirect("home")

            website_status = create_website(url=website_url.strip(), pagination_enabled=True if pagination_enabled else False, scraping_status="pending")

            if isinstance(website_status, str):
                messages.info(request, f"{website_url} already exists.")

            urls_to_process.append(website_url.strip())

        # Process uploaded file URLs
        elif uploaded_file:
            if not uploaded_file.name.endswith((".xls", ".xlsx")):
                messages.error(request, "Invalid file type! Please upload an Excel file (.xls, .xlsx).")
                return redirect("home")

            try:
                df = pd.read_excel(uploaded_file)

                if "urls" not in df.columns:
                    messages.error(request, "Invalid file format! Column 'urls' not found.")
                    return redirect("home")

                urls = df["urls"].dropna().unique()
                added_count = 0

                for url in urls:
                    url = url.strip()
                    if is_valid_url(url):
                        website_status = create_website(url=url, pagination_enabled=True if pagination_enabled else False, scraping_status="pending")

                        if not isinstance(website_status, str):
                            added_count += 1
                            urls_to_process.append(url)

                messages.success(request, f"{added_count} valid URLs uploaded successfully!")

            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
                return redirect("home")

        # Start processing only if new URLs were added
        if urls_to_process:
            process_next_url()

        return redirect("home")

    websites_data = filter_websites()
    domain_data = filter_domain()

    return render(request, "index.html", {"websites_data": websites_data, "domain_data": domain_data})