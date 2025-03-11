import requests
import time
import threading
from django.utils.timezone import now
from api.models.groq_api_request import APIRequestLog

def call_api(url, max_rpd=1000, max_rpm=30, max_tpm=6000):
    interval = 86400 / max_rpd
    used_tokens = 0
    
    for i in range(max_rpd):
        response = requests.get(url)
        request_time = now()
        
        if response.status_code == 200:
            tokens_remaining = int(response.headers.get("x-ratelimit-remaining-tokens", max_tpm))
            tokens_used = max_tpm - tokens_remaining
            used_tokens += tokens_used
            
            # Store request log in database
            APIRequestLog.objects.create(
                request_time=request_time,
                status_code=200,
                tokens_used=tokens_used,
                response_time=response.elapsed.total_seconds()
            )
            print(f"Request {i+1}: Success (200), Tokens Used: {tokens_used}")
            
            # If TPM is exceeded, wait until reset
            if used_tokens >= max_tpm:
                reset_time = int(response.headers.get("x-ratelimit-reset-tokens", 60))
                print(f"Token limit reached. Waiting {reset_time} seconds...")
                time.sleep(reset_time)
                used_tokens = 0
        elif response.status_code == 429:
            retry_after = int(response.headers.get("retry-after", 5))
            print(f"Request {i+1}: Rate limited. Retrying after {retry_after} seconds.")
            time.sleep(retry_after)
            continue
        else:
            print(f"Request {i+1}: Failed ({response.status_code})")
        
        time.sleep(interval)

def start_api_thread(url):
    thread = threading.Thread(target=call_api, args=(url,))
    thread.daemon = True
    thread.start()
    print("API thread started, running in the background...")

# Example usage
api_url = "https://api.example.com/data"
start_api_thread(api_url)