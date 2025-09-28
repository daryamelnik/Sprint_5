from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import RegistrationData
from urls import RoutesUrl
from locators import MainPageLocators, LoginRegisterPageLocators, RegistrationPageLocators


class TestRegistrationWithoutMask:
    def test_registration_without_mask(self, driver):
        driver.get(RoutesUrl.base_url)

        wait = WebDriverWait(driver, 10)

        # Navigate to registration form
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LoginRegisterPageLocators.NO_ACCOUNT_BUTTON)).click()

        # Fill out registration form with invalid email
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT))
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(RegistrationData.INVALID_EMAIL)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("qwerty123456")
        driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).send_keys("qwerty123456")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        # Verify that registration fails
        error_message = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
        assert error_message.is_displayed()

        assert RoutesUrl.registration_url == driver.current_url

        # Verify that the input fields are highlighted in red
        email_field_div = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).find_element(By.XPATH, "./..")
        password_field_div = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).find_element(By.XPATH, "./..")
        submit_password_field_div = driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).find_element(By.XPATH, "./..")

        assert "input_inputError" in email_field_div.get_attribute("class")
        assert "input_inputError" in password_field_div.get_attribute("class")
        assert "input_inputError" in submit_password_field_div.get_attribute("class")