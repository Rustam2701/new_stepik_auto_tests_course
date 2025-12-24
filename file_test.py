from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'filename.txt')

first_name_field = browser.find_element(By.NAME, 'firstname')
first_name_field.send_keys('Rustam')

last_name_field = browser.find_element(By.NAME, 'lastname')
last_name_field.send_keys('Rusti')

email_field_input = browser.find_element(By.NAME, "email")
email_field_input.send_keys('trey@yandex.ru')

load_file_button = browser.find_element(By.ID, 'file')
load_file_button.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
button.click()

time.sleep(30)
browser.quit()
