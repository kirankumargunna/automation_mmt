
from Locators.homepage_locators import homepage_locators
from _wraper.webelements import Webelement


class BasePageFragments(Webelement):

    close_loginModel=homepage_locators.close_login_modal
    login_mobilenumber=homepage_locators.LOGIN_MOBILE_NUMBER


    def close_login_model(self):
        Webelement.wait_for_element_presence(BasePageFragments.close_loginModel)
        Webelement.is_element_displayed(BasePageFragments.login_mobilenumber)
        Webelement.click_element(BasePageFragments.close_loginModel)











