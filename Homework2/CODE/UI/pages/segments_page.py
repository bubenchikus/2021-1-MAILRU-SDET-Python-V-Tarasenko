from CODE.UI.pages.base_page import BasePage
from CODE.UI.locators.page_locators import SegmentsPageLocators
from selenium.common.exceptions import NoSuchElementException


class SegmentsPage(BasePage):

    locators = SegmentsPageLocators()

    def create_segment(self, segment_name='gus-segment'):
        self.click(self.locators.SEGMENTS_CREATE_LOCATOR)
        self.click(self.locators.SEGMENTS_CREATE_APPS_LOCATOR)
        self.click(self.locators.SEGMENTS_CREATE_GAMERS_LOCATOR)
        self.click(self.locators.SEGMENTS_CREATE_GAMERS_CHOOSE_LOCATOR)
        self.click(self.locators.SEGMENTS_CREATE_ADD_LOCATOR)
        self.fill_field(self.locators.SEGMENTS_CREATE_NAME_LOCATOR, segment_name)
        self.click(self.locators.SEGMENTS_CREATE_SUBMIT_LOCATOR)

    def check_segment(self, segment_name='gus-segment'):
        self.fill_field(self.locators.SEGMENTS_SEARCH_LOCATOR, segment_name)
        try:
            self.driver.find_element_by_xpath(self.locators.SEGMENTS_OPTION_LIST_LOCATOR[1])
        except NoSuchElementException:
            print('No search results...')

    def delete_segment(self):
        self.click(self.locators.SEGMENTS_CHOOSE_ALL_LOCATOR)
        self.click(self.locators.SEGMENTS_ACTION_LOCATOR)
        self.click(self.locators.SEGMENTS_DELETE_LOCATOR)
