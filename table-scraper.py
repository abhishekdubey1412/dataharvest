import os
import re
import time
import json
import random
import requests
import dns.resolver
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

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

def smooth_scroll_to_bottom(driver, max_wait=10):
    start_time = time.time()
    
    while True:
        current_position = driver.execute_script("return window.scrollY")
        
        scroll_step = random.randint(50, 150)
        driver.execute_script(f"window.scrollBy(0, {scroll_step});")
        
        time.sleep(random.uniform(0.05, 0.2))  

        new_position = driver.execute_script("return window.scrollY")
        
        if new_position == current_position or time.time() - start_time > max_wait:
            break  

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Common Data Collection
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

def extract_contact_info(driver):
    contact_info = {"emails": [], "phone_numbers": [], "social_links": []}
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    header_footer = soup.find_all(["header", "footer", "aside"])
    
    for section in header_footer:
        text = section.get_text(" ", strip=True)
        
        contact_info["emails"].extend(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text))
        contact_info["phone_numbers"].extend(re.findall(r"\+?\d{1,4}[\s-]?\(?\d{2,5}\)?[\s-]?\d{2,5}[\s-]?\d{2,5}", text))

        for a in section.find_all("a", href=True):
            href = a["href"]
            
            if any(social in href for social in ["facebook.com", "twitter.com", "linkedin.com", "instagram.com", "x.com"]):
                contact_info["social_links"].append(href)
            
            if href.startswith("mailto:"):
                email = href.split("mailto:")[1].split("?")[0]
                contact_info["emails"].append(email)
            
            if href.startswith("tel:"):
                phone_number = href.split("tel:")[1].split("?")[0]
                contact_info["phone_numbers"].append(phone_number)

    return {key: list(set(value)) for key, value in contact_info.items()}


# Main and Table Data Collection
def get_cleaned_content(soup):
    body = soup.find("body")
    soup = BeautifulSoup(str(body), 'html.parser')

    tags_to_remove = [
        "header", "footer", "script", "style", "noscript", "nav", "iframe", 
        "input", "svg", "aside", "button", "link", "meta", "picture", 
        "source", "object", "embed", "param", "canvas", "map", "area"
    ]

    for tags in tags_to_remove:
        for tag in soup.find_all(tags):
            tag.decompose()
    
    for pagination in soup.find_all(class_=lambda x: x is not None and isinstance(x, str) and "pagination" in x.lower()):
        pagination.decompose()

    for tag in soup.find_all(True):
        if tag.text == "" or tag.text ==  None:
            tag.decompose()
    
    for tag in soup.find_all(True):
        for attribute in ['onload', 'onclick']:
            del tag[attribute]

    return soup

def extract_tables_from_soup(soup):
    tables = soup.find_all("table")
    all_table_data = {}

    for index, table in enumerate(tables):
        rows = []
        headers = []

        header_row = table.find("tr")
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]

        for row in table.find_all("tr")[1:]:
            cols = [col.get_text(strip=True) for col in row.find_all(["td", "th"])]
            if cols:
                rows.append(cols)

        table_dicts = []
        if headers and rows:
            for row in rows:
                if len(row) == len(headers):
                    table_dicts.append(dict(zip(headers, row)))
            all_table_data[f"table_{index+1}"] = table_dicts
        else:
            all_table_data[f"table_{index+1}"] = rows
        
        table.decompose()
    
    return all_table_data, soup

def get_all_table_data(driver):
    all_data = {}

    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_table_data, main_soup = extract_tables_from_soup(soup)
    all_data.update(all_table_data)

    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for index, iframe in enumerate(iframes):
        driver.switch_to.frame(iframe)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        iframe_table_data, iframe_soup = extract_tables_from_soup(soup)
        all_data.update({f"iframe_{index+1}": iframe_table_data})

        iframe_soup = get_cleaned_content(iframe_soup)

        body_tag = iframe_soup.find('body')
        if body_tag:
            for child in body_tag.find_all(recursive=False):
                style = child.get('style', '')
                if 'display: none' in style or 'visibility: hidden' in style:
                    child.decompose()
            
            body_text = body_tag.get_text(strip=True)
            if body_text:
                all_data[f'iframe_{index+1}_body_content'] = body_text

        driver.switch_to.default_content()

    main_soup = get_cleaned_content(main_soup)
    if main_soup.text.strip():
        body_tag = main_soup.find('body')
        if body_tag:
            for child in body_tag.find_all(recursive=False):
                style = child.get('style', '')
                if 'display: none' in style or 'visibility: hidden' in style:
                    child.decompose()

            main_body_text = body_tag.get_text(strip=True)
            if main_body_text:
                all_data['main_body_content'] = main_body_text

    all_data = {k: v for k, v in all_data.items() if v}

    return all_data

# Save Data in JSON Fille
def save_data_to_json(table_data=None, social_data=None, company_data=None, url=None):
    domain = company_data.get("Domain") if company_data else None

    if domain:
        filename = f"{domain}.json"
    else:
        filename = f"{urlparse(url).netloc.split('www.')[-1]}.json"
    
    data = {
        "Data": [
            {"tables": {"main_body_content": table_data}} if table_data else {}
        ],
        "social_data": social_data or [],
        "company_data": company_data or [],
    }
    
    try:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
            
            if table_data is not None:
                existing_data["Data"].append({"tables": {"main_body_content": table_data}})
            
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(existing_data, f, indent=4, ensure_ascii=False)
        else:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
    except:
        print(table_data, social_data, company_data, url)

def scrape_pagination(driver):
    find_locator = None
    pagination_detected = False

    locators = [
        (By.CSS_SELECTOR, 'a[rel="next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[contains(translate(@aria-label, "NEXT", "next"), "next")]'), (By.CSS_SELECTOR, 'a[data-action="next"]'),
        (By.CSS_SELECTOR, 'a.next'), (By.CSS_SELECTOR, 'button.next'), (By.XPATH, '//a[contains(@class, "next")]'), (By.XPATH, '//a[normalize-space(translate(text(), "NEXT", "next")) = "next"]'),
        (By.XPATH, '//a[contains(translate(text(), "NEXT", "next"), "next")]'), (By.LINK_TEXT, "Next"), (By.XPATH, '//div[@class="pagination"]//a[text()="Next"]'), 
        (By.XPATH, '//a[text()="Previous"]/following-sibling::a'), (By.CSS_SELECTOR, 'ul.pagination a:last-child'), (By.CSS_SELECTOR, 'a[href*="next"]'), 
        (By.XPATH, '//a[contains(@href, "page")]'), (By.XPATH, "//a[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'next']"), 
        (By.LINK_TEXT, "next"), (By.XPATH, '//a[contains(text(), "Next")]'), (By.XPATH, "//a[contains(translate(text(), 'OLDER', 'older'), 'older')]")
    ]

    excluded_extensions = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}
    current_domain = urlparse(driver.current_url).netloc.split("www.")[-1].lower()

    while True:
        try:
            smooth_scroll_to_bottom(driver)
            next_button = None

            if not find_locator:
                for locator in locators:
                    try:
                        next_button = driver.find_element(*locator)
                        if next_button:
                            href = next_button.get_attribute('href')

                            if href and (
                                urlparse(href).netloc.split("www.")[-1].lower() != current_domain
                                or any(href.lower().endswith(ext) for ext in excluded_extensions)
                            ):
                                continue

                            find_locator = locator
                            break
                    except NoSuchElementException:
                        continue
            else:
                try:
                    next_button = driver.find_element(*find_locator)
                    if next_button:
                        href = next_button.get_attribute('href')

                        if href and (
                            urlparse(href).netloc.split("www.")[-1].lower() != current_domain
                            or any(href.lower().endswith(ext) for ext in excluded_extensions)
                        ):
                            break
                except NoSuchElementException:
                    break

            if next_button:
                pagination_detected = True

            if pagination_detected:
                table_data = get_all_table_data(driver)
                save_data_to_json(table_data=table_data, url=driver.current_url)

            # driver.execute_script("""
            #     ['header', 'footer'].forEach(tag => {
            #         document.querySelectorAll(tag).forEach(el => el.remove());
            #     });
            # """)

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
                    next_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable(*locator)
                    )
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_button)
                    ActionChains(driver).move_to_element(next_button).click().perform()
                    time.sleep(1.5)
                except:
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(1.5)

        except Exception as e:
            print(f"Pagination Error: {e}")
            break
    
    if not pagination_detected:
        table_data = get_all_table_data(driver)
        save_data_to_json(table_data=table_data, url=driver.current_url)
    
    return pagination_detected

urls = [
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
    "https://med.umn.edu/dom/education/global-medicine/faculty-directory?page=0",
    "https://www.dconc.gov/about-dco/contact-us/employee-directory",
    "https://cityofenglewood.org/Directory.aspx?DID=14",
    "https://dbh.dc.gov/page/saint-elizabeths-hospital-staff-directory",
    "https://healthcenter.uga.edu/staff-directory/",
    "https://snohomishcountywa.gov/directory.aspx",
    "https://sc.edu/study/colleges_schools/public_health/faculty-staff/",
    "https://nabip.org/who-we-are/staff-directory",
    "https://nabip.org/who-we-are/board-of-trustees",
    "https://www.easternahec.net/about-us-2/staff-directory/",
    "https://osteopathicmedicine.msu.edu/info/faculty-staff-directory",
    "https://lluh.org/patients-visitors/visitors/security-services/staff-directory#",
    "https://hsc.unm.edu/about/finance/sponsored-projects/about/staff-directory.html",
    "https://www.co.sauk.wi.us/publichealth/staff-directory",
    "https://libguides.uams.edu/faculty-staff",
    "https://www.redmond.gov/directory.aspx",
    "https://www.amtnyc.org/staff-directory",
    "https://nam.edu/staff-directory/",
    "https://nashuanh.gov/Directory.aspx?did=39",
    "https://www.urmc.rochester.edu/libraries/miner/about/staffdirectory",
    "https://www.ouhealth.com/oklahoma-center-for-geroscience/healthy-aging-services/oklahoma-healthy-aging-initiative-ohai-/staff-directory/",
    "https://guides.library.nymc.edu/HSLStaffDirectory",
    "https://iroquois.org/staff-directory/",
    "https://camosun.ca/programs-courses/school-health-and-human-services/hhs-faculty-staff-directory",
    "https://www.hpae.org/our-union/state-officers-and-staff-directory/",
    "https://nursing.gwu.edu/staff-directory",
    "https://health.mil/About-MHS/Contact-Us/Directory",
    "https://www.msm.edu/Research/research_centersandinstitutes/NCPC/divisions/substance/staff.php",
    "https://library.aah.org/prf.php",
    "https://medicine.wsu.edu/directory/",
    "https://med.virginia.edu/phs/office-of-the-chair/faculty-and-staff-directory/",
    "https://dlmp.uw.edu/staff/staff-directory",
    "https://health.usf.edu/nursing/faculty-staff/directory",
    "https://publichealth.gsu.edu/directory/",
    "https://www.jacksonphysiciansearch.com/about/team/",
    "https://www.ahrq.gov/funding/priorities-contacts/contacts/index.html",
    "https://www.stanfordchildrens.org/en/mss/aboutus/staffdirectory.html",
    "https://www.utmb.edu/hec/about-us/staff-directory",
    "https://sph.rutgers.edu/directory",
    "https://medicine.wright.edu/population-and-public-health-sciences/faculty-and-staff-directory",
    "https://research.luriechildrens.org/en/research-resources/research-administration-staff-directory/",
    "https://www.shu.ac.uk/about-us/our-people/staff-profiles",
    "https://www.nursing.emory.edu/faculty-and-staff-directory",
    "https://www.city.ac.uk/about/find-contact/staff-directory",
    "https://shhs.indianapolis.iu.edu/connect/directory/index.html",
    "https://nursing.duke.edu/centers-and-institutes/center-nursing-discovery/cnd-team-directory",
    "https://www.fammed.wisc.edu/directory/?cf-first-name=&cf-staff-type=Staff&cf-location=610+N+Whitney+Way+%28Madison%29",
    "https://www.sanjoseca.gov/your-government/departments-offices/housing/about-us/staff-directory",
    "https://www.hhs.gov/ohrp/about-ohrp/staff/index.html",
    "https://library.cuanschutz.edu/contact-the-library/staff-directory",
    "https://www.city.ac.uk/about/governance/executive-leadership",
    "https://www.qub.ac.uk/schools/psy/People/ProfessionalServicesStaff/",
    "https://umiamihealth.org/en/locations/uhealth-fitness-and-wellness-center/about-us/staff",
    "https://washu.edu/about-washu/university-leadership/university-council/",
    "https://www.ashland.edu/faculty-directory?page=3",
    "https://www.ashe.org/about/staff-1",
    "https://quantum-health.com/people/",
    "https://deptmedicine.arizona.edu/directory-staff",
    "https://www.haponline.org/About-HAP/Staff-Directory",
    "https://giving.unc.edu/who-we-are/staff-directory/",
    "https://www.massmed.org/About/MMS-Staff-Directory/#counsel",
    "https://www.ouh.nhs.uk/services/referrals/contacts.aspx",
    "https://www.uhdb.nhs.uk/consultant-directory/",
    "https://humanresources.uchicago.edu/department/contact/staff.shtml",
    "https://nastad.org/staff",
    "https://www.uic.edu/apps/departments-az/search?dispatch=find&orgid=99525",
    "https://www.sickkids.ca/en/directory/",
    "https://www.annapolis.gov/directory.aspx",
    "https://www.ntu.ac.uk/about-us/staff-directory?&&start_rank=23",
    "https://www.chesterfieldroyal.nhs.uk/about-us/our-board-directors/our-board-directors",
    "https://medschool.ucr.edu/directory",
    "https://www.harford.edu/about/get-to-know-harford/faculty-staff-directory/index.php",
    "https://ohsufoundation.org/staff-directory/",
    "https://www.homerton.nhs.uk/consultant-directory/",
    "https://www.nursing.umaryland.edu/directory/",
    "https://www.regiscollege.edu/about-regis/find-us/faculty-and-staff-directory",
    "https://www.feinberg.northwestern.edu/about/contact/directory.html",
    "https://nursing.ufl.edu/faculty/staff/",
    "https://www.qub.ac.uk/contact/Staff-directory/",
    "https://www.roosevelt.edu/contact/directory?page=0",
    "https://www.hyms.ac.uk/about/our-people",
    "https://facultydirectory.uchc.edu/",
    "https://directory.mt.gov/govt/state-dir/agency/dphhs",
    "https://www.salford.ac.uk/our-staff",
    "https://ung.edu/directory/",
    "https://lcmedsociety.com/page/StaffMembers",
    "https://health.wyo.gov/wp-content/uploads/2024/12/Copy-of-2024-2025-Facility-Directory-1.pdf",
    "https://www.chestercountyhospital.org/-/media/documents%20and%20audio/chestercounty/2023cchmedstaffdirectory.ashx?la=en",
    "https://www.floridahealth.gov/provider-and-partner-resources/volunteer-health-services-opportunities/staff-directory.html",
    "https://www.elcaminohealth.org/sites/default/files/2023-11/lg-medical-staff-roster-nov23.pdf",
    "https://2017-2021.commerce.gov/sites/default/files/2018-11/ohrm-staff-directory-7-10-18.pdf",
    "https://www.ncdhhs.gov/office-rural-health-staff-directory/open",
    "https://www.sarahbush.org/media/filer_public/ed/83/ed83567f-db2c-494a-b467-d731a3027fdb/med_staff_directory_2024.pdf",
    "https://www.aha.org/system/files/media/file/2023/02/AHA-IFDHE-Leadership-Council-2023.pdf",
    "https://www.ache.org/-/media/ache/membership/healthcare-consultants-forum/hcf-directory-2024.pdf",
    "https://hscrc.maryland.gov/Pages/staff.aspx",
    "https://hsl.med.nyu.edu/about-us/staff",
    "https://thebrooklynhealthhome.org/about-us/",
    "https://grhhn.org/who-we-are/",
    "https://ogletree.com/insights-resources/webinars/2024-04-29/understanding-the-dols-new-overtime-rule-and-the-increased-salary-thresholds-for-flsa-exempt-employees/",
    "https://ogletree.com/people/?_gl=1*1hsd2j9*_up*MQ..*_ga*MjA0OTQxNTQ5MS4xNzM1ODk3NDM3*_ga_V4WT9JNBFT*MTczNTg5NzQzNi4xLjAuMTczNTg5NzQzNi4wLjAuMA..",
    "https://www.royalfree.nhs.uk/our-locations/find-ward?keywords=&letter=A#ward-list",
    "https://www.mater.ie/consultants/index.xml?submitted=1&page=3&consultant-search-text=",
    "https://sc.edu/study/colleges_schools/medicine/about_the_school/faculty-staff/index.php",
    "https://goduke.com/staff-directory",
    "https://ncmedsoc.org/about-us/ncms-staff/",
    "https://aspph.org/about/staff-directory/",
    "https://texastech.com/staff-directory",
    "https://jjc.edu/directory",
    "https://www.mhanet.org/Web/Online/About/Staff.aspx?hkey=b219d8f5-dd46-44c7-aea3-5b946133c902",
    "https://www.healthmanagement.com/our-team/staff-directory/",
    "https://mmhpi.org/about/our-team/function-senior-leadership/",
    "https://www.tfhd.com/staff-directory",
    "https://www.jefferson.edu/academics/colleges-schools-institutes/health-professions/faculty.html",
    "https://www.aaap.org/about/staff/",
    "https://maternalhealthlearning.org/wp-content/uploads/2020/09/September-LI-Biosketches_Final.pdf",
    "https://hancockdaniel.com/attorneys/",
    "https://www.waveny.org/board-leadership/",
    "https://health.uconn.edu/about/leadership",
    "https://www1.villanova.edu/university/student-life/staff.html",
    "https://health.maryland.gov/phpa/cancer/SiteAssets/Pages/2019cancerconference/Attendee%20List.pdf",
    "https://www.kha-net.org/AlliedOrganizations/KONL/KONLDocuments/d162142.aspx?type=view",
    "https://medicine.temple.edu/about/leadership",
    "https://sc.edu/study/colleges_schools/public_health/faculty-staff/",
    "https://askphc.com/our-people/",
    "https://nursing.jhu.edu/faculty-research/faculty/directory/",
    "https://nursing.msu.edu/about-us/faculty-staff-directory",
    "https://www.nursing.psu.edu/directory/",
    "https://firststephome.org/management-team",
    "https://www.healthmanagement.com/about/",
    "https://www.aapc.com/training-and-events/docucon-speakers",
    "https://health.usf.edu/VP/leadership",
    "https://www.namss.org/About/Volunteer-Leaders-Staff",
    "https://experiencenewton.chambermaster.com/list/ql/health-care-11"
]

for url in urls:
    excluded_extensions = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}
    if not any(url.lower().endswith(ext) for ext in excluded_extensions):
        response = requests.get(url)
        if response.status_code == 200:
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            driver.maximize_window()
            time.sleep(3)

            accept_cookies(driver)
            smooth_scroll_to_bottom(driver)

            social_data = extract_contact_info(driver)
            mx_records, mail_provider, mail_status = get_mx_records(urlparse(url).netloc)
            company_data = {
                "Domain": urlparse(url).netloc.split("www.")[-1],
                "Title": driver.title,
                "Description": get_description(driver),
                "MX Records": mx_records,
                "Mail Provider": mail_provider,
                "Mail Status": mail_status
            }

            save_data_to_json(social_data=social_data, company_data=company_data)

            pagination = scrape_pagination(driver)
            if driver and not pagination:
                iframes = driver.find_elements(By.TAG_NAME, 'iframe')
                for iframe in iframes:
                    driver.switch_to.frame(iframe)
                    body_text = driver.find_element(By.TAG_NAME, 'body').text.strip()
                    if body_text:
                        scrape_pagination(driver)
                    driver.switch_to.default_content()

            driver.quit()