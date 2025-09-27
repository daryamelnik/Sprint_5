import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def register_user(driver, email, password):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    wait = WebDriverWait(driver, 10)

    # Check if already logged in, then logout
    if len(driver.find_elements(By.CLASS_NAME, "circleSmall")) > 0:
        driver.find_element(By.CLASS_NAME, "circleSmall").click()
        time.sleep(2) # Increased sleep time
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Вых')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, ".//button[text()='Вход и регистрация']")))
        driver.get('https://qa-desk.stand.praktikum-services.ru/') # Navigate back to home page after logout

    # Navigate to registration form
    wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Вход и регистрация']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Нет аккаунта']"))).click()

    # Fill out registration form
    wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submitPassword").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Создать аккаунт']").click()

def login_user(driver, email, password):
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    wait = WebDriverWait(driver, 10)

    # Check if already logged in
    if len(driver.find_elements(By.CLASS_NAME, "circleSmall")) > 0:
        return

    # Navigate to login form
    wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Вход и регистрация']"))).click()

    # Fill out login form
    wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()