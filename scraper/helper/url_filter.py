import requests

def remove_duplicates(urls):
    """Remove duplicate URLs while maintaining order."""
    return list(dict.fromkeys(urls))

def filter_urls(urls):
    """Remove duplicates and filter out URLs with unwanted extensions."""
    excluded_extensions = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}

    return [
        url for url in remove_duplicates(urls) 
        if not any(url.lower().endswith(ext) for ext in excluded_extensions)
    ]

def is_url_reachable(url):
    """Check if the URL is reachable (HTTP 200)."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False