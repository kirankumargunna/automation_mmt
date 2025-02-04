
from Locators.homepage_locators import homepage_locators
from _wraper.webelements import Webelement
from _data.data import homepagedata
from _wraper import helper

class BasePageFragments(Webelement):

    close_loginModel=homepage_locators.close_login_modal
    login_mobilenumber=homepage_locators.LOGIN_MOBILE_NUMBER
    travel_date=homepage_locators.DEPATURE


    @classmethod
    def setup_method(cls):
        cls.homepagedata=homepagedata()
        cls.h=helper

    def close_login_model(self):
        Webelement.wait_for_element_visible(BasePageFragments.close_loginModel)
        Webelement.is_element_displayed(BasePageFragments.login_mobilenumber)
        Webelement.click_element(BasePageFragments.close_loginModel)

    def set_date(self):
        Webelement.click_element(BasePageFragments.travel_date)
        self.h.get_date_of_travel()









