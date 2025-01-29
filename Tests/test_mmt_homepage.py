from Pages.HomePage import Homepage_mmt
from Pages.base_page import BasePageFragments


class Test_mmt_homepage:

        #navigate to make my trip webpage
        def test_homepage_elements(self):
                BasePageFragments.close_login_model(self)
                Homepage_mmt.logo_visablity_and_navigation(self)
                Homepage_mmt.list_your_property_hyperlink(self)