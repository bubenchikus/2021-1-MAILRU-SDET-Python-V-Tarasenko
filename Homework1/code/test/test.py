import pytest

import user_data as UD
from ui.locators import basic_locators as BL
from big_actions import BigActions


@pytest.mark.UI
class TestLogin(BigActions):
    #### проверяем работоспособность кнопок в окне логина  ####
    @pytest.mark.parametrize(
        "locator",
        [BL.LOGIN_PASSWORD_RESET_LOCATOR, BL.LOGIN_TERMS_LOCATOR, BL.LOGIN_POLICY_LOCATOR,
         BL.LOGIN_SOCIAL_VK_LOCATOR, BL.LOGIN_SOCIAL_OK_LOCATOR, BL.LOGIN_SOCIAL_MAIL_LOCATOR,
         BL.LOGIN_SOCIAL_GOOGLE_LOCATOR, BL.LOGIN_SOCIAL_FB_LOCATOR, BL.LOGIN_SOCIAL_TWI_LOCATOR,
         BL.LOGIN_REGISTER_LOCATOR, BL.LOGIN_CLOSE_LOCATOR, BL.LOGIN_LOGO_LOCATOR
         ]
    )
    def test_login_buttons(self, locator):
        self.login_page()
        self.click(locator)
        if locator == BL.LOGIN_EYE_LOCATOR:
            self.click(locator)  # close eye

    #### пытаемся логиниться под разными данными ####
    @pytest.mark.parametrize("uid", UD.login.keys())
    def test_login_field(self, uid):
        self.login_fill(uid)


@pytest.mark.UI
class TestLogout(BigActions):
    #### проверяем работоспособность кнопок логаута ####
    def test_logout(self, login_default):
        self.logout_buttons()


@pytest.mark.UI
class TestChange(BigActions):
    ####  проверяем кнопки редактирования контактной информации  ####
    @pytest.mark.parametrize("locator", [BL.CHANGE_SAVE_LOCATOR, BL.CHANGE_ADD_LOCATOR, BL.CHANGE_DELETE_LOCATOR])
    def test_change_buttons(self, locator, login_default):
        self.get_page("https://target.my.com/profile/contacts")
        if locator == BL.CHANGE_DELETE_LOCATOR:
            self.click(BL.CHANGE_ADD_LOCATOR)  # кнопка "удалить" появляется после добавления почты
        self.click(locator)

    #### пытаемся изменить контактную информацию ####
    @pytest.mark.parametrize("uid", UD.change.keys())
    def test_change_field(self, uid, login_default):
        self.change_fill(uid)


@pytest.mark.UI
class TestHead(BigActions):
    #### жмём кнопки в шапке и по наличию элементов проверяем, что произошёл переход на нужную страницу####
    @pytest.mark.parametrize("locator, page_element",
                             [(BL.HEAD_SEGMENTS_LOCATOR, BL.FLAG_SEGMENTS_LOCATOR),
                              (BL.HEAD_BILLING_LOCATOR, BL.FLAG_BILLING_LOCATOR)])
    def test_head_buttons(self, locator, page_element, login_default):
        self.click(locator)
        self.wait_load(page_element)
