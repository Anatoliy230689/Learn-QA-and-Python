from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path="/home/anatoliy/PycharmProjects/pythonProject/geckodriver")
driver.get("https://www.google.ru/")
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys('webdriver')

time.sleep(10)
driver.close()
driver.quit()