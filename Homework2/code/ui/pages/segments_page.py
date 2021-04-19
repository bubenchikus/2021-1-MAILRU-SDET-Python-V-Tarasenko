from ui.pages.base_page import BasePage
from ui.locators.page_locators import SegmentsPageLocators


class SegmentsPage(BasePage):

    locators = SegmentsPageLocators()

    def go_to_create_new_segment(self):
        self.driver.get('https://target.my.com/segments/segments_list/new/')

    def create_segment(self, segment_name):
        self.go_to_create_new_segment()
        self.click(self.locators.SEGMENTS_CREATE_APPS_LOCATOR)
        self.click(self.locators.SEGMENTS_CREATE_GAMERS_LOCATOR)
        self.click(self.locators.SEGMENTS_CREATE_GAMERS_CHOOSE_LOCATOR)
        self.click(self.locators.SEGMENTS_CREATE_ADD_LOCATOR)
        self.fill_field(self.locators.SEGMENTS_CREATE_NAME_LOCATOR, segment_name)
        self.click(self.locators.SEGMENTS_CREATE_SUBMIT_LOCATOR)
        self.find(self.locators.SEGMENTS_SEARCH_LOCATOR)  # wait segments list page content to load

    def delete_segments(self):
        self.find(self.locators.SEGMENTS_TABLE_FRAGMENT_LOCATOR)
        self.click(self.locators.SEGMENTS_CHOOSE_ALL_LOCATOR)
        self.click(self.locators.SEGMENTS_ACTION_LOCATOR)
        self.click(self.locators.SEGMENTS_DELETE_LOCATOR)
