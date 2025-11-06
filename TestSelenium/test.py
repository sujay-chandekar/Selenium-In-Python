from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


import time

service = Service(r"C:\Users\sujay\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

#1
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/fieldset/label[2]/input").click()
time.sleep(1)
#2
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/fieldset/input").send_keys("ndcjcdscj")
time.sleep(1)
#3
ele = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/fieldset/select")
select = Select(ele)
select.select_by_value('option2')
time.sleep(1)
#4
driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/fieldset/label[3]/input").click()
time.sleep(1)
#5
driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/fieldset/button").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
print(driver.title)
#6
driver.switch_to.window(handles[0])
print(driver.title)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/fieldset/a").click()
time.sleep(2)
handles = driver.window_handles
time.sleep(1)
driver.switch_to.window(handles[0])
time.sleep(2)
#7
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/fieldset/input[1]").send_keys("Ishavar")
driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/fieldset/input[2]").click()
wait = WebDriverWait(driver,10)
driver.switch_to.alert
alert = wait.until(EC.alert_is_present())
time.sleep(1)
alert.accept()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/fieldset[1]/input[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/fieldset[1]/input[2]").click()
time.sleep(1)
#mouse hover
ele = driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/button")
actions = ActionChains(driver)
actions.move_to_element(ele).click().perform()
driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[1]").click()
time.sleep(2)
#iframe switch
frame1 = driver.find_element(By.XPATH,"/html/body/div[5]/fieldset/iframe")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[2]/a").click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)