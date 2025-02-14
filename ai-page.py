import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from stable_baselines3 import PPO
import gym
from gym import spaces
import numpy as np

# Define URLs to scrape
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

# Reinforcement Learning Environment
class PaginationEnv(gym.Env):
    def __init__(self, driver):
        super(PaginationEnv, self).__init__()
        self.driver = driver
        self.action_space = spaces.Discrete(3)  # Actions: 0 = Click Next, 1 = Scroll, 2 = Stop
        self.observation_space = spaces.Box(low=0, high=1, shape=(1,), dtype=np.float32)

    def step(self, action):
        try:
            if action == 0:  # Click 'Next' button
                next_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
                next_button.click()
                time.sleep(2)
            elif action == 1:  # Scroll down
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
                time.sleep(2)
            elif action == 2:  # Stop
                return np.array([0]), 0, True, {}
            
            return np.array([1]), 1, False, {}
        except (NoSuchElementException, TimeoutException):
            return np.array([0]), -1, True, {}

    def reset(self):
        return np.array([1])

# Start undetected Chrome driver
def get_stealth_driver():
    options = uc.ChromeOptions()
    options.headless = True
    driver = uc.Chrome(options=options)
    return driver

def scrape(url):
    driver = get_stealth_driver()
    driver.get(url)
    time.sleep(3)
    
    env = PaginationEnv(driver)
    model = PPO("MlpPolicy", env, verbose=0)
    
    obs = env.reset()
    done = False
    while not done:
        action, _ = model.predict(obs)
        obs, _, done, _ = env.step(action)
    
    page_source = driver.page_source
    driver.quit()
    return page_source

# Run scraper on all URLs
for url in urls:
    html = scrape(url)
    with open(f"output_{random.randint(1000, 9999)}.html", "w", encoding="utf-8") as f:
        f.write(html)