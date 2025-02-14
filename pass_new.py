import os
import time
import json
import random
import dns.resolver
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.1770.50"
]

def human_typing(element, text, min_delay=0.05, max_delay=0.15):
    """Simulates human-like typing"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))

def human_mouse_movement(driver, element):
    """Moves the mouse to an element like a real user"""
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(random.uniform(0.5, 1.5))

def initialize_driver():
    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents)}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # Use the same version as your Chrome
    driver = uc.Chrome(options=options, headless=False, version_main=133)

    time.sleep(random.uniform(1, 3))  # Random delay for human-like behavior

    # Advanced fingerprint evasion
    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
        Object.defineProperty(navigator, 'vendor', {get: () => 'Google Inc.'});
        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
    """)

    return driver

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
            return [], "Null", 0

        provider_name = "Unknown Provider"
        for record in mx_records:
            domain_parts = record.split(".")[-3:]
            provider_name = mail_provider_map.get(".".join(domain_parts), mail_provider_map.get(".".join(domain_parts[-2:]), "Unknown Provider"))
            if provider_name != "Unknown Provider":
                break

        return mx_records, provider_name, 1
    except Exception:
        return [], "Null", 0

def get_description(driver):
    try:
        description = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")
        return description
    except:
        description = "No description found"
        return description

def find_linkedin_on_website(driver):
    try:
        linkedin_link = driver.find_element(By.XPATH, "//a[contains(@href, 'linkedin.com/company/')]").get_attribute("href")
        return linkedin_link
    except:
        return "LinkedIn profile not found"

def find_relevant_pages(driver):
    relevant_keywords = [
        "about", "team", "leadership", "people", "profile", "staff", "contact", "history", "culture",
        "executives", "board", "directory", "organization", "members", "employees", "leaders"
    ]
    
    excluded_extensions = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}
    
    relevant_links = set()
    
    try:
        current_domain = urlparse(driver.current_url).netloc
        anchor_tags = driver.find_elements(By.TAG_NAME, 'a')
        
        for anchor in anchor_tags:
            href = anchor.get_attribute("href")
            if not href:
                continue
            
            parsed_href = urlparse(href)
            anchor_url = parsed_href.netloc

            if anchor_url and anchor_url != current_domain:
                continue  # Ignore external links
            
            if 'login' in href.lower():
                continue  # Skip login pages
            
            if any(keyword.lower() in href.lower() for keyword in relevant_keywords):
                file_extension = parsed_href.path.split('.')[-1].lower()
                
                if file_extension and f".{file_extension}" in excluded_extensions:
                    continue  # Ignore non-HTML resources
                
                normalized_url = href.split('#')[0]
                relevant_links.add(normalized_url)
        
        return list(relevant_links)
    
    except Exception as e:
        return list(relevant_links)

def accept_cookies(driver):
    try:
        cookie_or_no_thanks_button = WebDriverWait(driver, 10).until(
            EC.any_of(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'accept all cookies')]")),
                EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'no thanks')]")),
                EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'i agree')]")),
                EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'allow all')]")),
                EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'i understand')]")),
            )
        )
        cookie_or_no_thanks_button.click()
    except:
        pass

def scroll_to_bottom(driver):
    scroll_step = 50
    delay = 0.02

    last_height = driver.execute_script(
        "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);"
    )

    while True:
        for _ in range(0, last_height, scroll_step):
            driver.execute_script(f"window.scrollBy(0, {scroll_step});")
            time.sleep(delay)
        
        time.sleep(1)
        new_height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);"
        )
        
        if new_height == last_height:
            break
        last_height = new_height

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def save_data(data, pagination_content=None):
    domain = data["Domain"]
    json_filename = f"{domain}.json"
    html_filename = f"{domain}.html"

    if os.path.exists(json_filename):
        with open(json_filename, "r+", encoding="utf-8") as json_file:
            try:
                existing_data = json.load(json_file)
                if isinstance(existing_data, list):
                    existing_data.append(data)
                else:
                    existing_data = [existing_data, data]
            except json.JSONDecodeError:
                existing_data = [data]

            json_file.seek(0)
            json.dump(existing_data, json_file, indent=4)
    else:
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump([data], json_file, indent=4)

    if pagination_content:
        with open(html_filename, "w", encoding="utf-8") as html_file:
            html_file.write(pagination_content)


def get_cleaned_content(driver):
    body = driver.find_element(By.TAG_NAME, "body")
    soup = BeautifulSoup(body.get_attribute("outerHTML"), 'html.parser')

    tags_to_remove = [
        "header", "footer", "script", "style", "noscript", "nav", "iframe", 
        "form", "input", "svg", "aside", "button", "link", "meta", "picture", 
        "source", "object", "embed", "param", "canvas", "map", "area"
    ]

    for tag in soup.find_all(tags_to_remove):
        tag.decompose()
    
    for pagination in soup.find_all(class_=lambda x: x is not None and isinstance(x, str) and "pagination" in x.lower()):
        pagination.decompose()

    child_tags = set()
    for child in soup.body.find_all(recursive=False):
        child_tags.add(child.name)

    for tag in soup.find_all(child_tags):
        if tag.text == "" or tag.text ==  None:
            tag.decompose()

    return str(soup)


def scrape_pagination(driver):
    extracted_content = set()
    pagination_content_data = ""
    pagination_detected = False
    find_locator = None

    locators = [
        (By.CSS_SELECTOR, 'a[rel="next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[contains(translate(@aria-label, "NEXT", "next"), "next")]'), (By.CSS_SELECTOR, 'a[data-action="next"]'),
        (By.CSS_SELECTOR, 'a.next'), (By.CSS_SELECTOR, 'button.next'), (By.XPATH, '//a[contains(@class, "next")]'),
        (By.XPATH, '//a[normalize-space(translate(text(), "NEXT", "next")) = "next"]'), (By.XPATH, '//a[contains(translate(text(), "NEXT", "next"), "next")]'), (By.LINK_TEXT, "Next"),
        (By.XPATH, '//div[@class="pagination"]//a[text()="Next"]'), (By.XPATH, '//a[text()="Previous"]/following-sibling::a'), (By.CSS_SELECTOR, 'ul.pagination a:last-child'),
        (By.CSS_SELECTOR, 'a[href*="next"]'), (By.XPATH, '//a[contains(@href, "page")]'), (By.XPATH, '//a[contains(text(), "Next")]')
    ]

    excluded_extensions = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}
    current_domain = urlparse(driver.current_url).netloc.split("www.")[-1].lower()

    while True:
        try:
            scroll_to_bottom(driver)
            next_button = None

            if not find_locator:
                for locator in locators:
                    try:
                        next_button = driver.find_element(*locator)
                        href = next_button.get_attribute('href') if next_button else None
                        if href and urlparse(href).netloc.split("www.")[-1].lower() != current_domain or any(href.lower().endswith(ext) for ext in excluded_extensions):
                            next_button = None
                            continue
                        
                        find_locator = locator
                        break
                    except:
                        continue
            else:
                try:
                    next_button = driver.find_element(*find_locator)
                    href = next_button.get_attribute('href') if next_button else None
                    if href and urlparse(href).netloc.split("www.")[-1].lower() != current_domain or any(href.lower().endswith(ext) for ext in excluded_extensions):
                        break
                except:
                    break

            if next_button:
                pagination_detected = True
            
            if pagination_detected: 
                    cleaned_content = get_cleaned_content(driver)
                    new_content = []
                    for line in cleaned_content.split("\n"):
                        if line.strip() not in extracted_content:
                            new_content.append(line.strip())
                            extracted_content.add(line.strip())

                    cleaned_content = "\n".join(new_content)
                    if cleaned_content in pagination_content_data:
                        break
                    pagination_content_data += cleaned_content

            if not next_button or not next_button.is_displayed() or not next_button.is_enabled():
                break
            
            if any(
                    "disabled" in element.get_attribute("class") or
                    element.get_attribute("aria-disabled") == "true" or
                    element.get_attribute("disabled") is not None or
                    "pointer-events: none" in element.get_attribute("style") or
                    "disabled" in element.get_attribute("innerHTML")
                    for element in [next_button]
                ):
                    break

            if next_button:
                try:
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_button)
                    time.sleep(1.5)
                    ActionChains(driver).move_to_element(next_button).click().perform()
                    time.sleep(0.5)
                except:
                    time.sleep(1.5)
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(0.5)

        except Exception as e:
            print(f"Pagination Error: {e}")
            break
    
    if pagination_detected:
        return pagination_content_data, True
    else:
        return driver.find_element(By.TAG_NAME, "body").get_attribute("outerHTML"), False


def scrape_data(urls):
    for url in urls:
        data = {}

        driver = initialize_driver()
        driver.get(url)
        try:
            search_box = driver.find_element(By.NAME, "q")
            human_typing(search_box, "Selenium anti-detection techniques")
        except:
            pass

        time.sleep(random.uniform(0.3, 1.6))

        try:
            data["Domain"] = urlparse(url).netloc.split("www.")[-1]
            data["Title"] = driver.title
            data["Description"] = get_description(driver)
            data["LinkedIn URL"] = find_linkedin_on_website(driver)
            data["MX Records"], data["Mail Provider"], data["Mail Status"] = get_mx_records(urlparse(url).netloc)

            accept_cookies(driver)
            scroll_to_bottom(driver)

            # relevant_pages = find_relevant_pages(driver)
            pagination_content_data, pagination_found = scrape_pagination(driver)
            # if driver.current_url in relevant_pages:
            #     relevant_pages.remove(driver.current_url)

            data['Pagination Detected'] = pagination_found

            try:
                soup = BeautifulSoup(pagination_content_data, 'html.parser')
                tables = soup.find_all("table")
                if tables:
                    table_data = []
                    for table in tables:
                        rows = []
                        headers = []
                        header_row = table.find('tr')
                        if header_row:
                            headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]
                        for row in table.find_all('tr'):
                            if row == header_row and headers:
                                continue
                            cols = [col.get_text(strip=True) for col in row.find_all(['td', 'th'])]
                            if cols:
                                rows.append(cols)
                        if headers and rows:
                            table_dicts = []
                            for row in rows:
                                if len(row) == len(headers):
                                    table_dicts.append(dict(zip(headers, row)))
                            table_data.append(table_dicts)
                        else:
                            table_data.append(rows)
                    data['Tables'] = table_data
                else:
                    tag_content = {}

                    for tag in soup.find_all():
                        text = tag.get_text(strip=True)
                        if text:
                            if tag.name not in tag_content:
                                tag_content[tag.name] = set()
                            tag_content[tag.name].add(text)

                    cleaned_text_dict = {tag: list(content) for tag, content in tag_content.items()}
                    data['Cleaned Text'] = cleaned_text_dict

            except Exception as e:
                print(f"Error processing content: {e}")

            save_data(data, pagination_content_data)

            # save_data(data, pagination_content_data)


            # pages = []
            # for url in relevant_pages:
            #     parsed_url = urlparse(url)
            #     scheme, netloc, path = parsed_url.scheme, parsed_url.netloc, parsed_url.path
            #     pages.append(f"{scheme}://{netloc}{path}")

            # pages = list(set(pages))

            # for page in pages:
            #     data = {}
            #     data["Domain"] = urlparse(url).netloc.split("www.")[-1]
            #     data['URL'] = page
            #     driver.get(page)
            #     time.sleep(1)
            #     scroll_to_bottom(driver)

            #     pagination_content_data = scrape_pagination(driver)

            #     data['Pagination Content Data'] = pagination_content_data
            #     save_data(data)

        except Exception as e:
            print(f"Error scraping {url}: {e}")
        finally:
            time.sleep(1)
            if driver:
                driver.quit()
            del driver


urls = [
    # "https://www.wbs.ac.uk/about/people/",
    # "https://tpchd.org/info/staff-directory/",
    # "https://www.eversana.com/thought-leaders/",
    # "https://www.health.columbia.edu/directory",
    # "https://www.nnlm.gov/about/staff-directory",
    # "https://meded.ucsf.edu/about-us/our-people",
    # "https://www.ucb.ac.uk/about-us/staff-directory/",
    # "https://www.ruralhealth.us/about-us/staff-directory",
    # "https://datascience.cancer.gov/about/staff-directory",
    "https://www.stowe.co.uk/school/academic/staff-directory",
    # "https://www.mdx.ac.uk/about-us/our-people/staff-directory/",
    # "https://www.dconc.gov/about-dco/contact-us/employee-directory",
    # "https://www.blythedale.org/about-the-hospital/staff-directory",
    # "https://www.marathoncounty.gov/about-us/staff-directory/-npage-5",
    # "https://ph.ucla.edu/about/faculty-staff-directory?type=all&page=1",
    # "https://www.researchgate.net/institution/Tulane-University/members",
    # "https://sc.edu/study/colleges_schools/public_health/faculty-staff/",
    # "https://med.umn.edu/dom/education/global-medicine/faculty-directory",
    # "https://www.emoryhenry.edu/academics/school-health-sciences/directory/",
    # "https://www.wlv.ac.uk/about-us/our-staff/?collection=wlv-web-our-staff&form=wlv-facet&query=&start_rank=21",
    # "https://www.homerton.nhs.uk/staff-directory/staff-directory?staffDirectory=true&searchTerm=&search=search&searchType=All"
]


# domain_url = []
# for url in urls:
#     parsed_url = urlparse(url)
#     scheme, netloc, path = parsed_url.scheme, parsed_url.netloc, parsed_url.path
#     domain_url.append(f"{scheme}://{netloc}")

# domain_url = list(set(domain_url))
scrape_data(urls)