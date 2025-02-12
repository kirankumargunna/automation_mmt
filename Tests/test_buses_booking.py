import pytest 
import allure
from Pages.HomePage import Homepage_mmt
from Pages.base_page import BasePageFragments
from Pages.BusesPage import Buses_mmt
from _data.data import flightpageData as FD, homepagedata as HD



class Test_mmt_busespage(BasePageFragments):

    @allure.title("buses page smoke test")
    @allure.description("To verify all the elements are loaded in the buses search page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.busespage
    @pytest.mark.smoke
    def test_smoketest_busespage(self):

        # search for buses in homepage
        BasePageFragments.close_login_model(self)
        Homepage_mmt.bus_search(self)

        #verfiy mmt logo is visable and navigates to home page on clicking 
        Buses_mmt.logo_visability_and_navigation_in_pages(self)

        
