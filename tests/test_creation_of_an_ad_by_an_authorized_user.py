import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, login_user, generate_user_data

def test_create_ad_authorized(driver):
    email, password = generate_user_data()
    
    # Register user
    register_user(driver, email, password)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/regiatration"))

    # Login user
    login_user(driver, email, password)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "circleSmall")))
    
    # Click on "Place ad"
    post_ad_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains( @class, 'buttonPrimary') and contains(., 'Разместить объявление')]")))
    post_ad_button.click()

    # Wait for the create listing page to load
    wait.until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/create-lisiting"))

    # Fill out the form
    ad_title = "Test Ad Title"
    ad_description = "Test Ad Description"
    ad_price = "12345"

    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[ @placeholder='Название']"))).send_keys(ad_title)
    driver.find_element(By.XPATH, "//textarea[ @placeholder='Описание товара']").send_keys(ad_description)
    driver.find_element(By.CSS_SELECTOR, "input[name='price']").send_keys(ad_price)

    # Select category
    wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[contains( @class, 'dropDownMenu_arrowDown')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Книги"]/parent::button[starts-with( @class, "dropDownMenu_btn")]'))).click()

    # Select city
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[ @name='city']/following-sibling::button"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//button[.//span[text()="Казань"]]'))).click()
    
    # Select condition
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.radioUnput_shell__Wtdwe input[value="Б/У"] + div.radioUnput_inputRegular__FbVbr'))).click()

    # Publish
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Опубликовать']"))).click()

    # Go to profile
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.circleSmall"))).click()
    profile_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains( @class, 'profileText name')]")))
    driver.execute_script("arguments[0].click();", profile_link)
    wait.until(EC.url_contains("/profile"))

    # Verify ad is in profile
    ad_card = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains( @class, 'card')])[last()]")))
    assert "card" in ad_card.get_attribute("class")
