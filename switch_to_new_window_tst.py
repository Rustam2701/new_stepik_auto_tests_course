from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_number = browser.find_element(By.ID, 'input_value').text
x = int(x_number)

form_x = log(abs(12 * sin(x)))

answer_input = browser.find_element(By.NAME, 'text')
answer_input.send_keys(form_x)

button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
button.click()

time.sleep(30)
browser.quit()
