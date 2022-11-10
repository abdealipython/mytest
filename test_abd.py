import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time


def setup_function():
    global driver
    hub_url = "http://192.168.1.11:4441/wd/hub"
    driver = webdriver.Remote(command_executor=hub_url, desired_capabilities={"browserName": "chrome"})
    driver.get('https://alnafi.com/auth/signin')
    driver.maximize_window()
    print(driver.title)


def teardown_function():
    driver.quit()

def my_data():
    return [
        ("abdeali@alnafi.com","abdeali@123"),
        ("ali@alnafi.com", "ali@123")
    ]


@pytest.mark.parametrize("username,password",my_data())
def test_login(username, password):
    print("My pytest login")
    driver.find_element(By.ID, 'Username/ Email').send_keys(username)
    driver.find_element(By.ID, 'Password').send_keys(password)
    time.sleep(2)
