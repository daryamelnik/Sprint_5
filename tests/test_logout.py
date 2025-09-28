from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, login_user, generate_user_data

def test_logout(driver):
    email, password = generate_user_data()
    
    # First, register the user
    register_user(driver, email, password)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/regiatration"))

    # Now, log in
    login_user(driver, email, password)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "circleSmall")))

    # Logout
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "circleSmall"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnSmall"))).click()

    # Verify that the user is logged out
    assert wait.until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Вход и регистрация']"))).is_displayed()
    
    # Verify that the user avatar and name are not displayed
    assert len(driver.find_elements(By.CLASS_NAME, "circleSmall")) == 0
    assert len(driver.find_elements(By.CLASS_NAME, "profileText")) == 0