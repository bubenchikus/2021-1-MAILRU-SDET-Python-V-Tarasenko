import pytest
from big_actions import BigActions
from ui.locators import basic_locators as BL
import user_data as UD


@pytest.mark.UI
class TestLogin(BigActions):
    #### проверяем работоспособность кнопок в окне логина ####
    @pytest.mark.parametrize("locator", [BL.LOGIN_CLOSE_LOCATOR, BL.LOGIN_LOGO_LOCATOR])
    def test_login_buttons(self, locator):
        self.login_page()
        self.click(locator)
        if locator == BL.LOGIN_EYE_LOCATOR:
            self.click(locator)  # close eye

    #### проверяем работоспособность гиперссылок в окне логина  ####
    @pytest.mark.parametrize(
        "locator",
        [BL.LOGIN_PASSWORD_RESET_LOCATOR, BL.LOGIN_TERMS_LOCATOR, BL.LOGIN_POLICY_LOCATOR,
         BL.LOGIN_SOCIAL_VK_LOCATOR, BL.LOGIN_SOCIAL_OK_LOCATOR, BL.LOGIN_SOCIAL_MAIL_LOCATOR,
         BL.LOGIN_SOCIAL_GOOGLE_LOCATOR, BL.LOGIN_SOCIAL_FB_LOCATOR, BL.LOGIN_SOCIAL_TWI_LOCATOR,
         BL.LOGIN_REGISTER_LOCATOR
         ]
    )
    def test_login_links(self, locator):
        self.login_page()
        self.click(locator)
        if locator != BL.LOGIN_REGISTER_LOCATOR:
            self.close_window()

    #### пытаемся логиниться под разными данными ####
    def test_login_field_default(self, logout_default):
        self.login_fill('default')
        self.wait_load(BL.DASHBOARD_CONTENT)

    @pytest.mark.parametrize("uid", UD.login.keys())
    def test_login_field_incorrect(self, uid):
        try:
            if uid != 'default':
                self.login_fill(uid)
        except ValueError:
            print("Login fields can't handle this data")


@pytest.mark.UI
class TestLogout(BigActions):
    def test_logout(self, login_default):
        self.wait_load(BL.DASHBOARD_CONTENT)
        self.click(BL.LOGOUT_START_LOCATOR)
        self.click(BL.LOGOUT_BUTTON_LOCATOR)


@pytest.mark.UI
class TestChange(BigActions):
    ####  проверяем кнопки редактирования контактной информации  ####
    @pytest.mark.parametrize("locator", [BL.CHANGE_SAVE_LOCATOR, BL.CHANGE_ADD_LOCATOR])
    def test_change_buttons(self, locator, login_default, logout_default):
        self.change_page()
        self.click(locator)

    def test_change_delete(self, login_default, logout_default):
        self.change_page()
        self.click(BL.CHANGE_ADD_LOCATOR)
        self.click(BL.CHANGE_DELETE_LOCATOR)

    #### пытаемся изменить контактную информацию ####
    @pytest.mark.parametrize("uid", UD.change.keys())
    def test_change_field(self, uid, login_default, logout_default):
        try:
            self.change_fill(uid)
            self.click(BL.CHANGE_SAVE_LOCATOR)
        except ValueError:
            print("Change window can't handle this data")


@pytest.mark.UI
class TestHead(BigActions):
    @pytest.mark.parametrize("locator", [BL.HEAD_SEGMENTS_LOCATOR, BL.HEAD_BILLING_LOCATOR])
    def test_head_buttons(self, locator, login_default, logout_default):
        self.wait_load(BL.DASHBOARD_CONTENT)
        self.click(locator)
        if locator == BL.HEAD_SEGMENTS_LOCATOR:
            assert self.driver.current_url == 'https://target.my.com/segments/segments_list', 'AAAAAA! Incorrect url..'
        elif locator == BL.HEAD_BILLING_LOCATOR:
            assert self.driver.current_url == 'https://target.my.com/billing', 'AAAAAA! Incorrect url..'
