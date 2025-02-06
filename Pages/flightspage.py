from typing import List
from selenium.webdriver.support.ui import Select
from _wraper.webelements import Webelement
from Locators.flightPage_locators import flightPage_locators
from Pages.base_page import BasePageFragments


class flights_MMT(BasePageFragments):

    search_bar=flightPage_locators.SEARCH_BAR
    fareType_bar=flightPage_locators.FARETYPE_BAR
    search_button_disabled=flightPage_locators.SEARCH_BUTTON_DISABLED
    search_button_enabled=flightPage_locators.SEARCH_BUTTON_ENABLED
    current_trip_type=flightPage_locators.CURRENT_TRIP_TYPE
    trip_type_dropdown=flightPage_locators.TRIP_TYPE_DROPDOWN


    def verfy_search_bar_flightPage(self):
        assert Webelement.findElement(flights_MMT.search_bar) , "search bar is not dispaled in flight page"

    def verfiy_fareType_bar(self):
        assert Webelement.findElement(flights_MMT.fareType_bar), "fare type bar is not displayed"
    
    def verfiy_search_button_status(self):
        
        if Webelement.findElement(flights_MMT.search_button_enabled):
            return True
        elif Webelement.findElement(flights_MMT.search_button_disabled):
            return False
    def select_trip_type(self,trip_type:str):

        if Webelement.findElement(flights_MMT.current_trip_type).text !=trip_type:
            Webelement.click_element(flights_MMT.current_trip_type)
            element=Webelement.findElement(flights_MMT.trip_type_dropdown)
            dropdown=Select(element)
            dropdown.select_by_visible_text(trip_type)
    def enter_to_and_from_city(self):
        
        


