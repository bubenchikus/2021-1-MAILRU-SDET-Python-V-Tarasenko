from selenium.webdriver.common.by import By


class BaseLocators:
    pass


class MainLocators(BaseLocators):
    ALLOW_BUTTON = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    ENTER_CHAT = (By.ID, 'ru.mail.search.electroscope:id/keyboard')
    ENTER_SETTINGS = (By.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')


class ChatLocators(MainLocators):
    MESSAGE_FIELD = (By.ID, 'ru.mail.search.electroscope:id/input_text')
    SEND_FIELD = (By.ID, 'ru.mail.search.electroscope:id/text_input_send')
    FACT_CARD = (By.XPATH, "//android.widget.TextView[contains(@text,'государство в Восточной Европе')]")
    POPULATION_REQUEST = (By.XPATH, "//android.widget.TextView[@text='численность населения россии']")
    POPULATION_RESPONSE = (By.XPATH, "//android.widget.TextView[@text='146 млн.']")
    CALCULATOR_RESPONSE = (By.XPATH, "//android.widget.TextView[@text='9']")


class SettingsLocators(MainLocators):
    NEWS_SOURCE = (By.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    VESTI_FM = (By.XPATH, "//android.widget.TextView[@text='Вести FM']")
    CHECK = (By.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')

    ABOUT = (By.ID, 'ru.mail.search.electroscope:id/user_settings_about')
    VERSION = (By.XPATH, "//android.widget.TextView[contains(@text,'Версия')]")
    RIGHTS_RESERVED = (By.XPATH, "//android.widget.TextView[contains(@text,'Все права защищены.')]")

