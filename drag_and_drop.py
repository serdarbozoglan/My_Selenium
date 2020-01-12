import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # used for drag and dropping

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
sourceElement = driver.find_element_by_xpath('//*[@id="DHTMLgoodies_dragableElement2"]']) #element to move (Washington) 
# There is an issue with the above selection but the logis should be in this way
destinationElement = driver.find_element_by_xpath('//*[@id="box103"]') # destination elemnt (United States)
actions = ActionChains(driver)
actions.drag_and_drop(sourceElement, destinationElement).perform()