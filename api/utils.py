import threading
from scraper.main import run_scraping
from api.models.url_data import UrlData

RESTRICTED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}

scraping_lock = threading.Lock()

def is_valid_url(url):
    """Check if a URL has a restricted file extension."""
    return not any(url.lower().endswith(ext) for ext in RESTRICTED_EXTENSIONS)

def process_next_url():
    """Fetch the next pending URL and start processing."""
    pending_urls = UrlData.objects.filter(scraping_status="pending")
    if pending_urls:
        next_url = pending_urls[0]
        threading.Thread(target=scrape_url, args=(next_url.url,)).start()
    else:
        print("All URLs processed. No pending URLs left.")

def scrape_url(url):
    """Run scraping in a separate thread and update status."""
    with scraping_lock:
        try:
            if is_domain_scraped(url):
                print(f"Skipping {url}, already scraped.")
                update_website_status(url, "completed")
                process_next_url()
                return

            website = update_website_status(url, "in_progress")
            run_scraping(url, website, headless=True)
            update_website_status(url, "completed")

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            update_website_status(url, "failed")

        process_next_url()

def update_website_status(url, status):
    """Update scraping status of the website."""
    website = UrlData.objects.filter(url=url).first()
    if website:
        website.scraping_status = status
        website.save()
    return website

def is_domain_scraped(url):
    """Check if a domain has already been scraped."""
    return UrlData.objects.filter(url__icontains=url, scraping_status="completed").exists()