from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open "https://www.google.com/" in Chrome browser
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# 2. Make Chrome browser window in full screen mode
driver.fullscreen_window()
time.sleep(2)

# 3. Fetch the Google logo image's location on screen and its size using Selenium
try:
    logo = driver.find_element(By.XPATH, "//*[@alt='Google' or @aria-label='Google' or @class='lnXbf']")
except Exception:
    logo = driver.find_element(By.TAG_NAME, "img")

print("Google Logo Location:", logo.location)
print("Google Logo Size:", logo.size)

# 4. Check if this Google logo is clickable or not
# 5. If Google logo is clickable then click on it, else write "Not clickable" in the search textbox
if logo.is_displayed() and logo.is_enabled():
    try:
        logo.click()
        print("Google logo is clickable - clicked successfully.")
    except Exception:
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Not clickable")
        print("Entered 'Not clickable' in search textbox.")
else:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Not clickable")
    print("Entered 'Not clickable' in search textbox.")

time.sleep(2)
driver.quit()
