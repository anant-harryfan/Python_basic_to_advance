# --profile-directory="Profile 1
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path = 'C:\\Program Files (x86)\\chromedriver.exe'

options = Options()
options.add_argument("user-data-dir=C:\\Users\\xyz\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(executable_path=path, chrome_options=options)

driver.get("https://meet.google.com/mma-hvvv-wwu?authuser=0")
time.sleep(5)
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "GOH7Zb")))
    time.sleep(5)
    element.click()
    print(element)
    element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ZB88ed")))
    time.sleep(3)
    element2.click()
    print(element2)
    element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Y5sE8d")))
    time.sleep(3)
    element3.click()
    print(element3)

except Exception as e:
    # driver.quit()
    print(e)
