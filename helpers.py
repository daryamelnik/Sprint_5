import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginRegisterPageLocators, RegistrationPageLocators
from urls import RoutesUrl


def generate_user_data():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{random_string}@example.com"
    password = "qwerty123456"
    return email, password


def register_user(driver, email, password):
    driver.get(RoutesUrl.base_url)
    wait = WebDriverWait(driver, 10)

    # Check if already logged in, then logout
    if len(driver.find_elements(*MainPageLocators.USER_PROFILE_ICON)) > 0:
        driver.find_element(*MainPageLocators.USER_PROFILE_ICON).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))
        driver.get(RoutesUrl.base_url) # Navigate back to home page after logout

    # Navigate to registration form
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(LoginRegisterPageLocators.NO_ACCOUNT_BUTTON)).click()

    # Wait for the registration form to be loaded
    wait.until(EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON))

    # Fill out registration form
    wait.until(EC.element_to_be_clickable(RegistrationPageLocators.EMAIL_INPUT)).send_keys(email)
    wait.until(EC.element_to_be_clickable(RegistrationPageLocators.PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(RegistrationPageLocators.CONFIRM_PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)).click()

def login_user(driver, email, password):
    driver.get(RoutesUrl.base_url)
    wait = WebDriverWait(driver, 10)

    # Check if already logged in
    if len(driver.find_elements(*MainPageLocators.USER_PROFILE_ICON)) > 0:
        return

    # Navigate to login form
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()

    # Fill out login form
    wait.until(EC.element_to_be_clickable(LoginRegisterPageLocators.EMAIL_INPUT)).send_keys(email)
    wait.until(EC.element_to_be_clickable(LoginRegisterPageLocators.PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(LoginRegisterPageLocators.LOGIN_BUTTON)).click()