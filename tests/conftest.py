import pytest
from selenium import webdriver
from helpers import generate_user_data, register_user


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    email, password = generate_user_data()
    register_user(driver, email, password)
    return email, password
