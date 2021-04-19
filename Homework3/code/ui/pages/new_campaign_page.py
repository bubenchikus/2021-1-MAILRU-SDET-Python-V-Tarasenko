from ui.pages.main_page import MainPage
from ui.locators.page_locators import NewCampaignPageLocators
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class NewCampaignPage(MainPage):

    locators = NewCampaignPageLocators()

    def choose_goal(self, goal):
        if goal.lower() == 'traffic':
            self.click(self.locators.GOAL_TRAFFIC_LOCATOR)

    def fill_url(self, url):
        self.fill_field(self.locators.URL_LOCATOR, url)

    def fill_name(self, name):
        self.wait().until(EC.presence_of_element_located(self.locators.FOOTER_LOCATOR))
        self.wait().until(EC.presence_of_element_located(self.locators.MAPBOX))
        self.click(self.locators.EXPAND_WHO_GEOGRAPHY_LOCATOR)
        self.fill_field(self.locators.NAME_LOCATOR, name)

    def set_sex(self, sex):
        self.click(self.locators.EXPAND_WHO_SEX_LOCATOR)
        if sex.lower() == 'мужчины':
            self.click(self.locators.WHO_SEX_CHECKBOX_F_LOCATOR)  # unselecting checkbox
        elif sex.lower() == 'женщины':
            self.click(self.locators.WHO_SEX_CHECKBOX_M_LOCATOR)

    def set_age(self, age):
        self.click(self.locators.EXPAND_WHO_AGE_LOCATOR)
        self.click(self.locators.WHO_AGE_CHECKBOX_LOCATOR)
        self.click(self.locators.WHO_AGE_SELECT_LOCATOR)
        if age.lower() == 'неизвестный возраст':
            self.click(self.locators.WHO_AGE_SELECT_UNKNOWN_LOCATOR)

    def set_geography(self, option, region):
        self.click(self.locators.EXPAND_WHO_GEOGRAPHY_LOCATOR)
        if option.lower() == 'города и регионы':
            self.click(self.locators.WHO_GEOGRAPHY_RADIO_REGION_LOCATOR)
            self.fill_field(self.locators.WHO_GEOGRAPHY_ADD_WITH_FIELD_LOCATOR, region)
            self.click(self.locators.WHO_GEOGRAPHY_ADD_WITH_FIELD_CONFIRM_LOCATOR, 2)

    def set_behavior(self, category, subcategory):
        self.click(self.locators.EXPAND_WHO_BEHAVIOR_LOCATOR)
        if category.lower() == 'группы телесмотрения':
            self.click(self.locators.WHO_BEHAVIOR_SEARCH_TV_LOCATOR)
            if subcategory == 'смотрят тв средне':
                self.click(self.locators.WHO_BEHAVIOR_SEARCH_TV_MEDIUM_LOCATOR)

    def set_interests(self, category, subcategory):
        self.click(self.locators.EXPAND_WHO_INTERESTS_LOCATOR)
        if category.lower() == 'авто':
            self.click(self.locators.WHO_INTERESTS_SEARCH_AUTO_LOCATOR)
            if subcategory.lower() == 'авто внедорожники':
                self.click(self.locators.WHO_INTERESTS_SEARCH_AUTO_SUV_LOCATOR)

    def set_context(self, category, phrase, minus, period):
        self.click(self.locators.EXPAND_WHO_CONTEXT_LOCATOR)
        self.fill_field(self.locators.WHO_CONTEXT_SEARCH_LOCATOR, category)
        self.fill_field(self.locators.WHO_CONTEXT_SEARCH_PHRASES_LOCATOR, phrase)
        self.click(self.locators.WHO_CONTEXT_PICKUP_LOCATOR)
        self.wait(self.locators.WHO_CONTEXT_LOAD_MORE_LOCATOR)
        self.fill_field(self.locators.WHO_CONTEXT_MINUS_LOCATOR, minus)
        self.fill_field(self.locators.WHO_CONTEXT_PERIOD_LOCATOR, period)
        self.click(self.locators.WHO_CONTEXT_CREATE_LOCATOR)

    def set_segments(self):
        self.click(self.locators.EXPAND_WHO_SEGMENTS_LOCATOR)
        self.click(self.locators.WHO_SEGMENTS_CHECKBOX_LOCATOR)

    def set_schedule_of_display(self):
        self.click(self.locators.EXPAND_SCHEDULE_OF_DISPLAY_LOCATOR)
        self.click(self.locators.SCHEDULE_OF_DISPLAY_WEEKEND_LOCATOR)

    def set_schedule_of_company(self, fr, to):
        self.click(self.locators.EXPAND_SCHEDULE_OF_COMPANY_LOCATOR)
        self.fill_field(self.locators.SCHEDULE_OF_COMPANY_FROM_LOCATOR, fr)
        self.fill_field(self.locators.SCHEDULE_OF_COMPANY_TO_LOCATOR, to)

    def set_model(self, model):
        self.click(self.locators.EXPAND_PRICE_MODEL_LOCATOR)
        if model.lower() == 'клики':
            self.click(self.locators.PRICE_MODEL_OPTIMIZE_CLICKS_LOCATOR)

    def set_budget(self, per_day, total):
        self.fill_field(self.locators.PRICE_BUDGET_PER_DAY_LOCATOR, per_day)
        self.fill_field(self.locators.PRICE_BUDGET_TOTAL_LOCATOR, total)

    def choose_format(self, frmt):
        if frmt.lower() == 'карусель':
            self.click(self.locators.FORMAT_CAROUSEL_LOCATOR)

    def file_upload_slides(self, file_path):
        self.upload(self.locators.ADS_SLIDE_UPLOAD_LOCATOR, file_path)
        self.click(self.locators.ADS_UNIVERSAL_SAVE_BUTTON)

    def set_slides(self, url, title, text):
        self.fill_field(self.locators.ADS_SLIDE_URL_LOCATOR, url)
        self.fill_field(self.locators.ADS_SLIDE_TITLE_LOCATOR, title)
        self.fill_field(self.locators.ADS_SLIDE_TEXT_LOCATOR, text)

    def file_upload_common(self, file_path):
        self.upload(self.locators.ADS_COMMON_UPLOAD_LOCATOR, file_path)
        self.click(self.locators.ADS_UNIVERSAL_SAVE_BUTTON)

    def set_common(self, url, title, text):
        self.fill_field(self.locators.ADS_COMMON_URL_LOCATOR, url)
        self.fill_field(self.locators.ADS_COMMON_TITLE_LOCATOR, title)
        self.fill_field(self.locators.ADS_COMMON_TEXT_LOCATOR, text)

    def set_all_slides(self, file_path_1, slides_url, slides_title, slides_text,
                       file_path_2, common_url, common_title, common_text):
        for locator in [self.locators.ADS_SLIDE1_LOCATOR,
                        self.locators.ADS_SLIDE2_LOCATOR,
                        self.locators.ADS_SLIDE3_LOCATOR]:
            self.click(locator)
            self.file_upload_slides(file_path_1)
            self.set_slides(slides_url, slides_title, slides_text)
            self.file_upload_common(file_path_2)
            self.set_common(common_url, common_title, common_text)

    def save_campaign(self):
        self.click(self.locators.ADS_SAVE_LOCATOR)
        self.find(self.locators.PREVIEW_LOCATOR)
        time.sleep(2)  # придётся подождать завершения загрузки данных
        self.click(self.locators.SAVE_CAMPAIGN_LOCATOR)

    root = os.path.abspath(os.path.join(__file__, "../../.."))
    default_path_1 = os.path.join(root, "upload", "goose1.jpg")
    default_path_2 = os.path.join(root, "upload", "goose2.jpg")

    def new_campaign_full_process(self, goal='traffic', url='https://en.wikipedia.org/wiki/Goose',
                                  name='My Campaign Name', sex='женщины', age='неизвестный возраст',
                                  geo_option='города и регионы', region='Москва',
                                  behavior_category='группы телесмотрения', behavior_subcategory='смотрят тв средне',
                                  interests_category='авто', interests_subcategory='авто внедорожники',
                                  context_category='Гусь', context_phrase='купить гуся', context_minus='утка',
                                  context_period='1d', schedule_fr='10.06.2021', schedule_to='11.06.2021',
                                  model='клики', budget_per_day='1000', budget_total='1000', frmt='карусель',
                                  slides_url='https://en.wikipedia.org/wiki/Goose', slides_title='Бу!Гуси',
                                  slides_text='Текст про гусей', common_url='https://en.wikipedia.org/wiki/Goose',
                                  common_title='Бу!', common_text='Текст',
                                  path1=default_path_1, path2=default_path_2):
        self.choose_goal(goal)
        self.fill_url(url)
        self.fill_name(name)

        self.set_sex(sex)
        self.set_age(age)
        self.set_geography(geo_option, region)
        self.set_behavior(behavior_category, behavior_subcategory)
        self.set_interests(interests_category, interests_subcategory)
        self.set_context(context_category, context_phrase, context_minus, context_period)
        self.set_segments()
        self.set_schedule_of_display()
        self.set_schedule_of_company(schedule_fr, schedule_to)
        self.set_model(model)
        self.set_budget(budget_per_day, budget_total)

        self.choose_format(frmt)

        self.set_all_slides(path1, slides_url, slides_title, slides_text,
                            path2, common_url, common_title, common_text)
        self.save_campaign()

