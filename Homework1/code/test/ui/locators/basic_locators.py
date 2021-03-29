from selenium.webdriver.common.by import By

LOGIN_START_LOCATOR = (By.XPATH, "//*[contains(text(), 'Войти')]")
LOGIN_MAIL_LOCATOR = (By.NAME, 'email')
LOGIN_PASSWORD_LOCATOR = (By.NAME, 'password')
LOGIN_SUBMIT_LOCATOR = (By.XPATH, "//*[ contains(@class, 'authForm-module-button')]")
LOGIN_LOGO_LOCATOR = (By.XPATH, "//*[ contains(@class, 'authForm-module-logoLink')]")
LOGIN_CLOSE_LOCATOR = (By.XPATH, "//*[ contains(@class, 'close')]")
LOGIN_EYE_LOCATOR = (By.XPATH, "//*[ contains(@class, 'eye')]")
LOGIN_PASSWORD_RESET_LOCATOR = (By.XPATH, "//*[contains(text(), 'Забыли')]")
LOGIN_TERMS_LOCATOR = (By.XPATH, "//*[contains(text(), 'Условиями')]")
LOGIN_POLICY_LOCATOR = (By.XPATH, "//*[contains(text(), 'Политикой')]")
LOGIN_SOCIAL_VK_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-vk')]")
LOGIN_SOCIAL_OK_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-ok')]")
LOGIN_SOCIAL_MAIL_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-mailru')]")
LOGIN_SOCIAL_GOOGLE_LOCATOR = (By.XPATH, "//*[ contains(@style, 'authGoo')]")
LOGIN_SOCIAL_FB_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-fb')]")
LOGIN_SOCIAL_TWI_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-tw')]")
LOGIN_REGISTER_LOCATOR = (By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]")


LOGOUT_START_LOCATOR = (By.XPATH, "//*[contains(@class, 'right-module-rightButton')]")
LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(), 'Выйти')]")


CHANGE_FIO_LOCATOR = (By.XPATH, "//*[contains(@data-name, 'fio')]//*[ contains(@class, 'input__inp')]")
CHANGE_PHONE_LOCATOR = (By.XPATH, "//*[contains(@data-name, 'phone')]//*[ contains(@class, 'input__inp')]")
CHANGE_MAIL_LOCATOR = (By.XPATH, "//*[contains(@class, 'js-additional-email')]"
                                 "//*[ contains(@class, 'input__inp')]")
CHANGE_REMOVE_MAIL_LOCATOR = (By.XPATH, "//*[ contains(@class, 'email_remove')]")
CHANGE_SAVE_LOCATOR = (By.XPATH, "//*[contains(text(), 'Сохранить')]")
CHANGE_ADD_LOCATOR = (By.XPATH, "//*[contains(@class, 'clickable-button__spinner')]")
CHANGE_DELETE_LOCATOR = (By.XPATH, "//*[ contains(@class, 'email_remove')]")

DASHBOARD_CONTENT = (By.XPATH, "//*[ contains(@class, 'instruction-module-container')]")

HEAD_SEGMENTS_LOCATOR = (By.XPATH, "//*[ contains(@class, 'segments')]")
HEAD_BILLING_LOCATOR = (By.XPATH, "//*[ contains(@class, 'billing')]")
