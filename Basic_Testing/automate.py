from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import time

try:
    # Setup Chrome driver with proper options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')  # Start browser maximized
    
    # Use the chromedriver from the specified path
    service = Service(r"C:\Users\sujay\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Navigate to the page
    driver.get(r"D:\Selenium\Basic_Testing\hover.html")
    time.sleep(4)
    driver.find_element(By.NAME,"name").send_keys("Sumit")
    time.sleep(1)
    driver.find_element(By.ID,"submitBtn").click()
    time.sleep(1)

    #Task 2
    ele = driver.find_element(By.XPATH,"/html/body/main/section/div[2]/select")
    select = Select(ele)
    select.select_by_value("green")
    time.sleep(1)

    #tsak 3
    driver.find_element(By.XPATH,"/html/body/main/section/div[3]/label/input").click()
    time.sleep(1)
    #task 4
    driver.find_element(By.XPATH,"/html/body/main/section/fieldset/label[1]/input").click()
    time.sleep(1)
    # task 5 - delayed content (no alert in page; wait for visibility)
    driver.find_element(By.ID, "showDelayedBtn").click()
    wait = WebDriverWait(driver, 7)
    # Wait for the delayed content element to become visible
    wait.until(EC.visibility_of_element_located((By.ID, "delayedContent")))
    time.sleep(1)

    # task 6 - open modal and close it (use the close button's ID)
    driver.find_element(By.ID, "openModalBtn").click()
    # wait for modal to be visible
    wait.until(EC.visibility_of_element_located((By.ID, "practiceModal")))
    # click the close button by ID (more reliable than XPath)
    driver.find_element(By.ID, "closeModalBtn").click()
    time.sleep(1)

    # task 7 - click "Add row" button multiple times
    add_btn = driver.find_element(By.ID, "addRowBtn")
    for i in range(5):
        add_btn.click()
        time.sleep(0.5)
    time.sleep(1)
    #task 8 -- clicking on the "link" after hovering
    element = driver.find_element(By.ID,"hoverArea")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/h1/a").click()
    driver.implicitly_wait(10)


except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Clean up
    try:
        driver.quit()
    except:
        pass