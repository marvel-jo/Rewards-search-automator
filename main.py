from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
import requests
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Setup WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to Bing
driver.get("https://www.bing.com/")

# Maximize browser window
driver.maximize_window()

# Function to login to Microsoft account
def login_to_microsoft(email, password):
    driver.get("https://login.live.com/")
    time.sleep(2)
    
    # Enter email
    email_input = driver.find_element(By.NAME, 'loginfmt')
    email_input.send_keys(email)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(2)
    
    # Enter password
    password_input = driver.find_element(By.NAME, 'passwd')
    password_input.send_keys(password)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(2)
    
    # Stay signed in? (Yes)
    driver.find_element(By.ID, 'acceptButton').click()
    time.sleep(2)

# Function to perform daily sets
def perform_daily_sets():
    driver.get("https://rewards.bing.com/")
    time.sleep(2)
    
    # Find all daily set links
    daily_set_links = driver.find_elements(By.CLASS_NAME, 'text-align-center.rewards-card-container.min-dimension')

    # Iterate through the first three elements or the number of elements found
    for i in range(min(3, len(daily_set_links))):
        link = daily_set_links[i]
        
        # Click on the daily set link
        link.click()
        
        # Wait for new tab to open and switch to it
        time.sleep(2)  # Adjust timing as necessary
        driver.switch_to.window(driver.window_handles[-1])
        
        # Perform actions on the new tab if needed
        # Example: Close the tab after interaction
        driver.close()
        
        # Switch back to the original tab
        driver.switch_to.window(driver.window_handles[0])
        
        # Wait briefly before proceeding to the next link
        time.sleep(2)
def perform_daily_search(url):
        driver.get("https://www.bing.com/")
        # Fetch content from URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Split text into words (assuming one word per line)
        words = response.text.splitlines()

        # Randomize words for search
        random.shuffle(words)

        # Perform 40 searches
        for query in words[:40]:
            search_box = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, 'q'))
            )
            search_box.clear()  # Clear any previous text in the search box
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)  # Wait for search results to load

# Replace these with your Microsoft account email and password
email = "your.email@gmail.com"
password = "yourpassword"


# Login and perform daily sets
login_to_microsoft(email, password)
perform_daily_sets()
perform_daily_search("https://raw.githubusercontent.com/marvel-jo/Rewards-search-automator/main/words.txt")
# Close the driver
driver.quit()
