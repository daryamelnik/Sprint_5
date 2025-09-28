from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, login_user, generate_user_data
from urls import RoutesUrl
from locators import MainPageLocators

class TestLogout:
    def test_logout(self, driver):
        email, password = generate_user_data()

        # First, register the user
        register_user(driver, email, password)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be(RoutesUrl.registration_url))

        # Now, log in
        login_user(driver, email, password)
        wait.until(EC.visibility_of_element_located(MainPageLocators.USER_PROFILE_ICON))

        # Logout
        wait.until(EC.element_to_be_clickable(MainPageLocators.USER_PROFILE_ICON)).click()
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON_PROFILE_DROPDOWN)).click()

        # Verify that the user is logged out
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON)).is_displayed()

        # Verify that the user avatar and name are not displayed
        assert len(driver.find_elements(*MainPageLocators.USER_PROFILE_ICON)) == 0
        assert len(driver.find_elements(*MainPageLocators.PROFILE_TEXT)) == 0