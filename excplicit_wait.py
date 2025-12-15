from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 14).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
button.click()

x_number = browser.find_element(By.ID, 'input_value').text
x = int(x_number)

form_x = log(abs(12*sin(x)))

answer_input = browser.find_element(By.ID, 'answer')
answer_input.send_keys(form_x)

button = browser.find_element(By.ID, 'solve')
browser.execute_script("arguments[0].scrollIntoView(true);", button)
button.click()


time.sleep(30)
browser.quit()
