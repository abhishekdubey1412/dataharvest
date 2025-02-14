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

def find_relevant_pages(driver):
    relevant_keywords = [
        "about", "team", "leadership", "people", "profile", "staff", "contact", "history", "culture",
        "executives", "board", "directory", "organization", "members", "employees"
    ]
    relevant_links = set()
    
    try:
        anchor_tags = driver.find_elements(By.TAG_NAME, 'a')
        
        for anchor in anchor_tags:
            href = anchor.get_attribute("href")
            if 'login' in href.lower():
                continue
            
            if any(keyword.lower() in href.lower() for keyword in relevant_keywords):
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
        
        print("Yes")
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

    # body = driver.find_element(By.TAG_NAME, "body")
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
    # return cleaned_content

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
        dom_before_click = None

        while True:
            try:
                scroll_to_bottom(driver)
                next_button = None

                if not find_locator:
                    current_domain = urlparse(driver.current_url).netloc.split("www.")[-1].lower()

                    for locator in locators:
                        try:
                            next_button = driver.find_element(*locator)
                            href = next_button.get_attribute('href')

                            if href:
                                href_domain = urlparse(href).netloc.split("www.")[-1].lower()
                                if href_domain != current_domain:
                                    continue

                            find_locator = locator
                            pagination_detected = True
                            break
                        except:
                            continue

                elif find_locator:
                    try:
                        next_button = driver.find_element(*find_locator)
                        href = next_button.get_attribute('href')
                        if href:
                            href_domain = urlparse(href).netloc.split("www.")[-1].lower()
                            if href_domain != current_domain:
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

                        if not dom_before_click:
                            dom_before_click = driver.page_source
                        elif dom_before_click == driver.page_source:
                            break

                        if not urlparse(driver.current_url).netloc.split("www.")[-1].lower() == urlparse(next_button.get_attribute('href')).netloc.split("www.")[-1].lower():
                            continue
                        next_button.click()
                        driver.page_source
                    except:
                        if not dom_before_click:
                            dom_before_click = driver.page_source
                        elif dom_before_click == driver.page_source:
                            break
                        
                        if not urlparse(driver.current_url).netloc.split("www.")[-1].lower() == urlparse(next_button.get_attribute('href')).netloc.split("www.")[-1].lower():
                            continue
                        driver.execute_script("arguments[0].click();", next_button)
                        dom_before_click = driver.page_source

            except Exception as e:
                break
        
        if pagination_detected:
            return pagination_content_data
        else:
            return driver.find_element(By.TAG_NAME, "body").get_attribute("outerHTML")

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

urls = [
        # "https://www.eversana.com/thought-leaders/",
        # "https://www.definitivehc.com/about/our-people",
        "https://www.nimhd.nih.gov/about/overview/staff-directory.html",
        "https://www.paloverdehospital.org/Directory.aspx",
        "https://healthcareerfund.org/about-us/staff-directory/",
        "https://www.health.columbia.edu/directory",
        "https://www.forthealthcare.com/find-a-doctor/?last=a",
        "https://www.forthealthcare.com/about/leadership/administrative-team/",
        "https://www.forthealthcare.com/about/leadership/board-of-directors/",
        "https://www.ruralhealth.us/about-us/staff-directory",
        "https://www.ruralhealth.us/about-us/board-of-trustees",
        "https://datascience.cancer.gov/about/staff-directory",
        "https://www.co.jefferson.wa.us/directory.aspx?did=25",
        "https://www.co.jefferson.wa.us/Directory.aspx",
        "https://www.shelbytnhealth.com/293/Leadership",
        "https://www.shelbytnhealth.com/Directory.aspx",
        "https://doh.sd.gov/contact/staff-directory/",
        "https://www.uclahealth.org/programs/ccsw/about-us/staff-directory/administrative-support",
        "https://limr.mainlinehealth.org/about/staff-directory",
        "https://umc.edu/son/Faculty-Staff/Staff-Directory.html",
        "https://www.nih.gov/about-nih/who-we-are/nih-leadership",
        "https://health.maryland.gov/pophealth/pages/StaffDirectory.aspx",
        "https://health.maryland.gov/Pages/officeofsecretary.aspx",
        "https://www.mirecc.va.gov/visn22/Staff_Directory.asp",
        "https://ukhealthcare.uky.edu/doctors-providers/advanced-practice-providers/directory",
        "https://ukhealthcare.uky.edu/doctors-providers/physician-liaison-program",
        "https://www.nnlm.gov/about/staff-directory",
        "https://www.ncdhhs.gov/about/leadership",
        "https://www.tfhd.com/patients-visitors/staff-directory/",
        "https://dceg2.cancer.gov/cgi-bin/Personnel.pl?1=ALL",
        "https://dceg2.cancer.gov/cgi-bin/Personnel.pl?1=OD%2CTDRP",
        "https://www.kdhe.ks.gov/Directory.aspx?DID=13",
        "https://www.bsu.edu/campuslife/healthcenter/aboutus/staffdirectory",
        "https://www.hcafloridahealthcare.com/locations/aventura-hospital/about-us/leadership",
        "https://www.alabamapublichealth.gov/ems/staff.html",
        "https://www.mclaren.org/main/physician-directory",
        "https://www.blythedale.org/about-the-hospital/staff-directory",
        "https://medicaleducation.weill.cornell.edu/about-us/staff-directory",
        "https://medicalboard.georgia.gov/about-us/gcmb-staff-directory",
        "https://www.neomed.edu/about/administration/faculty-staff-directory/?RECTYPE=E&FIRST_NAME=&LAST_NAME=&DISCIPLINE_DESC=%25&DISCSPEC=%25&SPECIALTY_DESC=%25&SHOWALL=0",
        "https://www.clearcreekcounty.us/Directory.aspx",
        "https://medicalstaff.islandhealth.ca/medical-staff-leadership#top",
        "https://www.co.monroe.mi.us/Directory.aspx",
        "https://www.lesueurcounty.gov/Directory.aspx",
        "https://www.co.grand.co.us/Directory.aspx",
        "https://www.livingstoncountyny.gov/Directory.aspx",
        "https://www.mdx.ac.uk/about-us/our-people/staff-directory/",
        "https://pitkincounty.com/Directory.aspx",
        "https://www.bismarcknd.gov/directory.aspx?did=13",
        "https://www.co.walworth.wi.us/directory.aspx",
        "https://mtha.org/about-mha/staff-directory/",
        "https://www.ucb.ac.uk/about-us/staff-directory/",
        "https://www.wbs.ac.uk/about/people/",
        "https://www.sccwi.gov/Directory.aspx",
        "https://www.yamhillcounty.gov/Directory.aspx",
        "https://www.countyofmerced.com/directory.aspx?did=10",
        "https://www.fbfl.us/directory.aspx",
        "https://www.co.hunterdon.nj.us/directory.aspx",
        "https://www.nyecountynv.gov/directory.aspx",
        "https://www.cambridgeunited.com/club/staff-directory",
        "https://www.portarthurtx.gov/directory.aspx",
        "https://www.qac.org/Directory.aspx",
        "https://www.monroecounty-fl.gov/directory.aspx",
        "https://windhamct.gov/directory.aspx",
        "https://www.tetoncountywy.gov/Directory.aspx?DID=29",
        "https://www.marathoncounty.gov/about-us/staff-directory/-npage-5",
        "https://scha.org/about/staff-directory/",
        "https://www.sacredheart.edu/faculty--staff-directory/?depcol=departments%3Epublic+health",
        "https://tpchd.org/i-want-to/about-us/about-the-health-department/staff-directory/",
        "https://www.taoscounty.org/Directory.aspx",
        "https://www.homerton.nhs.uk/staff-directory/staff-directory?staffDirectory=true&searchTerm=&search=search&searchType=All",
        "https://www.wlv.ac.uk/about-us/our-staff/?collection=wlv-web-our-staff&form=wlv-facet&query=&start_rank=21",
        "https://health.frederickcountymd.gov/directory.aspx",
        "https://mcarchives.duke.edu/staff-directory",
        "https://www.wyomingco.net/Directory.aspx",
        "https://www.washtenaw.org/Directory.aspx",
        "https://nu.outsystemsenterprise.com/FSD/",
        "https://www.grandcountyutah.net/Directory.aspx",
        "https://co.otero.nm.us/Directory.aspx",
        "https://sjson.edu/about-us/faculty-staff-directory/",
        "https://www.columbiaco.com/Directory.aspx",
        "https://orangecountync.gov/directory.aspx",
        "https://capemaycountynj.gov/Directory.aspx",
        "https://www.emoryhenry.edu/academics/school-health-sciences/directory/",
        "https://www.co.jackson.mi.us/Directory.aspx",
        "https://www.mcw.edu/departments/libraries/about-us/staff-directory",
        "https://www.osfhealthcare.org/sfmccon/directory/",
        "https://www.snohd.org/directory.aspx",
        "https://giving.wakehealth.edu/stay-connected/contact-us",
        "https://www.shelbycountytn.gov/Directory.aspx",
        "https://campus.und.edu/directory/index.html",
        "https://www.dhd10.org/about-us/staff-directory/",
        "https://www.stmarys.ac.uk/staff-directory/our-staff.aspx",
        "https://www.stowe.co.uk/school/academic/staff-directory",
        "https://meded.ucsf.edu/about-us/our-people",
        "https://www.countyofnapa.org/Directory.aspx",
        "https://www.desotocountyms.gov/directory.aspx",
        "https://www.mha.org/about/board-of-trustees/",
        "https://www.plymouth.ac.uk/schools/peninsula-school-of-dentistry/peninsula-school-of-dentistry-staff-directory",
        "https://www.nmb.us/Directory.aspx",
        "https://www.leegov.com/Staff/directory?dept=all",
        "https://www.lrhc.org/provider-directory/",
        "https://www.shreveportla.gov/directory.aspx",
        "https://www.osfhealthcare.org/sfmccon/directory/staff/",
        "https://www.osfhealthcare.org/sfmccon/directory/faculty/",
        "https://louisville.edu/campushealth/about-us/staff-directory",
        "https://hca.wv.gov/Pages/Directory.aspx",
        "https://www.boisestate.edu/spph/faculty-and-staff-directory/",
        "https://www.jeffersoncountyny.gov/departments/Officefortheaging/StaffDirectory",
        "https://www.ncha.org/about-us/staff-directory/",
        "https://www.maine.gov/pfr/insurance/about/staff-directory",
        "https://www.co.lucas.oh.us/directory.aspx",
        "https://www.cmsdocs.org/about-us/staff-directory",
        "https://www.lvhn.org/doctors",
        "https://nychealthandhospitals-appservice-test.azurewebsites.net/simulationcenter/staff/",
        "https://www.carteretcountync.gov/Directory.aspx?did=27",
        "https://www.carteretcountync.gov/193/Board-of-Commissioners",
        "https://www.eastalabamahealth.org/careers-and-resources/education-and-training/staff-directory",
        "https://africacdc.org/staff-directory/",
        "https://hobi.med.ufl.edu/about/staff-directory/",
        "https://www.kumc.edu/enterprise-analytics/about/staff-directory.html",
        "https://hr.uconn.edu/staff-directory/",
        "https://ph.ucla.edu/about/faculty-staff-directory?type=all&page=1",
        "https://library.mednet.iu.edu/people/staff-directory.html",
        "https://www.mclennan.gov/1152/Staff-Directory",
        "https://www.nhcgov.com/Directory.aspx?did=88",
        "https://doctorsns.com/contact-us/staff-directory",
        "https://medicine.uiowa.edu/md/contact-us/faculty-and-staff-directory",
        "https://www.tuftsctsi.org/staff-directory/",
        "https://www.sa.gov/Directory/Departments/SAMHD/About/Staff-Directory",
        "https://med.umn.edu/dom/education/global-medicine/faculty-directory",
        "https://www.dconc.gov/about-dco/contact-us/employee-directory",
        "https://cityofenglewood.org/Directory.aspx?DID=14",
        "https://dbh.dc.gov/page/saint-elizabeths-hospital-staff-directory",
        "https://healthcenter.uga.edu/staff-directory/",
        "https://snohomishcountywa.gov/directory.aspx",
        "https://sc.edu/study/colleges_schools/public_health/faculty-staff/",
        "https://nabip.org/who-we-are/our-staff/",
        "https://www.acf.hhs.gov/omb/staff-directory",
        "https://www.researchgate.net/institution/Tulane_University",
        "https://culturalheritage-architecture-staff.list.directories.nyu.edu/"
    ]

def scrape_data(urls):
    for url in urls:
        data = {}

        driver = initialize_driver()
        driver.get(url)
        time.sleep(3)

        try:
            data["Domain"] = urlparse(url).netloc.split("www.")[-1]
            data["Title"] = driver.title
            data["Description"] = get_description(driver)
            data["LinkedIn URL"] = find_linkedin_on_website(driver)
            data["MX Records"], data["Mail Provider"], data["Mail Status"] = get_mx_records(urlparse(url).netloc)

            accept_cookies(driver)
            scroll_to_bottom(driver)

            relevant_pages = find_relevant_pages(driver)
            pagination_content_data = scrape_pagination(driver)
            if driver.current_url in relevant_pages:
                relevant_pages.remove(driver.current_url)

            data['Pagination Content Data'] = pagination_content_data
            save_data(data, pagination_content_data)

            for page in relevant_pages:
                data = {}
                data["Domain"] = urlparse(url).netloc.split("www.")[-1]
                data['url'] = page
                driver.get(page)
                time.sleep(3)
                scroll_to_bottom(driver)

                pagination_content_data = scrape_pagination(driver)

                data['Pagination Content Data'] = pagination_content_data
                save_data(data)

        except Exception as e:
            print(f"Error scraping {url}: {e}")
        finally:
            time.sleep(3)
            driver.quit()

scrape_data(urls)


# for url in urls:
#     data = {}
    
#     driver = initialize_driver()
#     driver.get(url)
#     time.sleep(3)

#     data["Domain"] = urlparse(url).netloc.split("www.")[-1]
#     data["Title"] = driver.title
#     data["Description"] = get_description(driver)
#     data["LinkedIn URL"] = find_linkedin_on_website(driver)
#     data["MX Records"], data["Mail Provider"], data["Mail Status"] = get_mx_records(urlparse(url).netloc)

#     accept_cookies(driver)
#     scroll_to_bottom(driver)
#     relevant_pages = find_relevant_pages(driver).append(url)
#     relevant_pages = list(set(relevant_pages))

#     for page in relevant_pages:
#         if driver.current_url in relevant_pages:
#             relevant_pages.pop(driver.current_url)
#             pagination_content_data = scrape_pagination(driver)

#     data['Pagination Content Data'] = pagination_content_data
#     save_data(data, pagination_content_data)

#     time.sleep(3)
#     driver.quit()
