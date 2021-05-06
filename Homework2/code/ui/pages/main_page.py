from ui.pages.base_page import BasePage
from ui.locators.page_locators import MainPageLocators


class MainPage(BasePage):

    locators = MainPageLocators()

    def go_to_campaign_list_page(self):
        self.driver.get('https://target.my.com/dashboard')
        self.find(self.locators.CAMPAIGN_TABLE_FRAGMENT_LOCATOR)  # waiting for table to load

    def go_to_new_campaign_page(self):
        self.driver.get('https://target.my.com/campaign/new')

    def go_to_segments_page(self):
        self.driver.get('https://target.my.com/segments/segments_list')

    def delete_campaigns(self):
        self.click(self.locators.CAMPAIGN_CHOOSE_ALL_LOCATOR)
        self.click(self.locators.CAMPAIGN_ACTION_LOCATOR)
        self.click(self.locators.CAMPAIGN_DELETE_LOCATOR)
