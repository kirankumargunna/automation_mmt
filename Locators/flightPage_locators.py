
from selenium.webdriver.common.by import By

from Locators.Base_locators import Baselocators


class flightPage_locators(Baselocators):

        SEARCH_BAR=(By.ID,'widgetHeader')
        FARETYPE_BAR=(By.XPATH,"//div[@class='fareTypeWrapper']")
        FILTERS_FLIGHTS=(By.XPATH,"//div[@class='filtersOuter']")
        JOURNEY_TITLE = (By.XPATH, "//p[contains(@class,'journey-title')]//span")
        PROMOTION_BANNER = (By.ID, "carouselBanner")
        WEEKLY_FARE_BANNER = (By.ID, 'weeklyFare')
        SORT_BY_TAB = (By.ID, "//div[@class='sortTabsWrapper appendTop20']")
        AVAILABLE_FLIGHTS = (By.XPATH, "//div[@class=' ']")



