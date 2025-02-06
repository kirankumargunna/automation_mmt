from typing import List

from selenium.webdriver.remote.webelement import WebElement

from Locators.flightPage_locators import flightPage_locators
from Pages.base_page import BasePageFragments


class flights_MMT(BasePageFragments):

    search_bar=flightPage_locators.SEARCH_BAR


    def verfy_search_bar_flightPage(self):
        assert WebElement.find_element(flights_MMT.search_bar) , "search bar is not dispaled in flight page"
