import os
import time
import json
import random
import dns.resolver
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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

def get_cleaned_content(driver):
    body = driver.find_element(By.TAG_NAME, "body")
    soup = BeautifulSoup(body.get_attribute("outerHTML"), 'html.parser')

    tags_to_remove = ["header", "footer", "script", "style", "noscript", "nav", "iframe"]
    for tag in tags_to_remove:
        for element in soup.find_all(tag):
            element.decompose()

    for pagination in soup.find_all("div", class_="pagination"):
        pagination.decompose()

    return str(soup)
    
    # driver.execute_script("""
    #     var header = arguments[0].querySelector('header');
    #     if (header) header.remove();
        
    #     var nav = arguments[0].querySelector('nav');
    #     if (nav) nav.remove();
        
    #     var footer = arguments[0].querySelector('footer');
    #     if (footer) footer.remove();

    #     var iframes = arguments[0].querySelector('iframe');
    #     iframes.forEach(function(iframe) { iframe.remove(); });
        
    #     var scripts = arguments[0].querySelectorAll('script');
    #     scripts.forEach(function(script) { script.remove(); });
        
    #     var noscripts = arguments[0].querySelectorAll('noscript');
    #     noscripts.forEach(function(noscript) { noscript.remove(); });
        
    #     var styles = arguments[0].querySelectorAll('style');
    #     styles.forEach(function(style) { style.remove(); });
        
    #     var pagination = arguments[0].querySelector('div[class*="pagination"]');
    #     if (pagination) pagination.remove();
                        
    #     // Remove elements with no content or src/href attributes
    #     var elements = arguments[0].querySelectorAll('*');
    #     elements.forEach(function(element) {
    #         if (!element.textContent.trim() && !element.hasAttribute('src') && !element.hasAttribute('href')) {
    #             element.remove();
    #         } else if (element.hasAttribute('href') && 
    #                 (element.getAttribute('href').startsWith('mailto:') || element.getAttribute('href').startsWith('tel:'))) {
    #             element.remove();
    #         }
    #     });
    # """, body)
    # cleaned_content = body.get_attribute("outerHTML")

def scrape_pagination(driver):
        extracted_content = set()
        pagination_content_data = ""
        pagination_detected = False

        locators = [
            (By.CSS_SELECTOR, 'a[rel="next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[normalize-space(text())="Next"]'), (By.XPATH, '//a[@class="next"]'),
            (By.XPATH, '//a[@aria-label="Next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[contains(@href, "next")]'), (By.LINK_TEXT, "Next"),
            (By.CSS_SELECTOR, 'a[aria-label="Next"]'), (By.CSS_SELECTOR, 'a[aria-label="Next page"]'), (By.CSS_SELECTOR, 'a[rel="next"]'),
            (By.CSS_SELECTOR, 'a[href*="next"]'), (By.CSS_SELECTOR, 'a.pg-normal.pg-button.pg-next-button'), (By.CSS_SELECTOR, 'button.next'), 
            (By.XPATH, "//a[contains(translate(text(), 'NEXT', 'next'), 'next')]"), (By.ID, "next-button-id"), (By.XPATH, '//a[contains(@class, "next")]'), 
            (By.CSS_SELECTOR, 'a[data-action="next"]'), (By.XPATH, '//div[@class="pagination"]//a[text()="Next"]'), (By.XPATH, '//a[text()="Previous"]/following-sibling::a'),
            (By.CSS_SELECTOR, 'div.pagination a:nth-of-type(2)'), (By.CSS_SELECTOR, 'a[aria-label="Next page"]'), (By.CSS_SELECTOR, 'button.next'),
            (By.XPATH, '//*[@role="button" and text()="Next"]'), (By.CSS_SELECTOR, 'a[title="Next page"]'), (By.XPATH, "//a[contains(text(), 'Next')]"), (By.CSS_SELECTOR, 'button[type="button"][class*="next"]'),
            (By.CSS_SELECTOR, 'a:hover[rel="next"]'), (By.CSS_SELECTOR, 'ul.pagination a:last-child'), (By.XPATH, "//a[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='next']"), 
            (By.CSS_SELECTOR, 'a[href*="page"]'), (By.XPATH, "//a[contains(translate(text(), 'OLDER', 'older'), 'older')]")
        ]

        find_locator = None
        while True:
            try:
                scroll_to_bottom(driver)
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
                                pagination_detected = True
                                break
                        except:
                            continue

                elif find_locator:
                    try:
                        next_button = driver.find_element(*find_locator)
                        href = next_button.get_attribute('href')
                        if href and urlparse(url).netloc.split("www.")[-1] in href.lower():
                            continue
                    except:
                        break
                
                if pagination_detected: 
                    cleaned_content = get_cleaned_content(driver)
                    new_content = []
                    for line in cleaned_content.split("\n"):
                        if line.strip() not in extracted_content:
                            new_content.append(line.strip())
                            extracted_content.add(line.strip())

                    cleaned_content = "\n".join(new_content)
                    pagination_content_data += cleaned_content

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
                        ActionChains(driver).move_to_element(next_button).perform()
                        next_button.click()
                    except:
                        driver.execute_script("arguments[0].click();", next_button)

            except Exception as e:
                break
        
        if pagination_detected:
            return pagination_content_data
        else:
            return driver.find_element(By.TAG_NAME, "body").get_attribute("outerHTML")

def save_data(data, pagination_content):
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

    with open(html_filename, "w", encoding="utf-8") as html_file:
        html_file.write(pagination_content)

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
    time.sleep(3)

    data["Domain"] = urlparse(url).netloc.split("www.")[-1]
    data["Title"] = driver.title
    data["Description"] = get_description(driver)
    data["LinkedIn URL"] = find_linkedin_on_website(driver)
    data["MX Records"], data["Mail Provider"], data["Mail Status"] = get_mx_records(urlparse(url).netloc)

    accept_cookies(driver)
    scroll_to_bottom(driver)
    pagination_content_data = scrape_pagination(driver)

    data['Pagination Content Data'] = pagination_content_data
    save_data(data, pagination_content_data)

    time.sleep(3)
    driver.quit()