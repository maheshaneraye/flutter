from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open Google Chrome and navigate to https://www.google.com/
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# 2. Locate the Google search textbox
search_box = driver.find_element(By.NAME, "q")

# 3. Retrieve the following properties: X coordinate & Y coordinate
x_coord = search_box.location['x']
y_coord = search_box.location['y']
print(f"X coordinate: {x_coord}")
print(f"Y coordinate: {y_coord}")

# 4. Check whether the textbox is displayed
is_displayed = search_box.is_displayed()
print(f"Is Displayed: {is_displayed}")

# 5. Check whether the textbox is enabled
is_enabled = search_box.is_enabled()
print(f"Is Enabled: {is_enabled}")

# 6. If enabled, enter "Selenium Automation" into the textbox
# 7. Otherwise, print "Search textbox is disabled"
if is_enabled:
    search_box.send_keys("Selenium Automation")
    print("Entered 'Selenium Automation' into the search textbox.")
else:
    print("Search textbox is disabled")

time.sleep(2)
driver.quit()
