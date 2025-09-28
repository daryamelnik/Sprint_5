import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, login_user, generate_user_data
from urls import UrbanRoutesUrl

def test_login(driver):
    email, password = generate_user_data()
    
    # First, register the user
    register_user(driver, email, password)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be(UrbanRoutesUrl.registration_url))

    # Assert that the user is logged in
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "circleSmall"))).is_displayed()

    # Logout

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "circleSmall"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выйти')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Вход и регистрация']")))

    # Now, log in
    login_user(driver, email, password)

    # Verify successful login
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "buttonPrimary"))).text == 'Разместить объявление'
    
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "circleSmall"))).is_displayed()

    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "profileText"))).is_displayed()