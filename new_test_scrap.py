# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1770.50",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
#     "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
#     "Mozilla/5.0 (Android 13; Mobile; rv:113.0) Gecko/113.0 Firefox/113.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
# ]

# def initialize_driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument(f"user-agent={random.choice(user_agents)}")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--incognito")
#     options.add_argument("--start-maximized")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     driver = webdriver.Chrome(options=options)
#     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#     return driver

# def scroll_to_bottom(driver):
#     """Improved scroll function with content-aware checking"""
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)  # Increased delay for content loading
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

# def handle_pagination(driver):
#     """Enhanced pagination handling with explicit waits"""
#     while True:
#         try:
#             # Wait for page to stabilize
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//body"))
#             )

#             # Try to find next button using multiple strategies
#             next_button = None
#             locators = [
#                     (By.CSS_SELECTOR, 'a[rel="next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[normalize-space(text())="Next"]'), (By.XPATH, '//a[@class="next"]'),
#                     (By.XPATH, '//a[@aria-label="Next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[contains(@href, "next")]'), (By.LINK_TEXT, "Next"),
#                     (By.CSS_SELECTOR, 'a[aria-label="Next"]'), (By.CSS_SELECTOR, 'a[aria-label="Next page"]'), (By.CSS_SELECTOR, 'a[rel="next"]'), (By.CSS_SELECTOR, 'a[href*="page"]'),
#                     (By.CSS_SELECTOR, 'a[href*="next"]'), (By.CSS_SELECTOR, 'a.pg-normal.pg-button.pg-next-button'), (By.CSS_SELECTOR, 'button.next'), (By.XPATH, "//a[contains(translate(text(), 'NEXT', 'next'), 'next')]"),
#                     (By.ID, "next-button-id"), (By.XPATH, '//a[contains(@class, "next")]'), (By.CSS_SELECTOR, 'a[data-action="next"]'), (By.XPATH, '//div[@class="pagination"]//a[text()="Next"]'),
#                     (By.XPATH, '//a[text()="Previous"]/following-sibling::a'), (By.CSS_SELECTOR, 'div.pagination a:nth-of-type(2)'), (By.CSS_SELECTOR, 'a[aria-label="Next page"]'), (By.CSS_SELECTOR, 'button.next'),
#                     (By.XPATH, '//*[@role="button" and text()="Next"]'), (By.CSS_SELECTOR, 'a[title="Next page"]'), (By.XPATH, "//a[contains(text(), 'Next')]"), (By.CSS_SELECTOR, 'button[type="button"][class*="next"]'),
#                     (By.CSS_SELECTOR, 'a:hover[rel="next"]'), (By.CSS_SELECTOR, 'ul.pagination a:last-child')
#                 ]

#             for locator in locators:
#                 try:
#                     next_button = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located(locator)
#                     )
#                     if next_button.is_displayed() and next_button.is_enabled():
#                         break
#                 except:
#                     continue

#             if not next_button:
#                 break

#             # Check if button is actually clickable
#             try:
#                 WebDriverWait(driver, 5).until(EC.element_to_be_clickable(next_button))
#             except:
#                 break

#             # Store current page ID to check for navigation
#             current_page = driver.current_url

#             try:
#                 ActionChains(driver).move_to_element(next_button).click().perform()
#                 # Wait for page to change
#                 WebDriverWait(driver, 15).until(
#                     lambda d: d.current_url != current_page
#                 )
#                 # Wait for new content to load
#                 WebDriverWait(driver, 15).until(
#                     EC.presence_of_element_located((By.XPATH, "//body"))
#                 )
#                 time.sleep(2)  # Additional buffer
#             except (TimeoutException, StaleElementReferenceException):
#                 break

#             # Scroll to load potential lazy-loaded content
#             scroll_to_bottom(driver)

#         except Exception as e:
#             print(f"Pagination error: {str(e)}")
#             break

# urls = [
#         "https://www.eversana.com/thought-leaders/",
#         "https://www.health.columbia.edu/directory",
#         "https://www.forthealthcare.com/find-a-doctor/?last=a",
#         "https://www.ruralhealth.us/about-us/staff-directory",
#         "https://www.nnlm.gov/about/staff-directory",
#         "https://www.mdx.ac.uk/about-us/our-people/staff-directory/",
#         "https://datascience.cancer.gov/about/staff-directory",
#         "https://www.blythedale.org/about-the-hospital/staff-directory",
#         "https://www.ucb.ac.uk/about-us/staff-directory/",
#         "https://www.wbs.ac.uk/about/people/",
#         "https://www.marathoncounty.gov/about-us/staff-directory/",
#         "https://tpchd.org/info/staff-directory/",
#         "https://www.wlv.ac.uk/about-us/our-staff/?form=wlv-facet&query=&collection=wlv-web-our-staff",
#         "https://www.emoryhenry.edu/academics/school-health-sciences/directory/",
# ]

# for url in urls:
#     driver = initialize_driver()
#     try:
#         driver.get(url)
#         WebDriverWait(driver, 15).until(
#             EC.presence_of_element_located((By.XPATH, "//body"))
#         )

#         # Initial scroll to load content
#         scroll_to_bottom(driver)
        
#         # Handle pagination
#         handle_pagination(driver)

#     except Exception as e:
#         print(f"Error processing {url}: {str(e)}")
#     finally:
#         driver.quit()
#     time.sleep(random.uniform(2, 5))  # Random delay between sites


import time
import random
import dns.resolver
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# List of user agents to simulate different browsers and devices
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1770.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Android 13; Mobile; rv:113.0) Gecko/113.0 Firefox/113.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
]

def random_sleep(min_delay=1, max_delay=3):
    time.sleep(random.uniform(min_delay, max_delay))

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents)}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
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

def accept_cookies_human_like(driver):
    try:
        # Random delay before accepting cookies
        random_sleep(2, 5)
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
        )
        cookie_button.click()
        random_sleep(1, 3)  # Simulate delay after accepting cookies
    except Exception:
        pass

def simulate_mouse_move(driver):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    ActionChains(driver).move_by_offset(x, y).perform()
    random_sleep(1, 2)

def random_scroll(driver):
    scroll_step = random.randint(100, 300)  # Randomize scroll amount
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    random_sleep(1, 3)

def scroll_to_bottom_human_like(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        random_scroll(driver)
        random_sleep(1, 3)  # Pause before the next scroll
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Simulate final scroll to bottom to mimic a human user finishing the page load
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    random_sleep(2, 4)  # Final pause after reaching bottom

def click_element_human_like(driver, element):
    ActionChains(driver).move_to_element(element).perform()  # Hover first
    random_sleep(1, 3)  # Delay before clicking
    element.click()  # Click after delay
    random_sleep(2, 4)  # Delay after clicking

def get_cleaned_content_human_like(driver):
    body = driver.find_element(By.TAG_NAME, "body")
    driver.execute_script("""
        var header = arguments[0].querySelector('header');
        if (header) header.remove();
        
        var footer = arguments[0].querySelector('footer');
        if (footer) footer.remove();
        
        var pagination = arguments[0].querySelector('div[class*="pagination"]');
        if (pagination) pagination.remove();
    """, body)
    
    random_sleep(2, 4)  # Wait after removing elements to simulate human pause
    cleaned_content = body.get_attribute("outerHTML")
    return cleaned_content

def scrape_pagination_human_like(driver):
    locators = [
        (By.CSS_SELECTOR, 'a[rel="next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[normalize-space(text())="Next"]'),
        (By.XPATH, '//a[@class="next"]'), (By.XPATH, '//a[@aria-label="Next"]')
    ]

    find_locator = None
    while True:
        try:
            scroll_to_bottom_human_like(driver)
            next_button = None

            if not find_locator:
                for locator in locators:
                    try:
                        next_button = driver.find_element(*locator)
                        href = next_button.get_attribute('href')
                        if href and "youtube" in href.lower():
                            continue
                        else:
                            find_locator = locator
                            break
                    except:
                        continue

            elif find_locator:
                try:
                    next_button = driver.find_element(*find_locator)
                    href = next_button.get_attribute('href')
                    if href and "youtube" in href.lower():
                        continue
                except:
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
                    click_element_human_like(driver, next_button)
                except:
                    driver.execute_script("arguments[0].click();", next_button)

        except Exception:
            break

def random_user_agent():
    return random.choice(user_agents)

# Main scraping logic
urls = [
    "https://www.eversana.com/thought-leaders/",
    "https://www.health.columbia.edu/directory",
    "https://www.forthealthcare.com/find-a-doctor/?last=a",
    "https://www.ruralhealth.us/about-us/staff-directory",
    "https://www.nnlm.gov/about/staff-directory",
    "https://www.mdx.ac.uk/about-us/our-people/staff-directory/",
    "https://datascience.cancer.gov/about/staff-directory",
    "https://www.blythedale.org/about-the-hospital/staff-directory",
    "https://www.ucb.ac.uk/about-us/staff-directory/",
    "https://www.wbs.ac.uk/about/people/",
    "https://www.marathoncounty.gov/about-us/staff-directory/",
    "https://tpchd.org/info/staff-directory/",
    "https://www.wlv.ac.uk/about-us/our-staff/?form=wlv-facet&query=&collection=wlv-web-our-staff",
    "https://www.emoryhenry.edu/academics/school-health-sciences/directory/",
]

for url in urls:
    data = {}
    
    driver = initialize_driver()
    driver.get(url)
    random_sleep(3, 5)  # Delay before starting to interact with the page

    data["Domain"] = urlparse(url).netloc.split("www.")[-1]
    data["Title"] = driver.title
    data["Description"] = get_description(driver)
    data["LinkedIn URL"] = find_linkedin_on_website(driver)
    data["MX Records"], data["Mail Provider"], data["Mail Status"] = get_mx_records(urlparse(url).netloc)

    accept_cookies_human_like(driver)
    scroll_to_bottom_human_like(driver)
    scrape_pagination_human_like(driver)

    # data["Content"] = get_cleaned_content_human_like(driver)

    random_sleep(3, 5)  # Pause before finishing the page scrape
    driver.quit()