from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_user_data, login_user, register_user
from urls import RoutesUrl
from locators import MainPageLocators, AdCreationPageLocators, ProfilePageLocators
from data import AdData

class TestCreationOfAnAdByAnAuthorizedUser:
    def test_create_ad_authorized(self, driver):
        email, password = generate_user_data()

        # Register user
        register_user(driver, email, password)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.url_to_be(RoutesUrl.registration_url))

        # Login user
        login_user(driver, email, password)
        wait.until(EC.visibility_of_element_located(MainPageLocators.USER_PROFILE_ICON))

        # Click on "Place ad"
        post_ad_button = wait.until(EC.element_to_be_clickable(MainPageLocators.PRIMARY_BUTTON))
        post_ad_button.click()

        # Wait for the create listing page to load
        wait.until(EC.url_to_be(RoutesUrl.create_listing_url))

        # Fill out the form
        wait.until(EC.visibility_of_element_located(AdCreationPageLocators.AD_TITLE_INPUT)).send_keys(AdData.TITLE)
        driver.find_element(*AdCreationPageLocators.AD_DESCRIPTION_TEXTAREA).send_keys(AdData.DESCRIPTION)
        driver.find_element(*AdCreationPageLocators.AD_PRICE_INPUT).send_keys(AdData.PRICE)

        # Select category
        wait.until(EC.element_to_be_clickable(AdCreationPageLocators.CATEGORY_DROPDOWN)).click()
        category_option_xpath = AdCreationPageLocators.CATEGORY_OPTION_XPATH.format("Книги")
        wait.until(EC.element_to_be_clickable((By.XPATH, category_option_xpath))).click()

        # Select city
        wait.until(EC.element_to_be_clickable(AdCreationPageLocators.CITY_DROPDOWN)).click()
        city_option_xpath = AdCreationPageLocators.CITY_OPTION_XPATH.format("Казань")
        wait.until(EC.element_to_be_clickable((By.XPATH, city_option_xpath))).click()

        # Select condition
        wait.until(EC.element_to_be_clickable(AdCreationPageLocators.CONDITION_USED_RADIO)).click()

        # Publish
        wait.until(EC.element_to_be_clickable(AdCreationPageLocators.PUBLISH_BUTTON)).click()

        # Go to profile
        driver.get(RoutesUrl.profile_url)
        wait.until(EC.url_to_be(RoutesUrl.profile_url))

        # Verify ad is in profile
        ad_card = wait.until(EC.visibility_of_element_located(ProfilePageLocators.LAST_AD_CARD))
        assert "card" in ad_card.get_attribute("class")