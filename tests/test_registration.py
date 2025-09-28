from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, generate_user_data

def test_registration(driver):
    email, password = generate_user_data()
    register_user(driver, email, password)
    
    wait = WebDriverWait(driver, 10)
    # Verify successful registration
    wait.until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/regiatration"))
    assert "https://qa-desk.stand.praktikum-services.ru/regiatration" == driver.current_url

    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "buttonPrimary"))).text == 'Разместить объявление'