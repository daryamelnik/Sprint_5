from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, generate_user_data
from urls import RoutesUrl
from locators import RegistrationPageLocators

class TestRegisterExisting:
    def test_register_existing_user(self, driver):
        email, password = generate_user_data()

        # First, register the user
        register_user(driver, email, password)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be(RoutesUrl.registration_url))

        # Now, try to register the same user again
        register_user(driver, email, password)

        # Verify that registration fails and error messages are displayed
        error_message = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
        assert error_message.is_displayed()

        # Verify that the input fields are highlighted in red
        email_field_div = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).find_element(By.XPATH, "./..")
        password_field_div = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).find_element(By.XPATH, "./..")
        submit_password_field_div = driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT).find_element(By.XPATH, "./..")

        assert "input_inputError" in email_field_div.get_attribute("class")
        assert "input_inputError" in password_field_div.get_attribute("class")
        assert "input_inputError" in submit_password_field_div.get_attribute("class")