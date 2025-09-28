from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, generate_user_data
from urls import RoutesUrl
from locators import MainPageLocators

class TestRegistration:
    def test_registration(self, driver):
        email, password = generate_user_data()
        register_user(driver, email, password)

        wait = WebDriverWait(driver, 10)
        # Verify successful registration
        wait.until(EC.url_to_be(RoutesUrl.registration_url))
        assert RoutesUrl.registration_url == driver.current_url

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.PRIMARY_BUTTON)).text == 'Разместить объявление'