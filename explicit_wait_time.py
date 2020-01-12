from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Some website may load with lag (gecikme olabilir ssayfanin yuklenmesinde)
# Eger yuklenmeden iselem yapmaya calisirsak hata verir
# Load edildiginden emin oluktan sonra devam ederiz bu sekilde
url = 'https://google.com/earth'
driver = webdriver.Chrome()
driver.get(url)

# Banner is loaded with lag in google earth
# To overcome this issue 

# EXPLICIT WAIT
wait = WebDriverWait(driver, 10) # waits for 10 seconds
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a')))
launchEarthButton.click()

