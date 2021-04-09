from CODE.UI.pages.base_page import BasePage
from CODE.UI.locators.page_locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException

class MainPage(BasePage):

    locators = MainPageLocators()

    def go_to_campaign_page(self):
        option=1
        try:
            self.driver.find_element_by_xpath(self.locators.DASHBOARD_CREATE_CAMPAIGN_LOCATOR[1])
        except NoSuchElementException:
            option+=1
        if option==1:
            self.click(self.locators.DASHBOARD_CREATE_CAMPAIGN_LOCATOR)
        else:
            self.click(self.locators.DASHBOARD_CREATE_CAMPAIGN_ALTERNATIVE_LOCATOR)
        return option

    def check_creation(self, campaign_name):
        self.fill_field(self.locators.CAMPAIGN_SEARCH_LOCATOR, campaign_name)
        try:
            self.driver.find_element_by_xpath(self.locators.CAMPAIGN_OPTION_LIST_LOCATOR[1])
        except NoSuchElementException:
            print('No search results...')

    def go_to_segments_page(self):
        self.click(self.locators.HEAD_SEGMENTS_LOCATOR)





