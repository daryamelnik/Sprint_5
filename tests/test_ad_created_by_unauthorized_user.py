from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import RoutesUrl
from locators import MainPageLocators, AdCreationModalLocators


class TestAdCreatedByUnauthorizedUser:
    def test_ad_creation_unauthorized(self, driver):
        driver.get(RoutesUrl.base_url)
        wait = WebDriverWait(driver, 10)

        # Click the "Place ad" button
        post_ad_button = wait.until(EC.element_to_be_clickable(MainPageLocators.PRIMARY_BUTTON))
        post_ad_button.click()

        # Check: a modal window with the title "To place an ad, please log in" is displayed
        modal = wait.until(EC.visibility_of_element_located(AdCreationModalLocators.MODAL_WINDOW))
        modal_title = modal.find_element(*AdCreationModalLocators.MODAL_TITLE)
        assert modal_title.is_displayed()