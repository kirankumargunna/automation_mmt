import pytest 
import allure
from Tests.test_mmt_homepage import Test_mmt_homepage



class Test_mmt_flightapage(Test_mmt_homepage):

    @allure.title("flight page smoke test")
    @allure.description("To verify all the elements are loaded in the flight search page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.flightpage
    @pytest.mark.smoke
    def test_smoketest_flightpage(self):

        #close the login prompt after opened 
        Test_mmt_homepage.close_login_model(self)

        
