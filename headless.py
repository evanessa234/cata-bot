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

def login():
    send_keys_to_xpath("//input[@type='email']", "looker-test-396@headout.com")
    send_keys_to_xpath("//input[@type='password']", "headout-test-396")
    click_xpath_element("//button[normalize-space()='Log in']")

def main():
    login()
    driver.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        driver.close()
        raise e
