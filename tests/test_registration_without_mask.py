import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def generate_invalid_email():
    return "invalid-email"

def test_registration_without_mask(driver):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')

    wait = WebDriverWait(driver, 10)

    # Navigate to registration form
    wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Вход и регистрация']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Нет аккаунта']"))).click()

    # Fill out registration form with invalid email
    wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    invalid_email = generate_invalid_email()
    driver.find_element(By.NAME, "email").send_keys(invalid_email)
    driver.find_element(By.NAME, "password").send_keys("qwerty123456")
    driver.find_element(By.NAME, "submitPassword").send_keys("qwerty123456")
    driver.find_element(By.XPATH, ".//button[text()='Создать аккаунт']").click()

    # Verify that registration fails
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка')]")))
    assert error_message.is_displayed()

    assert "https://qa-desk.stand.практикум-сервисы.рф/regiatration" != driver.current_url

    # Verify that the input fields are highlighted in red
    email_field_div = driver.find_element(By.NAME, "email").find_element(By.XPATH, "./..")
    password_field_div = driver.find_element(By.NAME, "password").find_element(By.XPATH, "./..")
    submit_password_field_div = driver.find_element(By.NAME, "submitPassword").find_element(By.XPATH, "./..")

    assert "input_inputError" in email_field_div.get_attribute("class")
    assert "input_inputError" in password_field_div.get_attribute("class")
    assert "input_inputError" in submit_password_field_div.get_attribute("class")