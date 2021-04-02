from selenium.webdriver.common.by import By

LOGIN_START_LOCATOR = (By.XPATH, "//*[contains(text(), 'Войти')]")
LOGIN_MAIL_LOCATOR = (By.NAME, 'email')
LOGIN_PASSWORD_LOCATOR = (By.NAME, 'password')

LOGIN_CLOSE_LOCATOR = (By.XPATH, "//*[ contains(@class, 'close')]")
LOGIN_LOGO_LOCATOR = (By.XPATH, "(//*[ contains(@class, 'logoLink')])[2]")

LOGIN_SUBMIT_LOCATOR = (By.XPATH, "(//*[contains(text(), 'Войти')])[2]")
LOGIN_EYE_LOCATOR = (By.XPATH, "//*[ contains(@class, 'eye')]")
LOGIN_PASSWORD_RESET_LOCATOR = (By.XPATH, "//*[contains(text(), 'Забыли')]")
LOGIN_TERMS_LOCATOR = (By.XPATH, "//*[contains(text(), 'Условиями')]")
LOGIN_POLICY_LOCATOR = (By.XPATH, "//*[contains(text(), 'Политикой')]")
LOGIN_SOCIAL_VK_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-vk')]")
LOGIN_SOCIAL_OK_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-ok')]")
LOGIN_SOCIAL_MAIL_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-mailru')]")
LOGIN_SOCIAL_GOOGLE_LOCATOR = (By.XPATH, "(//*[ contains(@class, 'socialIcon')])[9]")
LOGIN_SOCIAL_FB_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-fb')]")
LOGIN_SOCIAL_TWI_LOCATOR = (By.XPATH, "//*[ contains(@class, 'socialIcon-tw')]")
LOGIN_REGISTER_LOCATOR = (By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]")


LOGOUT_START_LOCATOR = (By.XPATH, "//*[contains(@class, 'right-module-mail')]")
LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(), 'Выйти')]")


CHANGE_FIO_LOCATOR = (By.XPATH, "(//*[contains(@maxlength, '100')])[1]")
CHANGE_PHONE_LOCATOR = (By.XPATH, "//*[contains(@maxlength, '20')]")
CHANGE_MAIL_LOCATOR = (By.XPATH, "(//*[contains(@maxlength, '100')])[2]")

CHANGE_REMOVE_MAIL_LOCATOR = (By.XPATH, "//*[ contains(@class, 'email_remove')]")
CHANGE_SAVE_LOCATOR = (By.XPATH, "//*[contains(text(), 'Сохранить')]")
CHANGE_ADD_LOCATOR = (By.XPATH, "//*[contains(@class, 'clickable-button__spinner')]")
CHANGE_DELETE_LOCATOR = (By.XPATH, "//*[ contains(@class, 'email_remove')]")


DASHBOARD_CONTENT = (By.XPATH, "//*[ contains(@class, 'instruction-module-container')]")


HEAD_SEGMENTS_LOCATOR = (By.XPATH, "//*[ contains(@class, 'segments')]")
HEAD_BILLING_LOCATOR = (By.XPATH, "//*[ contains(@class, 'billing')]")


FLAG_SEGMENTS_LOCATOR = (By.XPATH, "//*[contains(text(), 'Аудиторные сегменты')]")
FLAG_BILLING_LOCATOR = (By.XPATH, "//*[@data-type='deposit']")
