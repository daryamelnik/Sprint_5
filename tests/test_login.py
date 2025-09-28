from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login_user
from locators import MainPageLocators, TestLoginLocators

class TestLogin:
    def test_login(self, driver, registered_user):
        email, password = registered_user
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(MainPageLocators.USER_PROFILE_ICON)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))

        # Now, execute the login process
        login_user(driver, email, password)

        # Verify that the login was successful
        assert wait.until(
            EC.visibility_of_element_located(TestLoginLocators.PRIMARY_BUTTON)).text == 'Разместить объявление'

        assert wait.until(EC.visibility_of_element_located(MainPageLocators.USER_PROFILE_ICON)).is_displayed()

        assert wait.until(EC.visibility_of_element_located(TestLoginLocators.PROFILE_TEXT)).is_displayed()