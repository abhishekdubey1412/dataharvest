import time
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from scraper.helper.browser_initializer import rotate_user_agent
from selenium.webdriver.support import expected_conditions as EC
from scraper.extracted_data.structured_data_extractor import DataExtracted
from scraper.helper.smooth_scrolling import scroll_to_element, smooth_scroll

def is_pagination_present(driver, locator):
    """
    Check if the given pagination locator exists on the page.
    
    :param driver: Selenium WebDriver instance
    :param locator: Tuple containing By strategy and locator value
    :return: True if pagination element exists, otherwise False
    """
    try:
        element = driver.find_element(*locator)
        

        if not element or not element.is_displayed() or not element.is_enabled():
            return False

        if not element:
            return False

        if element.tag_name.lower() == 'a':
            href = element.get_attribute('href')
            
            prohibited_extensions = {".pdf", ".jpg", ".jpeg", ".png", ".gif", 
                                     ".svg", ".webp", ".zip", ".rar", ".mp4", ".mp3"}

            if href:
                if any(href.lower().endswith(ext) for ext in prohibited_extensions):
                    return False
                
                current_domain = urlparse(driver.current_url).netloc.replace("www.", "").strip().lower()
                href_domain = urlparse(href).netloc.replace("www.", "").strip().lower()

                if not href_domain:
                    return True
                elif href_domain == current_domain:
                    return "page" not in urlparse(href).path.lower()
                elif "page" in urlparse(href).query.lower():
                    return True
                elif href_domain != current_domain:
                    return False
        
        return True

    except Exception as e:
        return False
    
def detect_pagination(driver):
    """
    Detect pagination by checking a list of locators.
    
    :param driver: Selenium WebDriver instance
    :param locators: List of tuples containing By strategy and locator values
    :return: The first found locator if pagination exists, otherwise None
    """
    locators = [
        (By.CSS_SELECTOR, 'a[rel="next"]'), (By.XPATH, '//a[@rel="next"]'), (By.XPATH, '//a[contains(translate(@aria-label, "NEXT", "next"), "next")]'), (By.CSS_SELECTOR, 'a[data-action="next"]'),
        (By.CSS_SELECTOR, 'a.next'), (By.CSS_SELECTOR, 'button.next'), (By.XPATH, '//a[contains(@class, "next")]'), (By.XPATH, '//a[normalize-space(translate(text(), "NEXT", "next")) = "next"]'),
        (By.XPATH, '//a[contains(translate(text(), "NEXT", "next"), "next")]'), (By.LINK_TEXT, "Next"), (By.XPATH, '//div[@class="pagination"]//a[text()="Next"]'), 
        (By.XPATH, '//a[text()="Previous"]/following-sibling::a'), (By.CSS_SELECTOR, 'ul.pagination a:last-child'), (By.CSS_SELECTOR, 'a[href*="next"]'), 
        (By.XPATH, '//a[contains(@href, "page")]'), (By.XPATH, "//a[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = 'next']"), 
        (By.LINK_TEXT, "next"), (By.XPATH, '//a[contains(text(), "Next")]'), (By.XPATH, "//a[contains(translate(text(), 'OLDER', 'older'), 'older')]")
    ]

    for locator in locators:
        if is_pagination_present(driver, locator):
            return locator
        
    return False

def start_pagination(driver, session_id, locator, url_id):
    """
    Iterate through pagination until no next button is found.

    :param driver: Selenium WebDriver instance
    :param locator: Tuple containing By strategy and locator value
    """
    raw_data = []
    last_page_source = driver.find_element(By.TAG_NAME, "body").text.strip()
    
    while True:
        smooth_scroll(driver)
        raw_data.append(DataExtracted.extract_data(driver, url_id))

        try:
            next_button = driver.find_element(*locator)
        except:
            break

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
        
        try:
            scroll_to_element(driver, next_button)
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
            next_button.click()
            time.sleep(1.5)
        except Exception:
            try:
                next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(1.5)
            except Exception:
                break
        
        rotate_user_agent(driver, session_id)

        current_page_source = driver.find_element(By.TAG_NAME, "body").text.strip()
        if current_page_source == last_page_source:
            break

        last_page_source = current_page_source
    
    return raw_data