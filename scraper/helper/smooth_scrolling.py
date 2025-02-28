import random
from time import sleep

def smooth_scroll(driver):
    """
    Smoothly scrolls down a webpage with random pauses and step sizes to mimic human behavior.

    :param driver: Selenium WebDriver instance
    """
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    stagnant_count = 0

    while stagnant_count < 5:
        step = random.randint(100, 300)
        driver.execute_script(f"window.scrollBy(0, {step});")

        sleep(random.uniform(0.05, 0.2))

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        scroll_position = driver.execute_script("return window.scrollY + window.innerHeight")

        if scroll_position >= last_height:
            stagnant_count += 1
        else:
            stagnant_count = 0

        last_height = new_height

    print("Scrolling finished.")

def scroll_to_element(driver, element):
    """
    Scroll smoothly to a specific element on the page.

    :param driver: Selenium WebDriver instance
    :param element: Selenium WebElement to scroll to
    """
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    sleep(random.uniform(0.5, 0.8))