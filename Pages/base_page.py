from Locators.homepage_locators import homepage_locators
from _wraper.webelements import Webelement


class BasePageFragments(Webelement):



    # @staticmethod
    # def logo_mmt():
    #     return homepage_locators.MMT_LOGO

    @staticmethod
    def login_model(cls):
        return homepage_locators.close_login_modal


    def close_login_model(self):
        Webelement.click_element(self.login_model,"xpath")











