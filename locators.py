from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    USER_PROFILE_ICON = (By.CLASS_NAME, "circleSmall")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    LOGOUT_BUTTON_PROFILE_DROPDOWN = (By.CLASS_NAME, "btnSmall")
    PROFILE_TEXT = (By.CLASS_NAME, "profileText")
    PRIMARY_BUTTON = (By.CLASS_NAME, "buttonPrimary")


class AdCreationModalLocators:
    MODAL_WINDOW = (By.CSS_SELECTOR, "div.homePage_modal__zSdUB")
    MODAL_TITLE = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")


class LoginRegisterPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")


class RegistrationPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ошибка')]")


class AdCreationPageLocators:
    AD_TITLE_INPUT = (By.XPATH, "//input[@placeholder='Название']")
    AD_DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    AD_PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_DROPDOWN = (By.XPATH, ".//button[contains(@class, 'dropDownMenu_arrowDown')]")
    CATEGORY_OPTION_XPATH = '//span[text()="{}"]/parent::button[starts-with(@class, "dropDownMenu_btn")]'
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_OPTION_XPATH = '//button[.//span[text()="{}"]]'
    CONDITION_USED_RADIO = (By.CSS_SELECTOR, 'div.radioUnput_shell__Wtdwe input[value="Б/У"] + div.radioUnput_inputRegular__FbVbr')
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//h3[contains(@class, 'profileText name')]")
    LAST_AD_CARD = (By.XPATH, "(//div[contains(@class, 'card')])[last()]")


class TestLoginLocators:
    PRIMARY_BUTTON = (By.CLASS_NAME, "buttonPrimary")
    PROFILE_TEXT = (By.CLASS_NAME, "profileText")