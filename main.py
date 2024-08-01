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
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
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
    time.sleep(4)
    
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
def perform_daily_activities():
    try:
        daily_activities = driver.find_elements(By.CLASS_NAME, 'mee-icon.mee-icon-AddMedium')

        for activity in daily_activities:
            try:
                activity.click()
                time.sleep(2)  # Adjust timing as necessary
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print(f"Error performing activity: {e}")
                continue
    except Exception as e:
        print(f"Error finding activities: {e}")
def perform_daily_search(url):
        driver.get("https://rewards.bing.com/pointsbreakdown")
        time.sleep(4)
        driver.find_element(By.CLASS_NAME, 'ng-binding.ng-scope.c-hyperlink').click()
        time.sleep(4)
        # Fetch content from URL
        response = requests.get(url)

        # Split text into words (assuming one word per line)
        words = response.text.splitlines()

        # Randomize words for search
        random.shuffle(words)

        # Perform 40 searches
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(10)
        try:
            input_element = driver.find_element(By.ID, "id_a")
            input_element.click()
            time.sleep(5)

            try:
                sign_in_element = driver.find_element(By.CLASS_NAME, "id_text_signin")
                sign_in_element.click()
            except Exception as e:
                print(f"Error performing activity: {e}")
        except Exception as e:
            print(f"Error finding activities: {e}")
        for query in words[:40]:
            search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'q')))
            search_box.clear()  # Clear any previous text in the search box
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(random.uniform(8,12))  # Wait for search results to load
def logout_of_microsoft():
    driver.get("https://account.microsoft.com/")
    time.sleep(2)
    
    # Open the user account menu
    user_menu_button = driver.find_element(By.ID, 'mectrl_headerPicture')
    user_menu_button.click()
    time.sleep(2)
    
    # Click on the sign-out button
    sign_out_button = driver.find_element(By.ID, 'mectrl_body_signOut')
    sign_out_button.click()
    time.sleep(5)
# Replace these with your Microsoft account email and password
email = "youraccount@gmail.com"
password = "yourpassword"


# Login and perform daily sets
login_to_microsoft(email, password)
perform_daily_sets()
perform_daily_activities()
perform_daily_search("https://raw.githubusercontent.com/marvel-jo/Rewards-search-automator/main/words.txt")
# logout_of_microsoft()
# Close the driver
driver.quit()
