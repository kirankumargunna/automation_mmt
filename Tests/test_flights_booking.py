import pytest 
import allure
from Pages.HomePage import Homepage_mmt
from Pages.base_page import BasePageFragments
from Pages.flightspage import flights_MMT
from _data.data import flightpageData as FD, homepagedata as HD



class Test_mmt_flightapage(BasePageFragments):

    @allure.title("flight page smoke test")
    @allure.description("To verify all the elements are loaded in the flight search page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.flightpage
    @pytest.mark.smoke
    def test_smoketest_flightpage(self):

        

        # search for the flights in home page 
        BasePageFragments.close_login_model(self)
        Homepage_mmt.flight_search(self)

        #verfiy mmt logo is visable and navigates to home page on clicking 
        flights_MMT.logo_visability_and_navigation_in_pages(self)

        # verify that search bar is displayed 
        flights_MMT.verify_search_bar_flightPage(self)

        # verify the filter filter type bar is present 

        flights_MMT.verify_fareType_bar(self)

        #verify the avilable filters in the filghts page

        Avilable_Filters=flights_MMT.avilableFilters(self)

        missing = set(FD.Filters) - set(Avilable_Filters)  # Elements in FD.Filters but not in Avilable_Flights
        extra = set(Avilable_Filters) - set(FD.Filters)  # Elements in Avilable_Flights but not in FD.Filters

        assert sorted(Avilable_Filters) == sorted(FD.Filters), f"Missing: {missing}, Extra: {extra}"

        #verify the avilable icons in the filghts page sticky header

        Avilable_icons=flights_MMT.avilable_icons_stick_yHeader(self)

        missing = set(HD.elements_navigation_bar) - set(Avilable_icons)  # Elements in FD.Filters but not in Avilable_Flights
        extra = set(Avilable_icons) - set(HD.elements_navigation_bar)  # Elements in Avilable_Flights but not in FD.Filters

        assert sorted(Avilable_icons) == sorted(HD.elements_navigation_bar), f"Missing: {missing}, Extra: {extra}"




    @pytest.mark.flightpage
    def test_flight_search_valid_data(self):

        BasePageFragments.close_login_model(self)
        #search for flight with valid data in home page 
        Homepage_mmt.flight_search(self)

        #verfiy search button is disabled initally
        assert not flights_MMT.verfiy_search_button_status(self) , "search button in disabled intially"

        #select trip type
        flights_MMT.select_trip_type(self,FD.Trip_types[1])

        # enter to and from city 

        flights_MMT.enter_to_and_from_city(self)

        # verify search button is enabled 
        assert  flights_MMT.verfiy_search_button_status(self) , "search button in enabled"

        #enter date 

        flights_MMT.select_date(self)

        #click search button 
        flights_MMT.click_search_button(self)

