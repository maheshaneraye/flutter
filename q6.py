from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open https://www.google.com/ in Chrome
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# 2. Maximize the browser window
driver.maximize_window()
time.sleep(2)

# 3. Locate the Google logo
try:
    logo = driver.find_element(By.XPATH, "//*[@alt='Google' or @aria-label='Google' or @class='lnXbf']")
except Exception:
    logo = driver.find_element(By.TAG_NAME, "img")

# 4. Retrieve its X, Y, width, and height
x = logo.location['x']
y = logo.location['y']
width = logo.size['width']
height = logo.size['height']

# 5. Take a screenshot of the browser
screenshot_path = "google_screenshot.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved as {screenshot_path}")

# 6. Check whether the Google logo is displayed
# 7. If displayed, print "Google logo found" along with its location and size
# 8. Otherwise, print "Google logo not found"
if logo.is_displayed():
    print(f"Google logo found. Location: ({x}, {y}), Size: {width}x{height}")
else:
    print("Google logo not found")

time.sleep(2)
driver.quit()
