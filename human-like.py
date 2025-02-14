import random
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def bezier_curve(p0, p1, p2, p3, n=20):
    """Generates n points along a cubic Bézier curve."""
    t_values = np.linspace(0, 1, n)
    curve = [(int((1-t)**3 * p0[0] + 3 * (1-t)**2 * t * p1[0] + 3 * (1-t) * t**2 * p2[0] + t**3 * p3[0]), 
              int((1-t)**3 * p0[1] + 3 * (1-t)**2 * t * p1[1] + 3 * (1-t) * t**2 * p2[1] + t**3 * p3[1])) 
             for t in t_values]
    return curve

def random_sleep(min_t=0.01, max_t=0.03):
    """Random sleep for a human-like delay."""
    time.sleep(random.uniform(min_t, max_t))

def simulate_snake_like_mouse_move(driver):
    """Moves the mouse in a snake-like (curved) path within safe viewport bounds."""
    window = driver.get_window_rect()
    width, height = window["width"], window["height"]

    # Define safe movement area (avoiding edges)
    safe_margin = 50  
    start = (random.randint(safe_margin, width // 4), random.randint(safe_margin, height // 4))
    end = (random.randint(width // 2, width - safe_margin), random.randint(height // 2, height - safe_margin))

    # Control points for smooth curve
    mid1 = (random.randint(start[0] + 50, end[0] - 50), random.randint(start[1], end[1] // 2))
    mid2 = (random.randint(start[0], end[0]), random.randint(end[1] // 2, end[1]))

    path = bezier_curve(start, mid1, mid2, end, n=30)

    # Move mouse from start position (avoiding relative out-of-bounds errors)
    action = ActionChains(driver)
    action.move_by_offset(start[0], start[1]).perform()
    
    for i in range(1, len(path)):
        x_offset = path[i][0] - path[i-1][0]
        y_offset = path[i][1] - path[i-1][1]

        # Prevent moving outside viewport
        if 0 <= path[i][0] <= width and 0 <= path[i][1] <= height:
            action.move_by_offset(x_offset, y_offset).perform()
            random_sleep(0.02, 0.06)

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

driver = initialize_driver()
driver.get("https://aabhyasa.com/")

time.sleep(3)
simulate_snake_like_mouse_move(driver)
time.sleep(2)

driver.quit()
