import pytest
from selenium import webdriver
import random
import string

@pytest.fixture(scope="function")
def user_data():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{random_string}@example.com"
    password = "qwerty123456"
    return email, password

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
