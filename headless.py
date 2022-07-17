from multiprocessing import Semaphore
import string
import time
from datetime import datetime
from logging import exception

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from custom_exceptions import *

opts=webdriver.ChromeOptions()
# opts.add_argument('--headless')
opts.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

driver.maximize_window()
actions = ActionChains(driver)

driver.get("https://hub.test-headout.com/app/")

# click functions ........................................

# click element just by passing xpath string
# my_data = {
#     "Experience Name": "New Experience",
#     "Reference Code": "DJSHD6376XX",
#     "City Name": "New York"
# }

my_data = {
"supplyPartnerBillingEntityId": "User response",
"name": "experience_listing",
"collectionId": "User response",
"cityName": "User response",
"referenceCode" : "User response",
"tourType" : "User response",
"linkToProduct" : "User response",
"content": {
   "highlights": "User response",
   "description": "User response",
   "inclusions": "User response",
   "exclusions": "User response"
 },
"fulfillmentType" : "User response",
"addressLine1": "User response",
"addressLine2": "User response",
"postalCode": "User response",
"durationType": "User response",
"cancellableUpto" : "User response",
"APIcode" : "User response"
}

def click_xpath_element(xpath: str) -> str:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        raise ElementNotFoundError(type(e).__name__)
    else:
        element.click()
        return element

# click link element just by passing link text


def click_link_element(link_text: str) -> bool:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, link_text)))
    except Exception as e:
        raise ElementNotFoundError(type(e).__name__)
    else:
        element.click()

# send keys to element and takes xpath and key


def send_keys_to_xpath(xpath: str, key: str) -> bool:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
        element.click()
    except Exception as e:
        raise ElementNotFoundError(type(e).__name__)
    else:
        element.clear()
        element.send_keys(key)
        return element

def login():
    send_keys_to_xpath("//input[@type='email']", "looker-test-396@headout.com")
    send_keys_to_xpath("//input[@type='password']", "headout-test-396")
    click_xpath_element("//button[normalize-space()='Log in']")

def experience_overview():
    click_xpath_element("(//*[@type='checkbox'])[3]")
    send_keys_to_xpath("//input[@placeholder='Enter name']", my_data["name"]) # Experience Name
    send_keys_to_xpath("//input[@placeholder='Enter Your Reference Code']", my_data["referenceCode"]) # refernce code
    city_element = send_keys_to_xpath("//div[normalize-space()='Enter City Name']", my_data["cityName"])
    city_element.send_keys(Keys.RETURN)
    click_xpath_element("//button[normalize-space()='Next']")

def content():
    send_keys_to_xpath("(//textarea[@placeholder='Enter details'])[1]", my_data["content"]["highlights"])
    send_keys_to_xpath("(//textarea[@placeholder='Enter details'])[2]", my_data["content"]["description"])
    send_keys_to_xpath("(//textarea[@placeholder='Enter value'])[1]", my_data["linkToProduct"])
    send_keys_to_xpath("(//textarea[@placeholder='Enter value'])[2]", my_data["content"]["inclusions"])
    send_keys_to_xpath("(//textarea[@placeholder='Enter value'])[3]", my_data["content"]["exclusions"])
    for language in my_data["languages"]:
        click_xpath_element(f"//input[@value='{language}']")
    click_xpath_element("//button[normalize-space()='Next']")

def booking_info():
    send_keys_to_xpath("//input[@placeholder='Address 1']", my_data["tours"][0]["startPointAddress"]["addressLine1"])
    send_keys_to_xpath("//input[@placeholder='Address 2']", my_data["tours"][0]["startPointAddress"]["addressLine2"])
    send_keys_to_xpath("//input[@placeholder='Enter Postal Index Number code']", my_data["tours"][0]["startPointAddress"]["postalCode"])
    # FF = send_keys_to_xpath(, "API Connection")


def main():
    login()
    click_xpath_element("//button[normalize-space()='New Experience']")
    time.sleep(30)
    experience_overview()
    content()
    time.sleep(3)
    click_xpath_element("//button[normalize-space()='Next']")
    time.sleep(3)
    booking_info()

    driver.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        driver.close()
        raise e
