from Locators.homepage_locators import homepage_locators
from _wraper.webelements import Webelement
from _data.data import homepagedata



class Homepage_mmt(Webelement):

    @staticmethod
    def logo_mmt():
        return homepage_locators.MMT_LOGO

    @staticmethod
    def list_your_property():
        return homepage_locators.LIST_YOUR_PROPERTY

    @staticmethod


    def logo_visablity_and_navigation(self):
        assert Webelement.is_element_displayed(Homepage_mmt.logo_mmt(),"xpath"), "make my trip logo logo is not displayed"
        assert Webelement.verify_page_refresh(Homepage_mmt.logo_mmt(),"xpath"), "page not refreshed on mmt logo"

    def list_your_property_hyperlink(self):
        assert Webelement.is_element_displayed(Homepage_mmt.list_your_property(),"xpath"), "list you propert hyperlink is not displayed"
        assert Webelement.verify_new_tab(Homepage_mmt.list_your_property(),"xpath")==homepagedata.list_your_properties_pageTitle
        Homepage_mmt.close_current_tab()
    def  introducing_mybiz(self):
        assert Webelement.is_element_displayed((homepage_locators.LIST_YOUR_PROPERTY,))