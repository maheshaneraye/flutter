from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Open https://www.facebook.com/ in Chrome & Maximize window
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(2)

# 2. Find the Facebook logo and fetch its location and size
logo = driver.find_element(By.CSS_SELECTOR, "img")
print("Facebook Logo Location:", logo.location)
print("Facebook Logo Size:", logo.size)

# 3. Check whether the logo is displayed and enabled
is_displayed = logo.is_displayed()
is_enabled = logo.is_enabled()
print(f"Is Displayed: {is_displayed}, Is Enabled: {is_enabled}")

# 4. If the logo is clickable, click it; otherwise, enter "Logo not clickable" in email textbox
if is_displayed and is_enabled:
    try:
        logo.click()
        print("Facebook logo clicked successfully.")
    except Exception:
        email_box = driver.find_element(By.ID, "email")
        email_box.send_keys("Logo not clickable")
        print("Logo could not be clicked, entered 'Logo not clickable' in email textbox.")
else:
    email_box = driver.find_element(By.ID, "email")
    email_box.send_keys("Logo not clickable")
    print("Logo not clickable, entered 'Logo not clickable' in email textbox.")

time.sleep(2)
driver.quit()
