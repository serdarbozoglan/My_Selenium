import requests
from selenium import webdriver
driver= webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Bismillahirrahmanirrahim')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

addField1 = driver.find_element_by_xpath('//*[@id="sum1"]') # "copy xpath" by mouse when highlight the relevant part and inspect 
addField1.send_keys('10')
addField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
addField2.send_keys('20')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()

