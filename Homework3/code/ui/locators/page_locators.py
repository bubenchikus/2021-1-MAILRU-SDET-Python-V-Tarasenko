from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_START_LOCATOR = (By.XPATH, "//*[(text()='Войти')]")
    LOGIN_MAIL_LOCATOR = (By.NAME, 'email')
    LOGIN_PASSWORD_LOCATOR = (By.NAME, 'password')
    LOGIN_SUBMIT_LOCATOR = (By.XPATH, "//*[(text()='Войти') and contains(@class, 'authForm')]")


class MainPageLocators(BasePageLocators):

    LOGOUT_START_LOCATOR = (By.XPATH, "//*[contains(@class, 'right-module-mail')]")
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//*[contains(text(), 'Выйти')]")

    DASHBOARD_CONTENT = (By.XPATH, "//*[contains(@class, 'instruction-module-container')]")
    DASHBOARD_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//*[(text()='Создайте рекламную кампанию')]")
    DASHBOARD_ALTERNATIVE_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//*[(text()='Создать кампанию'))]")

    HEAD_SEGMENTS_LOCATOR = (By.XPATH, "//*[contains(@class, 'segments')]")

    CAMPAIGN_CHOOSE_ALL_LOCATOR = (By.XPATH, "//input[contains(@class,'name-module')]")
    CAMPAIGN_ACTION_LOCATOR = (By.XPATH, "//*[contains(@class,'massActionsSelect')]")
    CAMPAIGN_DELETE_LOCATOR = (By.XPATH, "//*[(text()='Удалить')]")
    CAMPAIGN_SEARCH_LOCATOR = (By.XPATH, "//*[(@placeholder='Поиск...')]")
    CAMPAIGN_OPTION_LIST_LOCATOR = (By.XPATH, "//*[contains(@class,'optionsList-module-item')]")
    CAMPAIGN_TABLE_FRAGMENT_LOCATOR = (By.XPATH, "//*[(text()='Название')]")
    CAMPAIGN_SHOW_LOCATOR = (By.XPATH, "//*[contains(@class, 'select-module-item-')]")


class NewCampaignPageLocators(MainPageLocators):

    GOAL_TRAFFIC_LOCATOR = (By.XPATH, "//*[contains(@class, 'traffic')]")
    URL_LOCATOR = (By.XPATH, "//*[(@placeholder='Введите ссылку')]")
    FOOTER_LOCATOR = (By.XPATH, "//*[(@class='footer')]")
    MAPBOX = (By.XPATH, "//*[(@href='https://www.mapbox.com/')]")
    NAME_LOCATOR = (By.XPATH, "//*[contains(@class, 'input_campaign-name')]//input")

    EXPAND_WHO_SEX_LOCATOR = (By.XPATH, "//*[(@data-targeting='sex')]")
    WHO_SEX_CHECKBOX_M_LOCATOR = (By.XPATH, "//*[(@targeting='sex-male')]//following-sibling::label")
    WHO_SEX_CHECKBOX_F_LOCATOR = (By.XPATH, "//*[(@targeting='sex-female')]//following-sibling::label")

    EXPAND_WHO_AGE_LOCATOR = (By.XPATH, "//*[(@data-targeting='age')]")
    WHO_AGE_CHECKBOX_LOCATOR = (By.XPATH, "//*[contains(text(), 'Охватить')]//preceding-sibling::*")
    WHO_AGE_SELECT_LOCATOR = (By.XPATH, "//*[(@class='select')]")
    WHO_AGE_SELECT_ALL_LOCATOR = (By.XPATH, "//*[(@data-id='all')]")
    WHO_AGE_SELECT_SELECTED_LOCATOR = (By.XPATH, "//*[(@data-id='selected')]")
    WHO_AGE_SELECT_UNKNOWN_LOCATOR = (By.XPATH, "//*[(@data-id='unknown')]")
    # WHO_AGE_SELECT_CUSTOM_LOCATOR = (By.XPATH, "//*[(@data-id='custom')]")

    EXPAND_WHO_GEOGRAPHY_LOCATOR = (By.XPATH, "//*[(@data-targeting='geo')]")
    WHO_GEOGRAPHY_RADIO_REGION_LOCATOR = (By.XPATH, "//*[(@type='radio') and (@value='region')]")
    WHO_GEOGRAPHY_RADIO_LOCAL_LOCATOR = (By.XPATH, "//*[(@type='radio') and (@value='local')]")
    WHO_GEOGRAPHY_ADD_WITH_FIELD_LOCATOR = (By.XPATH, "//*[contains(@placeholder, 'Добавить или исключить')]")
    WHO_GEOGRAPHY_ADD_WITH_FIELD_CONFIRM_LOCATOR = (By.XPATH, "//*[(text()='Добавить')]")
    WHO_GEOGRAPHY_ADD_WITH_BUTTON_LOCATOR = (By.XPATH, "//*[(text()='Добавить несколько...')]")
    WHO_GEOGRAPHY_RESET_LOCATOR = (By.XPATH, "//*[(text()='Сбросить всё')]")

    EXPAND_WHO_BEHAVIOR_LOCATOR = (By.XPATH, "//*[(@data-targeting='interests_soc_dem')]")
    WHO_BEHAVIOR_SEARCH_LOCATOR = (By.XPATH, "//*[@data-name='interests_soc_dem']//*[(@placeholder='Искать...')]")
    WHO_BEHAVIOR_SEARCH_TV_LOCATOR = (By.XPATH, "//*[(text()='Группы телесмотрения')]//preceding-sibling::span")
    WHO_BEHAVIOR_SEARCH_TV_MEDIUM_LOCATOR = (By.XPATH, "//*[(@title='Смотрят ТВ cредне')]")

    EXPAND_WHO_INTERESTS_LOCATOR = (By.XPATH, "//*[(@data-targeting='interests')]")
    WHO_INTERESTS_SEARCH_LOCATOR = (By.XPATH, "//*[@data-name='interests']//*[(@placeholder='Искать...')]")
    WHO_INTERESTS_SEARCH_AUTO_LOCATOR = (By.XPATH, "//*[(@title='Авто')]//preceding-sibling::span")
    WHO_INTERESTS_SEARCH_AUTO_SUV_LOCATOR = (By.XPATH, "//*[(@title='Авто внедорожники')]")

    EXPAND_WHO_CONTEXT_LOCATOR = (By.XPATH, "//*[(@data-targeting='context')]")
    WHO_CONTEXT_SEARCH_LOCATOR = (By.XPATH, "//*[(text()='Например: платье, холодильник')]//preceding-sibling::input")
    WHO_CONTEXT_SEARCH_PHRASES_LOCATOR = (By.XPATH, "//*[contains(@placeholder, 'Введите фразы, по которым ищут')]")
    WHO_CONTEXT_PICKUP_LOCATOR = (By.XPATH, "//*[(text()='Подобрать')]")
    WHO_CONTEXT_LOAD_MORE_LOCATOR = (By.XPATH, "//*[(text()='Загрузить еще')]")
    WHO_CONTEXT_MINUS_LOCATOR = (By.XPATH, "//*[contains(@placeholder, 'минус-фразы')]")
    WHO_CONTEXT_PERIOD_LOCATOR = (By.XPATH, "//*[contains(@class, 'inputPeriod')]")
    WHO_CONTEXT_CREATE_LOCATOR = (By.XPATH, "//*[(text()='Создать')]")

    EXPAND_WHO_GROUPS_LOCATOR = (By.XPATH, "//*[(@data-targeting='appsAndGroups')]")
    WHO_GROUPS_SEARCH_LOCATOR = (By.XPATH, "//*[contains(@placeholder, 'название группы/приложения')]")
    WHO_GROUPS_SEARCH_BUBBLE_LOCATOR = (By.XPATH, "//*[contains(@class,'module-bubble')]")
    WHO_GROUPS_SEARCH_CHOOSE_ALL_LOCATOR = (By.XPATH, "(//*[(text()='Выбрать все')])[1]")
    WHO_GROUPS_CREATE_LOCATOR = (By.XPATH, "//*[contains(@class,'module-group')]//*[contains(@class,'blue')]")

    EXPAND_WHO_SEGMENTS_LOCATOR = (By.XPATH, "//*[(@data-targeting='segments')]")
    WHO_SEGMENTS_CHECKBOX_LOCATOR = (By.XPATH, "(//*[(@type='checkbox') and contains(@class, 'segmentsSetting')])[1]")

    EXPAND_SCHEDULE_OF_DISPLAY_LOCATOR = (By.XPATH, "//*[(@data-targeting='fulltime')]")
    SCHEDULE_OF_DISPLAY_WEEKEND_LOCATOR = (By.XPATH, "//*[(text()='Выходные')]")

    EXPAND_SCHEDULE_OF_COMPANY_LOCATOR = (By.XPATH, "//*[(@data-targeting='date')]")
    SCHEDULE_OF_COMPANY_FROM_LOCATOR = (By.XPATH, "//*[contains(@class, 'date-from')]//*[contains(@class, 'input')]")
    SCHEDULE_OF_COMPANY_TO_LOCATOR = (By.XPATH, "//*[contains(@class, 'date-to')]//*[contains(@class, 'input')]")

    EXPAND_PRICE_MODEL_LOCATOR = (By.XPATH, "//*[(@data-targeting='autobidding_mode')]")
    PRICE_MODEL_OPTIMIZE_CLICKS_LOCATOR = (By.XPATH, "//*[(text()='Клики')]")

    EXPAND_PRICE_BUDGET_LOCATOR = (By.XPATH, "//*[(@data-targeting='budget_setting')]")
    PRICE_BUDGET_WINDOW_LOCATOR = (By.XPATH, "//*[(@class='budget-setting')]")
    PRICE_BUDGET_PER_DAY_LOCATOR = (By.XPATH, "//input[(@data-test_ui='budget-per_day')]")
    PRICE_BUDGET_TOTAL_LOCATOR = (By.XPATH, "//input[(@data-test_ui='budget-total')]")

    FORMAT_CAROUSEL_LOCATOR = (By.XPATH, "//*[(@id='patterns_26')]")

    ADS_SLIDE_UPLOAD_LOCATOR = (By.XPATH, "//input[contains(@data-test_ui,'600x600')]")
    ADS_SLIDE_URL_LOCATOR = (By.XPATH, "//*[(@placeholder='Введите ссылку для слайда')]")
    ADS_SLIDE_TITLE_LOCATOR = (By.XPATH, "//*[(@placeholder='Введите заголовок слайда')]")
    ADS_SLIDE_TEXT_LOCATOR = (By.XPATH, "//*[(@placeholder='Введите текст слайда (необязательно)')]")

    ADS_SLIDE1_LOCATOR = (By.XPATH, "//*[(text()='1')]")
    ADS_SLIDE2_LOCATOR = (By.XPATH, "//*[(text()='2')]")
    ADS_SLIDE3_LOCATOR = (By.XPATH, "//*[(text()='3')]")

    ADS_COMMON_UPLOAD_LOCATOR = (By.XPATH, "//input[contains(@data-test_ui,'256x256')]")
    ADS_COMMON_URL_LOCATOR = (By.XPATH, "//*[(@placeholder='Введите адрес ссылки')]")
    ADS_COMMON_TITLE_LOCATOR = (By.XPATH, "//*[(@placeholder='Введите заголовок объявления')]")
    ADS_COMMON_TEXT_LOCATOR = (By.XPATH, "//*[(@placeholder='Введите текст объявления')]")

    ADS_UNIVERSAL_SAVE_BUTTON = (By.XPATH, "//*[(@value='Сохранить изображение')]")
    ADS_SAVE_LOCATOR = (By.XPATH, "//*[(@data-test_ui='submit_banner_button')]")

    PREVIEW_LOCATOR = (By.XPATH, "//*[contains(@class, 'bannerPreview-module-previewWrap')]")

    SAVE_CAMPAIGN_LOCATOR = (By.XPATH, "//*[(text()='Создать кампанию')]//parent::button")


class SegmentsPageLocators(MainPageLocators):

    SEGMENTS_CREATE_LOCATOR = (By.XPATH, "//*[(text()='Создайте')]")
    SEGMENTS_ALTERNATIVE_CREATE_LOCATOR = (By.XPATH, "//*[(text()='Создать сегмент')]")
    SEGMENTS_CREATE_APPS_LOCATOR = (By.XPATH, "//*[(text()='Приложения и игры в соцсетях') and "
                                              "contains(@class, 'adding')]")
    SEGMENTS_CREATE_GAMERS_LOCATOR = (By.XPATH, "//*[(text()='Игравшие и платившие в платформе')]")
    SEGMENTS_CREATE_GAMERS_CHOOSE_LOCATOR = (By.XPATH, "//*[(text()='Игравшие в платформе')]")
    SEGMENTS_CREATE_ADD_LOCATOR = (By.XPATH, "//*[(text()='Добавить сегмент')]//parent::button")
    SEGMENTS_CREATE_NAME_LOCATOR = (By.XPATH, "//*[contains(@class, 'input_create')]//input[(@type='text')]")
    SEGMENTS_CREATE_SUBMIT_LOCATOR = (By.XPATH, "//*[(@data-class-name='Submit')]")

    SEGMENTS_TABLE_FRAGMENT_LOCATOR = (By.XPATH, "//*[(text()='Имя сегмента')]")
    SEGMENTS_ACTION_LOCATOR = (By.XPATH, "//*[contains(@class,'massAction')]")
    SEGMENTS_CHOOSE_ALL_LOCATOR = (By.XPATH, "//*[contains(@class,'Header')]//*[contains(@class, 'idCellCheckbox')]")
    SEGMENTS_DELETE_LOCATOR = (By.XPATH, "//*[(text()='Удалить')]")
    SEGMENTS_SEARCH_LOCATOR = (By.XPATH, "//*[(@placeholder='Поиск по названию или id...')]")
    SEGMENTS_SEARCH_BLOCK_LOCATOR = (By.XPATH, "//*[contains(@class,'optionsList-module-optionsList')]")
    SEGMENTS_OPTION_LIST_LOCATOR = (By.XPATH, "//*[contains(@class, 'optionsList-module-option-'))]")


FLAG_SEGMENTS_LOCATOR = (By.XPATH, "//*[contains(text(), 'Аудиторные сегменты')]")
FLAG_BILLING_LOCATOR = (By.XPATH, "//*[@data-type='deposit']")
