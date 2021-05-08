from selenium.webdriver.common.by import By


class BaseLocators:
    RESPONSE = "//android.widget.TextView[contains(@text, '{}')]"


class MainLocators(BaseLocators):
    ENTER_CHAT = (By.ID, 'ru.mail.search.electroscope:id/keyboard')
    ENTER_SETTINGS = (By.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')


class ChatLocators(MainLocators):
    MESSAGE_FIELD = (By.ID, 'ru.mail.search.electroscope:id/input_text')
    SEND_FIELD = (By.ID, 'ru.mail.search.electroscope:id/text_input_send')


class SettingsLocators(MainLocators):
    NEWS_SOURCE = (By.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    CHECK = (By.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')
    BACK = (By.CLASS_NAME, "android.widget.ImageButton")

    ABOUT = (By.ID, 'ru.mail.search.electroscope:id/user_settings_about')


