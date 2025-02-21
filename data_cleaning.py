from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium_stealth import stealth

# Set up Chrome options to use a custom user agent
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation flag
options.add_argument("--start-maximized")  # Maximize the browser window
options.add_argument("--disable-extensions")  # Disable browser extensions for more human-like behavior
options.add_argument("--disable-gpu")  # Disable GPU (useful for headless)
options.add_argument("--no-sandbox")  # Use with headless mode to avoid errors

# Initialize the ChromeDriver using the Service class
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Use selenium-stealth to apply anti-detection measures
stealth(driver,
        languages=["en-US", "en"],
        timezone="America/New_York",  # Set a realistic timezone
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        webgl_vendor="Intel Inc.",
        webgl_renderer="Intel Iris OpenGL Engine",
        navigator_platform="Win32",
        navigator_vendor="Google Inc.",
        fix_hairline=True)  # Helps with Canvas fingerprinting

# Open Gmail login page
driver.get('https://mail.google.com')

# Wait for the page to load
time.sleep(2)

# Add cookies to the browser
cookies = {
    'AEC': 'AVcja2eEWD00-LsURSG63-iQjXkwxIBB2dvWgcWuX4WNjJgTI0FAtejcGQ',
    'APISID': 'ySpUjZUGMPGbJddf/A_fjdWcCm0xGbM9sY',
    'COMPASS': 'appsfrontendserver=CgAQwP7MvQYaeAAJa4lX6H2wneR-Vc0U81BmQQVlGqKchAnMkccCiOuaQaHtQHta_hDFCcnLu9FVTFud0z8p5YfvRQjWa1RQ7xCao-kxzGDSjUqCYXneyG2LYiGQQMR0XwkU3gShVaD20RmKQYFB3W9gg-m2ZzkRgsa8I0Axiy4YmyABKoIBCAEQl_jMvQYaeAAJa4lX4Zxz3UM056FOvx_cwcpdzKibS0pOPIva3QueYLSynaO5Oqbx9VPq-oGykTEe6FWCmmSYmWVl_KKQA-s-Tz4JsBZmlJOqUJwX2bARzwZX3gy177N15UA-gWj7GwsG0jYtgiD99_EdxESNKoeo7kG2bAoD8zAB',
    'NID': '511=7qHlFgC-V2W_5XyPHEMplDEiUzTtvEkfd8rfOBO4sZV1kbv0xst0I8gGGmQ4gPQITVsbs0hyA8oTYhp4FwwBgn_Wyf6rD1mzgV6WxD07nIFZaPRhUQbOH_gnShxX_haxLPu0Kpbj9w0aaSllOPCnmYcmIcsGeCoxFGNC0i5nLk8YjXE3jgwWmGbVtbqT7V07P8Cr9h03Z9KnBmyF2yNw',
    'HSID': 'Ab4kJFXow1bGB0JbN',
    'SSID': 'AJFfoh7msZ5K-Vms5',
    'SID': 'yThplWztt8WJchGfzPOg1lUpDBL0D_wDCv4Q1HG9mKfFN2cY4jW5-dLwUwhgt52ch7Sfjw.',
    '1P_JAR': '2025-02-17-17',
    'SAPISID': 'ySpUjZUGMPGbJddf/A_fjdWcCm0xGbM9sY',
    'SIDCC': 'AJjdx8M28zHwmjz9tqkqxy04Fc9F0JvjjfOum2GlX_-j-QFw7mrjw9OwjJKmmlRxTQUyB2YdxHb7jOMrcWLGRMddGVg9htDa_H5cP-X7aZgU_21Olz4YqAvSXYJwCHpaDK9U4wH6FLFh4lgIUoCj9lqvw',
    'OTZ': '7497476_16_16__16_7497479_1:01064d380',
}

for cookie in cookies:
    driver.add_cookie({'name': cookie, 'value': cookies[cookie]})

# Refresh the page to login with the cookies
driver.refresh()

# Wait for the page to load and be logged in
time.sleep(5)

# You should be logged into Gmail at this point
print("Logged in successfully!")

# Close the browser after a delay (or do something else)
time.sleep(50)