import time
from selenium.webdriver.common.by import By
from scraper.helper.cookie_handler import manage_cookies
from scraper.helper.smooth_scrolling import smooth_scroll
from scraper.extracted_data.domain_data import DomainData
from scraper.helper.browser_initializer import initialize_browser
from scraper.extracted_data.structured_data_extractor import DataExtracted
from scraper.helper.pagination_detector import detect_pagination, start_pagination

def main(browser):
    manage_cookies(browser)
    smooth_scroll(browser)

    locator = detect_pagination(browser)
    if not locator:     
        iframes = browser.find_elements(By.TAG_NAME, "iframe")

        for index, iframe in enumerate(iframes):
            try:
                browser.switch_to.frame(iframe)
                print(f"switched to iframe {index + 1}")
                iframe_text = browser.find_element(By.TAG_NAME, "body").text.strip()

                if iframe_text:
                    iframe_locator = detect_pagination(browser)
                    if not iframe_locator:
                        browser.switch_to.default_content()
                        continue
                    
                    start_pagination(browser, iframe_locator)

                browser.switch_to.default_content()

            except Exception as e:
                print(f"Error switching to iframe {index + 1}: {e}")

    else:
        start_pagination(browser, locator)

def run_scraping(url, website_id, headless=False):
    """Initializes the browser, extracts data, and returns the result."""
    browser, session_id = initialize_browser(headless=headless)
    
    try:
        browser.get(url)
        time.sleep(2)
        manage_cookies(browser)
        smooth_scroll(browser)
        
        DomainData.extract_data(browser, website_id)
        DataExtracted.extract_data(browser)

    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")

    finally:
        if browser:
            try:
                browser.quit()
            except Exception:
                pass

# if __name__ == "__main__":
#     browser, session_id = initialize_browser()
#     urls = filter_urls(urls)
#     for url in urls:       
#         browser.get(url)
#         extract_data(browser)
#         
#         rotate_user_agent(browser, session_id) 
#     browser.quit()

    
# urls = [
#     "https://www.wbs.ac.uk/about/people/",
#     "https://tpchd.org/info/staff-directory/",
#     "https://www.eversana.com/thought-leaders/",
#     "https://www.health.columbia.edu/directory",
#     "https://www.nnlm.gov/about/staff-directory",
#     "https://meded.ucsf.edu/about-us/our-people",
#     "https://www.ucb.ac.uk/about-us/staff-directory/",
#     "https://www.ruralhealth.us/about-us/staff-directory",
#     "https://datascience.cancer.gov/about/staff-directory",
#     "https://www.stowe.co.uk/school/academic/staff-directory",
#     "https://www.mdx.ac.uk/about-us/our-people/staff-directory/",
#     "https://www.dconc.gov/about-dco/contact-us/employee-directory",
#     "https://www.blythedale.org/about-the-hospital/staff-directory",
#     "https://www.marathoncounty.gov/about-us/staff-directory/-npage-5",
#     "https://ph.ucla.edu/about/faculty-staff-directory?type=all&page=1",
#     "https://www.researchgate.net/institution/Tulane-University/members",
#     "https://sc.edu/study/colleges_schools/public_health/faculty-staff/",
#     "https://med.umn.edu/dom/education/global-medicine/faculty-directory",
#     "https://www.emoryhenry.edu/academics/school-health-sciences/directory/",
#     "https://www.wlv.ac.uk/about-us/our-staff/?collection=wlv-web-our-staff&form=wlv-facet&query=&start_rank=21",
#     "https://www.homerton.nhs.uk/staff-directory/staff-directory?staffDirectory=true&searchTerm=&search=search&searchType=All"
# ]