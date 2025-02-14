import time
import random
import dns.resolver
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def get_cleaned_content(driver):
    body = driver.find_element(By.TAG_NAME, "body")
    driver.execute_script("""
        var header = arguments[0].querySelector('header');
        if (header) header.remove();
        
        var footer = arguments[0].querySelector('footer');
        if (footer) footer.remove();
        
        var scripts = arguments[0].querySelectorAll('script');
        scripts.forEach(function(script) { script.remove(); });
        
        var noscripts = arguments[0].querySelectorAll('noscript');
        noscripts.forEach(function(noscript) { noscript.remove(); });
        
        var styles = arguments[0].querySelectorAll('style');
        styles.forEach(function(style) { style.remove(); });
        
        var pagination = arguments[0].querySelector('div[class*="pagination"]');
        if (pagination) pagination.remove();
                        
        // Remove elements with no content or src/href attributes
        var elements = arguments[0].querySelectorAll('*');
        elements.forEach(function(element) {
            if (!element.textContent.trim() && !element.hasAttribute('src') && !element.hasAttribute('href')) {
                element.remove();
            } else if (element.hasAttribute('href') && 
                    (element.getAttribute('href').startsWith('mailto:') || element.getAttribute('href').startsWith('tel:'))) {
                element.remove();
            }
        });
    """, body)
    cleaned_content = body.get_attribute("outerHTML")
    return cleaned_content


# url = 'https://www.ruralhealth.us/about-us/staff-directory'
# url = 'https://aabhyasa.com/'

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
    # time.sleep(random.uniform(2, 5))
    driver = initialize_driver()
    driver.get(url)
    time.sleep(5)

# mx_records, mail_provider, mail_status = get_mx_records(urlparse(url).netloc)
# description = get_description(driver)
# linkedin_profile = find_linkedin_on_website(driver)

# print(
#     f"Domain: {urlparse(url).netloc.split('www.')[-1]}\n"
#     f"Title: {driver.title}\n"
#     f"Description: {description}\n"
#     f"MX Records: {mx_records}\n"
#     f"Mail Provider: {mail_provider}\n"
#     f"Mail Status: {mail_status}\n"
#     f"LinkedIn URL: {linkedin_profile}"
# )

    # def get_pagination_data(driver):
    #     pagination_script = """
    #     function analyzePagination() {
    #         const pagination = {
    #             currentPage: null,
    #             totalPages: null,
    #             nextPage: null,
    #             prevPage: null,
    #             pages: []
    #         };

    #         const containers = document.querySelectorAll([
    #             '.pagination', 
    #             '.pager', 
    #             '[role="navigation"]',
    #             '[aria-label*="pagination i"], [aria-label*="page"]',
    #             '.pagination-banner',
    #             '.pagination-md'
    #         ].join(','));

    #         containers.forEach(container => {
    #             const currentElements = container.querySelectorAll([
    #                 '.active', 
    #                 '.current', 
    #                 '[aria-current="page"]',
    #                 '.is-active',
    #                 '.activepage'
    #             ].join(','));
                
    #             currentElements.forEach(el => {
    #                 const page = parseInt(el.textContent);
    #                 if (!isNaN(page)) pagination.currentPage = page;
    #             });

    #             const pageLinks = container.querySelectorAll('a, span, li');
    #             const pages = [];
                
    #             pageLinks.forEach(link => {
    #                 const url = link.href || '';
    #                 const text = link.textContent.trim();
                    
    #                 const urlParams = new URLSearchParams(url.split('?')[1]);
    #                 const pageFromUrl = urlParams.get('page') || 
    #                                 urlParams.get('sf_paged') || 
    #                                 url.match(/[?&](page|paged|pg)=(\d+)/)?.[2];
                    
    #                 const pageFromText = parseInt(text.match(/\d+/)?.[0]);
    #                 const page = parseInt(pageFromUrl) || pageFromText;
                    
    #                 if (!isNaN(page)) pages.push(page);
                    
    #                 if (link.rel.includes('next') || text.match(/next/i)) {
    #                     pagination.nextPage = url;
    #                 }
    #                 if (link.rel.includes('prev') || text.match(/prev|previous/i)) {
    #                     pagination.prevPage = url;
    #                 }
    #             });

    #             const pageTextMatches = container.textContent.match(
    #                 /(?:Page|of|total|of)\s*(\d+)\s*(?:pages|$)/i
    #             );
    #             if (pageTextMatches) {
    #                 pagination.totalPages = parseInt(pageTextMatches[1]);
    #             }
                
    #             const uniquePages = [...new Set(pages)].sort((a, b) => a - b);
    #             if (uniquePages.length > 0) {
    #                 pagination.pages = uniquePages;
    #                 if (!pagination.totalPages || Math.max(...uniquePages) > pagination.totalPages) {
    #                     pagination.totalPages = Math.max(...uniquePages);
    #                 }
    #             }
    #         });

    #         return pagination;
    #     }
    #     return analyzePagination();
    #     """
    #     return driver.execute_script(pagination_script)

    # def click_next_pages(driver):
    #     while True:
    #         pagination_data = get_pagination_data(driver)
    #         print("Detected Pagination:", pagination_data)

    #         next_page_url = pagination_data.get("nextPage")

    #         if not next_page_url:
    #             print("No more pages to navigate.")
    #             break
            
    #         try:
    #             # Click the next button if found
    #             next_button = WebDriverWait(driver, 5).until(
    #                 EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next') or contains(@rel, 'next')]"))
    #             )
    #             driver.execute_script("arguments[0].scrollIntoView();", next_button)
    #             driver.execute_script("arguments[0].click();", next_button)

    #             print("Clicked next page...")

    #             # Wait for new content to load
    #             WebDriverWait(driver, 5).until(lambda d: get_pagination_data(driver).get("currentPage") != pagination_data.get("currentPage"))

    #         except Exception as e:
    #             print("Failed to navigate to next page:", e)
    #             break

    # click_next_pages(driver)


    def scroll_to_bottom(driver):
        scroll_step = 80
        delay = 0.05

        while True:
            last_height = driver.execute_script("return document.documentElement.scrollHeight")
            current_position = driver.execute_script("return window.pageYOffset + window.innerHeight")

            while current_position < last_height:
                driver.execute_script(f"window.scrollBy(0, {scroll_step});")
                time.sleep(delay)
                current_position = driver.execute_script("return window.pageYOffset + window.innerHeight")

            time.sleep(1)
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break

        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    def scrape_pagination(driver):
        while True:
            try:
                scroll_to_bottom(driver)

                next_button = None
                last_page_link = None  # You should define this if it's needed for checks

                for locator in [
                    (By.XPATH, '//a[normalize-space(text())="Next"]'),
                    (By.XPATH, '//a[@class="next"]'),
                    (By.XPATH, '//a[@aria-label="Next"]'),
                    (By.XPATH, '//a[@rel="next"]'),
                    (By.XPATH, '//a[contains(@href, "next")]'),
                    (By.LINK_TEXT, "Next"),
                    (By.CSS_SELECTOR, 'a[aria-label="Next"]'),
                    (By.CSS_SELECTOR, 'a[rel="next"]'),
                    (By.CSS_SELECTOR, 'a[href*="page"]'),
                    (By.CSS_SELECTOR, 'a[rel="next"]'),
                    (By.CSS_SELECTOR, 'a[href*="next"]'),
                    (By.CSS_SELECTOR, 'a.pg-normal.pg-button.pg-next-button'),
                    (By.CSS_SELECTOR, 'button.next')
                ]:
                    try:
                        next_button = driver.find_element(*locator)
                        break
                    except:
                        continue
                
                for locator in [
                    (By.XPATH, '//a[normalize-space(text())="Last"]'),
                    (By.XPATH, '//a[@class="last"]'),
                    (By.XPATH, '//a[@aria-label="Last"]'),
                    (By.XPATH, '//a[@rel="last"]'),
                    (By.XPATH, '//a[contains(@href, "last")]'),
                    (By.CSS_SELECTOR, 'a[aria-label="Last"]'),
                    (By.CSS_SELECTOR, 'a[rel="last"]'),
                    (By.CSS_SELECTOR, 'a[href*="last"]'),
                ]:
                    try:
                        last_page_link = driver.find_element(*locator)
                        break
                    except:
                        continue

                if not next_button:
                    break

                if any(
                    "disabled" in element.get_attribute("class") or
                    element.get_attribute("aria-disabled") == "true" or
                    element.get_attribute("disabled") is not None or
                    "pointer-events: none" in element.get_attribute("style") or
                    "disabled" in element.get_attribute("innerHTML")
                    for element in [next_button, last_page_link]
                ):
                    break

                next_button.click()

            except Exception as e:
                break
        
    scrape_pagination(driver)
    time.sleep(random.uniform(1,5))
    
    driver.quit()




#     import time
# import random
# import dns.resolver
# from selenium import webdriver
# from urllib.parse import urlparse
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException

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

# def get_mx_records(domain):
#     mail_provider_map = {
#         "google.com": "Google (Gmail)", "l.google.com": "Google (Gmail)", "outlook.com": "Microsoft (Outlook)",
#         "hotmail.com": "Microsoft (Outlook)", "yahoo.com": "Yahoo Mail", "zoho.com": "Zoho Mail",
#         "icloud.com": "Apple iCloud Mail", "protonmail.com": "ProtonMail"
#     }
#     try:
#         answers = dns.resolver.resolve(domain, 'MX')
#         mx_records = [r.exchange.to_text().strip('.') for r in answers]
        
#         if not mx_records:
#             return [], "Null", 0

#         provider_name = "Unknown Provider"
#         for record in mx_records:
#             domain_parts = record.split(".")[-3:]
#             provider_name = mail_provider_map.get(".".join(domain_parts), mail_provider_map.get(".".join(domain_parts[-2:]), "Unknown Provider"))
#             if provider_name != "Unknown Provider":
#                 break

#         return mx_records, provider_name, 1
#     except Exception:
#         return [], "Null", 0

# def get_description(driver):
#     try:
#         description = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")
#         return description
#     except:
#         description = "No description found"
#         return description

# def find_linkedin_on_website(driver):
#     try:
#         linkedin_link = driver.find_element(By.XPATH, "//a[contains(@href, 'linkedin.com/company/')]").get_attribute("href")
#         return linkedin_link
#     except:
#         return "LinkedIn profile not found"

# def get_cleaned_content(driver):
#     body = driver.find_element(By.TAG_NAME, "body")
#     driver.execute_script("""
#         var header = arguments[0].querySelector('header');
#         if (header) header.remove();
        
#         var footer = arguments[0].querySelector('footer');
#         if (footer) footer.remove();
        
#         var scripts = arguments[0].querySelectorAll('script');
#         scripts.forEach(function(script) { script.remove(); });
        
#         var noscripts = arguments[0].querySelectorAll('noscript');
#         noscripts.forEach(function(noscript) { noscript.remove(); });
        
#         var styles = arguments[0].querySelectorAll('style');
#         styles.forEach(function(style) { style.remove(); });
        
#         var pagination = arguments[0].querySelector('div[class*="pagination"]');
#         if (pagination) pagination.remove();
                        
#         // Remove elements with no content or src/href attributes
#         var elements = arguments[0].querySelectorAll('*');
#         elements.forEach(function(element) {
#             if (!element.textContent.trim() && !element.hasAttribute('src') && !element.hasAttribute('href')) {
#                 element.remove();
#             } else if (element.hasAttribute('href') && 
#                     (element.getAttribute('href').startsWith('mailto:') || element.getAttribute('href').startsWith('tel:'))) {
#                 element.remove();
#             }
#         });
#     """, body)
#     cleaned_content = body.get_attribute("outerHTML")
#     return cleaned_content


# # url = 'https://www.ruralhealth.us/about-us/staff-directory'
# # url = 'https://aabhyasa.com/'

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
#         ]

# for url in urls:
#     # time.sleep(random.uniform(2, 5))
#     driver = initialize_driver()
#     driver.get(url)
#     time.sleep(5)

# mx_records, mail_provider, mail_status = get_mx_records(urlparse(url).netloc)
# description = get_description(driver)
# linkedin_profile = find_linkedin_on_website(driver)

# print(
#     f"Domain: {urlparse(url).netloc.split('www.')[-1]}\n"
#     f"Title: {driver.title}\n"
#     f"Description: {description}\n"
#     f"MX Records: {mx_records}\n"
#     f"Mail Provider: {mail_provider}\n"
#     f"Mail Status: {mail_status}\n"
#     f"LinkedIn URL: {linkedin_profile}"
# )

    # def get_pagination_data(driver):
    #     pagination_script = """
    #     function analyzePagination() {
    #         const pagination = {
    #             currentPage: null,
    #             totalPages: null,
    #             nextPage: null,
    #             prevPage: null,
    #             pages: []
    #         };

    #         const containers = document.querySelectorAll([
    #             '.pagination', 
    #             '.pager', 
    #             '[role="navigation"]',
    #             '[aria-label*="pagination i"], [aria-label*="page"]',
    #             '.pagination-banner',
    #             '.pagination-md'
    #         ].join(','));

    #         containers.forEach(container => {
    #             const currentElements = container.querySelectorAll([
    #                 '.active', 
    #                 '.current', 
    #                 '[aria-current="page"]',
    #                 '.is-active',
    #                 '.activepage'
    #             ].join(','));
                
    #             currentElements.forEach(el => {
    #                 const page = parseInt(el.textContent);
    #                 if (!isNaN(page)) pagination.currentPage = page;
    #             });

    #             const pageLinks = container.querySelectorAll('a, span, li');
    #             const pages = [];
                
    #             pageLinks.forEach(link => {
    #                 const url = link.href || '';
    #                 const text = link.textContent.trim();
                    
    #                 const urlParams = new URLSearchParams(url.split('?')[1]);
    #                 const pageFromUrl = urlParams.get('page') || 
    #                                 urlParams.get('sf_paged') || 
    #                                 url.match(/[?&](page|paged|pg)=(\d+)/)?.[2];
                    
    #                 const pageFromText = parseInt(text.match(/\d+/)?.[0]);
    #                 const page = parseInt(pageFromUrl) || pageFromText;
                    
    #                 if (!isNaN(page)) pages.push(page);
                    
    #                 if (link.rel.includes('next') || text.match(/next/i)) {
    #                     pagination.nextPage = url;
    #                 }
    #                 if (link.rel.includes('prev') || text.match(/prev|previous/i)) {
    #                     pagination.prevPage = url;
    #                 }
    #             });

    #             const pageTextMatches = container.textContent.match(
    #                 /(?:Page|of|total|of)\s*(\d+)\s*(?:pages|$)/i
    #             );
    #             if (pageTextMatches) {
    #                 pagination.totalPages = parseInt(pageTextMatches[1]);
    #             }
                
    #             const uniquePages = [...new Set(pages)].sort((a, b) => a - b);
    #             if (uniquePages.length > 0) {
    #                 pagination.pages = uniquePages;
    #                 if (!pagination.totalPages || Math.max(...uniquePages) > pagination.totalPages) {
    #                     pagination.totalPages = Math.max(...uniquePages);
    #                 }
    #             }
    #         });

    #         return pagination;
    #     }
    #     return analyzePagination();
    #     """
    #     return driver.execute_script(pagination_script)

    # def click_next_pages(driver):
    #     while True:
    #         pagination_data = get_pagination_data(driver)
    #         print("Detected Pagination:", pagination_data)

    #         next_page_url = pagination_data.get("nextPage")

    #         if not next_page_url:
    #             print("No more pages to navigate.")
    #             break
            
    #         try:
    #             # Click the next button if found
    #             next_button = WebDriverWait(driver, 5).until(
    #                 EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next') or contains(@rel, 'next')]"))
    #             )
    #             driver.execute_script("arguments[0].scrollIntoView();", next_button)
    #             driver.execute_script("arguments[0].click();", next_button)

    #             print("Clicked next page...")

    #             # Wait for new content to load
    #             WebDriverWait(driver, 5).until(lambda d: get_pagination_data(driver).get("currentPage") != pagination_data.get("currentPage"))

    #         except Exception as e:
    #             print("Failed to navigate to next page:", e)
    #             break

    # click_next_pages(driver)

    # def scroll_to_bottom(driver):
    #     scroll_step = 80
    #     delay = 0.05

    #     while True:
    #         last_height = driver.execute_script("return document.documentElement.scrollHeight")
    #         current_position = driver.execute_script("return window.pageYOffset + window.innerHeight")

    #         while current_position < last_height:
    #             driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    #             time.sleep(delay)
    #             current_position = driver.execute_script("return window.pageYOffset + window.innerHeight")

    #         time.sleep(1)
    #         new_height = driver.execute_script("return document.documentElement.scrollHeight")
    #         if new_height == last_height:
    #             break

    #     driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # def scrape_pagination(driver):
    #     while True:
    #         try:
    #             scroll_to_bottom(driver)

    #             # Wait until the "Next" button is clickable and then click it
    #             next_button = WebDriverWait(driver, 10).until(
    #                 EC.visibility_of_element_located((
    #                     By.XPATH, 
    #                     '//a[normalize-space(text())="Next" or @class="next" or @aria-label="Next" or @rel="next" or contains(@href, "next")]' 
    #                 )))

    #             # If the button is disabled, break the loop
    #             if (
    #                 "disabled" in next_button.get_attribute("class") or
    #                 next_button.get_attribute("aria-disabled") == "true" or
    #                 next_button.get_attribute("disabled") is not None or
    #                 "pointer-events: none" in next_button.get_attribute("style") or
    #                 "disabled" in next_button.get_attribute("innerHTML")
    #             ):
    #                 break

    #             # Scroll into view before clicking to avoid interception
    #             ActionChains(driver).move_to_element(next_button).perform()

    #             next_button.click()
            
    #         except (NoSuchElementException, ElementClickInterceptedException, TimeoutException) as e:
    #             try:
    #                 # If ElementClickInterceptedException occurs, scroll to the next button and try clicking again
    #                 next_button = driver.find_element(By.CSS_SELECTOR, 'button.next')
    #                 if (
    #                     "disabled" in next_button.get_attribute("class") or
    #                     next_button.get_attribute("aria-disabled") == "true" or
    #                     next_button.get_attribute("disabled") is not None
    #                 ):
    #                     break

    #                 # Scroll into view before clicking
    #                 ActionChains(driver).move_to_element(next_button).perform()
    #                 next_button.click()

    #             except (NoSuchElementException, ElementClickInterceptedException, TimeoutException):
    #                 try:
    #                     # Try finding the "Next" link in pagination
    #                     page_links = driver.find_elements(By.CSS_SELECTOR, 'a[rel="next"], a[href*="next"], a.pg-normal.pg-button.pg-next-button')
    #                     if page_links:
    #                         last_page_link = page_links[-1]

    #                         if (
    #                             "disabled" in last_page_link.get_attribute("class") or
    #                             last_page_link.get_attribute("aria-disabled") == "true" or
    #                             last_page_link.get_attribute("disabled") is not None or
    #                             "pointer-events: none" in last_page_link.get_attribute("style") or
    #                             "disabled" in last_page_link.get_attribute("innerHTML")
    #                         ):
    #                             break  # Break if the next link is disabled

    #                         # Scroll into view before clicking
    #                         ActionChains(driver).move_to_element(last_page_link).perform()
    #                         last_page_link.click()
    #                     else:
    #                         break  # No next page link found, exit loop

    #                 except NoSuchElementException:
    #                     break  # No pagination links found, exit loop

    # scrape_pagination(driver)
    # time.sleep(random.uniform(1,5))
    
    # driver.quit()