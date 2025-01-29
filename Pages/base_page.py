from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from Locators.homepage_locators import homepage_locators
from _wraper.webelements import Webelement


class BasePageFragments(Webelement):



    # @staticmethod
    # def logo_mmt():
    #     return homepage_locators.MMT_LOGO

    @staticmethod
    def login_model():
        return homepage_locators.close_login_modal


    def close_login_model(self):
        Webelement.wait_for_element_presence(BasePageFragments.login_model(),"xpath")
        Webelement.click_element(BasePageFragments.login_model(),"xpath")











