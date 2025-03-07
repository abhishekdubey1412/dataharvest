import time
import uuid
import random
import undetected_chromedriver as uc

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/134.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.1770.50"
    ]
    return random.choice(user_agents)

def initialize_browser(headless=False):
    session_id = str(uuid.uuid4())
    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={get_random_user_agent()}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    if headless:
        options.add_argument("--headless=new")

    driver = uc.Chrome(options=options, headless=headless, version_main=134, keep_alive=True)

    time.sleep(random.uniform(1, 3))

    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
        Object.defineProperty(navigator, 'vendor', {get: () => 'Google Inc.'});
        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
    """)

    driver.set_window_size(1920, 1080)
    driver.set_window_position(random.randint(0, 100), random.randint(0, 100))

    result = driver.execute_script("return navigator.webdriver")
    if result is None:
        print(f"[{session_id}] Stealth mode applied successfully!")
    else:
        print(f"[{session_id}] Warning: navigator.webdriver still detectable!")

    return driver, session_id

def rotate_user_agent(driver, session_id):
    new_user_agent = get_random_user_agent()
    try:
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": new_user_agent})
        print(f"[{session_id}] User-Agent rotated to: {new_user_agent}")
    except Exception as e:
        print(f"[{session_id}] Failed to rotate User-Agent: {e}")