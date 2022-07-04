from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.youtube.com/')



cookieAccept = driver.find_element(By.XPATH, "//*[@id=\"text\" and (contains(text(),'Принять все'))]")
cookieAccept.click()

searchbox = driver.find_element(By.XPATH, '//*[@id="search"]')
searchbox.send_keys('natalia qa')

searchButton = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
searchButton.click()

driver.close()