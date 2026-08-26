from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open https://www.youtube.com/ in Chrome
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

# 2. Make the browser full screen / maximized
driver.maximize_window()
time.sleep(3)

# 3. Locate the YouTube logo
logo = driver.find_element(By.XPATH, "//a[@id='logo']")

# 4. Retrieve its position and size
print("YouTube Logo Position (Location):", logo.location)
print("YouTube Logo Size:", logo.size)

# 5. Verify whether the logo is displayed
is_displayed = logo.is_displayed()
print("Is Logo Displayed:", is_displayed)

# 6. Check whether it is enabled / clickable
is_enabled = logo.is_enabled()
print("Is Logo Enabled:", is_enabled)

# 7. If clickable, click the logo; otherwise, print "YouTube logo is not clickable"
if is_displayed and is_enabled:
    try:
        logo.click()
        print("YouTube logo clicked successfully.")
    except Exception:
        print("YouTube logo is not clickable")
else:
    print("YouTube logo is not clickable")

time.sleep(2)
driver.quit()
