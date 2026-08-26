from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open https://www.amazon.com/ in Chrome
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

# 2. Maximize the browser window
driver.maximize_window()
time.sleep(2)

# 3. Locate the Amazon search textbox
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# 4. Fetch the location and dimensions of the search textbox
print("Search Box Location:", search_box.location)
print("Search Box Dimensions (Size):", search_box.size)

# 5. Check whether the textbox is enabled
# 6. If enabled, enter "Selenium WebDriver" into it
# 7. Otherwise, print "Search box is disabled"
if search_box.is_enabled():
    search_box.send_keys("Selenium WebDriver")
    print("Search box is enabled. Entered 'Selenium WebDriver'.")
else:
    print("Search box is disabled")

time.sleep(2)
driver.quit()
