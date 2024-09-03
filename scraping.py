from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium.common.exceptions as selenium_exceptions


phone_number = "+62 123456" #fill with Number
message = "Jancok" #fill with massage



service = Service(EdgeChromiumDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Edge(service=service)

# Open a webpage
driver.get('https://web.whatsapp.com/')

try:
    canvas_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas'))
    )
    print("Canvas element found, waiting for the next element...")

    # Wait for up to 20 seconds for the second element to appear after the first one
    side_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p'))
    )

    print("Second element found, continuing to the next step...")
except:
    # If the element is not found, continue to the next step
    print("Element not found, continuing to the next step...")

side_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p'))
    )

driver.get(f'https://web.whatsapp.com/send?phone={phone_number}&text={message}')

sent_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))
    )

sent_element.click()

for i in range(100):
    try:
        write_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'))
        )
        write_element.click()
        write_element.clear()
        write_element.send_keys(f"{message}-{i}")
        sent_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))
        )

        sent_element.click()

        print("write_element element found, waiting for the next element...")
    except:
        # If the element is not found, continue to the next step
        print("Element not found, continuing to the next step...")

input("Press Enter to continue...")