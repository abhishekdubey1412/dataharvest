# import time
# import json
# import requests
# from collections import Counter
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# # People-related keywords for filtering
# PEOPLE_KEYWORDS = [
#     'team', 'teams', 'leadership', 'staff', 'employee', 'employees',
#     'people', 'personnel', 'member', 'members', 'group', 'crew',
#     'management', 'director', 'executive', 'contact', 'leaders'
# ]

# # Initialize Chrome WebDriver
# def init_driver():
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     return driver

# # 🔍 **Search Google for a URL using Selenium**
# def search_google_for_url(query):
#     print(f"Searching Google for: {query}....")
#     driver = init_driver()
#     driver.get("https://www.google.com/")
    
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)
    
#     time.sleep(3)  # Allow time for results to load
    
#     try:
#         results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc a")
#         if results:
#             first_result_url = results[0].get_attribute("href")
#             print(f"Found URL: {first_result_url}")
#             driver.quit()
#             return first_result_url
#         else:
#             print("No results found.")
#     except Exception as e:
#         print(f"Error fetching search results: {e}")
    
#     driver.quit()
#     return None

# # 🌍 **Get Full Page Source Code (View Source)**
# def get_page_source(url):
#     print(f"Fetching full source code from: {url}....")
#     try:
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
#         }
#         response = requests.get(url, headers=headers, timeout=10)
#         if response.status_code != 200:
#             print(f"Failed to access webpage. HTTP {response.status_code}")
#             return None
#         return response.text
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {str(e)}")
#         return None

# # 🔍 **Analyze Primary Pages for Repeated Classes and Return JSON**
# def analyze_primary_pages(primary_pages):
#     result_json = {}
    
#     for page_url in primary_pages:
#         print(f"\nAnalyzing primary page: {page_url}")
#         html = get_page_source(page_url)
#         if html:
#             soup = BeautifulSoup(html, 'html.parser')
#             elements_with_class = soup.find_all(class_=True)
            
#             # Count class occurrences
#             class_counter = Counter()
#             for element in elements_with_class:
#                 classes = element.get('class')
#                 class_counter.update(classes)
            
#             # Find classes that appear more than twice
#             repeated_classes = {cls: count for cls, count in class_counter.items() if count > 2}
            
#             if repeated_classes:
#                 page_data = {}
#                 for cls in repeated_classes:
#                     elements = soup.find_all(class_=cls)
#                     text_content = [element.get_text(strip=True) for element in elements if element.get_text(strip=True)]
#                     page_data[cls] = text_content
                
#                 result_json[page_url] = page_data
#             else:
#                 result_json[page_url] = {"message": "No classes found appearing more than twice"}
    
#     return result_json

# # 🔗 **Extract and Filter Links from Source Code**
# def extract_and_filter_links_from_html(html, base_url):
#     print("Extracting and filtering links from the page source....")
#     soup = BeautifulSoup(html, "html.parser")
#     links = [a["href"] for a in soup.find_all("a", href=True)]
#     all_links = [requests.compat.urljoin(base_url, link) for link in links]
    
#     filtered_links = [
#         link for link in all_links 
#         if any(keyword in link.lower() for keyword in PEOPLE_KEYWORDS)
#     ]
    
#     primary_pages = []
#     nested_pages = []
    
#     for link in filtered_links:
#         path_parts = link.rstrip('/').split('/')
#         last_segments = '/'.join(path_parts[-2:]).lower()
        
#         if any(keyword == path_parts[-1].lower() for keyword in PEOPLE_KEYWORDS):
#             primary_pages.append(link)
#         elif any(keyword in last_segments for keyword in PEOPLE_KEYWORDS):
#             nested_pages.append(link)
    
#     print(f"\n🔹 Total Links Found: {len(all_links)}")
#     print(f"🔹 Total People-related Links: {len(filtered_links)}")
#     print(f"🔹 Primary Pages (direct keyword matches): {len(primary_pages)}")
#     print(f"🔹 Nested Pages (sub-pages): {len(nested_pages)}")
    
#     if all_links:
#         print("\n📋 All Extracted Links:")
#         for link in all_links:
#             print(link)
    
#     if primary_pages:
#         print("\n✅ Primary People-related Pages:")
#         for link in primary_pages:
#             print(link)
    
#     if nested_pages:
#         print("\n🔍 Nested People-related Pages:")
#         for link in nested_pages:
#             print(link)
    
#     if not (primary_pages or nested_pages):
#         print("\nNo people-related links found in the page source.")
    
#     return all_links, filtered_links, primary_pages, nested_pages

# # 🤖 **AI Agent for Extracting and Analyzing**
# def link_extractor_agent(query):
#     url = search_google_for_url(query)
    
#     if url:
#         source_code = get_page_source(url)
#         if source_code:
#             all_links, filtered_links, primary_pages, nested_pages = extract_and_filter_links_from_html(source_code, url)
#             if filtered_links:
#                 print("\n✅ Link Extraction Complete!")
#                 if primary_pages:
#                     class_data = analyze_primary_pages(primary_pages)
#                     print("\n✅ Primary Page Analysis Complete!")
#                     print("\nJSON Output:")
#                     print(json.dumps(class_data, indent=2))
#                 else:
#                     print("\nNo primary pages to analyze.")
#             else:
#                 print("\nNo people-related links found in the page source.")
#         else:
#             print("No source code extracted from the page.")
#     else:
#         print("Could not find a relevant webpage.")

# # 📌 **Main Execution**
# if __name__ == "__main__":
#     search_query = input("Enter your search query: ").strip()
#     link_extractor_agent(search_query)
