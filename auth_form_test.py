from math import sin, log

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_number = browser.find_element(By.ID, 'input_value').text
x = int(x_number)

form_x = log(abs(12 * sin(x)))

answer_input = browser.find_element(By.ID, 'answer')
answer_input.send_keys(form_x)

checkbox1 = browser.find_element(By.ID, "robotCheckbox")
checkbox1.click()

radiobutton1 = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton1)
radiobutton1.click()

button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
