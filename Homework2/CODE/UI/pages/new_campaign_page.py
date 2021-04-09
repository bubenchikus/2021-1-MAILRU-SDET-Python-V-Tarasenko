from CODE.UI.pages.main_page import MainPage
from CODE.UI.locators.page_locators import NewCampaignPageLocators
from selenium.webdriver.support import expected_conditions as EC
import os
import pytest
import time


class HintNotShowed(Exception):
    pass


class NewCampaignPage(MainPage):

    locators = NewCampaignPageLocators()

    def choose_goal(self, option=locators.GOAL_TRAFFIC_LOCATOR):
        self.click(option)

    def fill_url(self, url='https://en.wikipedia.org/wiki/Goose'):
        self.fill_field(self.locators.URL_LOCATOR, url)

    def fill_name(self, name='My Campaign Name'):
        # баг?: после заполнения урла автоматически открывается раздел География
        self.wait().until(EC.presence_of_element_located(self.locators.FOOTER_LOCATOR))
        self.wait().until(EC.presence_of_element_located(self.locators.MAPBOX))
        self.click(self.locators.EXPAND_WHO_GEOGRAPHY_LOCATOR)
        self.fill_field(self.locators.NAME_LOCATOR, name)

    # def check_hint(self, locator, message):
    #     self.move_cursor(locator)
    #     self.find(message)

    # def check_sex_hint(self):
    #     self.check_hint(self.locators.WHO_SEX_HINT_LOCATOR, self.locators.WHO_SEX_HINT_TEXT_LOCATOR)

    def set_sex(self, option=locators.WHO_SEX_CHECKBOX_F_LOCATOR):
        self.click(self.locators.EXPAND_WHO_SEX_LOCATOR)
        self.click(option)

    # def check_age_hint(self):
    #     self.check_hint(self.locators.WHO_AGE_HINT_LOCATOR, self.locators.WHO_AGE_HINT_TEXT_LOCATOR)

    def set_age(self, option=locators.WHO_AGE_SELECT_UNKNOWN_LOCATOR):
        self.click(self.locators.EXPAND_WHO_AGE_LOCATOR)
        self.click(self.locators.WHO_AGE_CHECKBOX_LOCATOR)
        self.click(self.locators.WHO_AGE_SELECT_LOCATOR)
        self.click(option)

    def set_geography(self, radio=locators.WHO_GEOGRAPHY_RADIO_REGION_LOCATOR, region='Москва'):
        self.click(self.locators.EXPAND_WHO_GEOGRAPHY_LOCATOR)
        self.click(radio)
        self.fill_field(self.locators.WHO_GEOGRAPHY_ADD_WITH_FIELD_LOCATOR, region)
        self.click(self.locators.WHO_GEOGRAPHY_ADD_WITH_FIELD_CONFIRM_LOCATOR, 2)

    def set_behavior(self, category=locators.WHO_BEHAVIOR_SEARCH_TV_LOCATOR,
                     subcategory=locators.WHO_BEHAVIOR_SEARCH_TV_MEDIUM_LOCATOR):
        self.click(self.locators.EXPAND_WHO_BEHAVIOR_LOCATOR)
        self.click(category)
        self.click(subcategory)

    def set_interests(self, category=locators.WHO_INTERESTS_SEARCH_AUTO_LOCATOR,
                      subcategory=locators.WHO_INTERESTS_SEARCH_AUTO_SUV_LOCATOR):
        self.click(self.locators.EXPAND_WHO_INTERESTS_LOCATOR)
        self.click(category)
        self.click(subcategory)

    def set_context(self, category='Гусь', phrase='купить гуся', minus='утка',
                    period='1d'):
        self.click(self.locators.EXPAND_WHO_CONTEXT_LOCATOR)
        self.fill_field(self.locators.WHO_CONTEXT_SEARCH_LOCATOR, category)
        self.fill_field(self.locators.WHO_CONTEXT_SEARCH_PHRASES_LOCATOR, phrase)
        self.click(self.locators.WHO_CONTEXT_PICKUP_LOCATOR)
        self.wait(self.locators.WHO_CONTEXT_LOAD_MORE_LOCATOR)
        self.fill_field(self.locators.WHO_CONTEXT_MINUS_LOCATOR, minus)
        self.fill_field(self.locators.WHO_CONTEXT_PERIOD_LOCATOR, period)
        self.click(self.locators.WHO_CONTEXT_CREATE_LOCATOR)

    # после выбора формата окно перестаёт быть доступным
    # def set_groups(self, name='https://vk.com'):
    #     self.click(self.locators.EXPAND_WHO_GROUPS_LOCATOR)
    #     self.fill_field(self.locators.WHO_GROUPS_SEARCH_LOCATOR, name)
    #     self.wait().until(EC.presence_of_element_located(self.locators.WHO_GROUPS_SEARCH_BUBBLE_LOCATOR))
    #     self.click(self.locators.WHO_GROUPS_SEARCH_CHOOSE_ALL_LOCATOR)
    #     self.click(self.locators.WHO_GROUPS_CREATE_LOCATOR)

    def set_segments(self):
        self.click(self.locators.EXPAND_WHO_SEGMENTS_LOCATOR)
        self.click(self.locators.WHO_SEGMENTS_CHECKBOX_LOCATOR)
        self.click(self.locators.WHO_SEGMENTS_CHECKBOX_LOCATOR)

    def set_schedule_of_display(self):
        self.click(self.locators.EXPAND_SCHEDULE_OF_DISPLAY_LOCATOR)
        self.click(self.locators.SCHEDULE_OF_DISPLAY_WEEKEND_LOCATOR)

    def set_schedule_of_company(self, fr='10.06.2021', to='11.06.2021'):
        self.click(self.locators.EXPAND_SCHEDULE_OF_COMPANY_LOCATOR)
        self.fill_field(self.locators.SCHEDULE_OF_COMPANY_FROM_LOCATOR, fr)
        self.fill_field(self.locators.SCHEDULE_OF_COMPANY_TO_LOCATOR, to)

    def set_model(self, option=locators.PRICE_MODEL_OPTIMIZE_CLICKS_LOCATOR):
        self.click(self.locators.EXPAND_PRICE_MODEL_LOCATOR)
        self.click(option)

    # не успеваю задебажить :(
    #def set_budget(self, per_day="100", total="1000"):
    #    self.fill_field(self.locators.PRICE_BUDGET_PER_DAY_LOCATOR, per_day)
    #    self.fill_field(self.locators.PRICE_BUDGET_TOTAL_LOCATOR, total)

    def choose_format(self, option=locators.FORMAT_CAROUSEL_LOCATOR):
        self.click(option)

    def file_upload_slides(self, file_path, input_locator=locators.ADS_SLIDE_UPLOAD_LOCATOR):
        self.upload(input_locator,file_path)
        self.click(self.locators.ADS_UNIVERSAL_SAVE_BUTTON)

    def set_slides(self, url='https://en.wikipedia.org/wiki/Goose', title='Бу!Гуси',
                   text = 'Текст про гусей'):
        self.fill_field(self.locators.ADS_SLIDE_URL_LOCATOR, url)
        self.fill_field(self.locators.ADS_SLIDE_TITLE_LOCATOR, title)
        self.fill_field(self.locators.ADS_SLIDE_TEXT_LOCATOR, text)

    def file_upload_common(self, file_path, input_locator=locators.ADS_COMMON_UPLOAD_LOCATOR):
        self.upload(input_locator,file_path)
        self.click(self.locators.ADS_UNIVERSAL_SAVE_BUTTON)

    def set_common(self, url='https://en.wikipedia.org/wiki/Goose', title='Бу!',
                   text='Текст'):
        self.fill_field(self.locators.ADS_COMMON_URL_LOCATOR, url)
        self.fill_field(self.locators.ADS_COMMON_TITLE_LOCATOR, title)
        self.fill_field(self.locators.ADS_COMMON_TEXT_LOCATOR, text)

    def set_all_slides(self, file_path_1, file_path_2):
        for locator in [self.locators.ADS_SLIDE1_LOCATOR,
                        self.locators.ADS_SLIDE2_LOCATOR,
                        self.locators.ADS_SLIDE3_LOCATOR]:
            self.click(locator)
            self.file_upload_slides(file_path_1)
            self.set_slides()
            self.file_upload_common(file_path_2)
            self.set_common()

    def save_campaign(self):
        self.click(self.locators.ADS_SAVE_LOCATOR)
        self.wait().until(EC.presence_of_element_located(self.locators.PREVIEW_LOCATOR))
        self.click(self.locators.SAVE_CAMPAIGN_LOCATOR)


