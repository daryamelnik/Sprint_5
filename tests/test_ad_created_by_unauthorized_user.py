from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import UrbanRoutesUrl


def test_ad_creation_unauthorized(driver):
    driver.get(UrbanRoutesUrl.base_url)
    wait = WebDriverWait(driver, 10)

    # Click the "Place ad" button
    post_ad_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Разместить объявление']")))
    post_ad_button.click()

    # Check: a modal window with the title "To place an ad, please log in" is displayed
    modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.homePage_modal__zSdUB")))
    modal_title = modal.find_element(By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    assert modal_title.is_displayed()