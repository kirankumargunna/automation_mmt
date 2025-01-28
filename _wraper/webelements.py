from Drivers.webdrivers import Webdrivers
from selenium.webdriver.common.by import By


class Webelement(Webdrivers):

    @classmethod
    def findElement(cls, element_locator, selector="xpath"):

        """
        returns web element for given element locator

        :return: webelement
        """
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return cls._browser.find_element(By.XPATH,element_locator)
        if selector == "id":
            return cls._browser.find_element(By.ID,element_locator)
        if selector == "link text":
            return cls._browser.find_element(By.LINK_TEXT,element_locator)
        if selector == "partial link text":
            return cls._browser.find_element(By.PARTIAL_LINK_TEXT,element_locator)
        if selector == "name":
            return cls._browser.find_element(By.NAME,element_locator)
        if selector == "tag name":
            return cls._browser.find_element(By.TAG_NAME,element_locator)
        if selector == "class name":
            return cls._browser.find_element(By.CLASS_NAME,element_locator)
        if selector == "css selector":
            return cls._browser.find_element(By.CSS_SELECTOR,element_locator)

    @classmethod
    def findElements(cls, element_locator, selector="xpath"):

        """
        returns web element for given element locator

        :return: webelement
        """
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return cls._browser.find_elements(By.XPATH, element_locator)
        if selector == "id":
            return cls._browser.find_elements(By.ID, element_locator)
        if selector == "link text":
            return cls._browser.find_elements(By.LINK_TEXT, element_locator)
        if selector == "partial link text":
            return cls._browser.find_elements(By.PARTIAL_LINK_TEXT, element_locator)
        if selector == "name":
            return cls._browser.find_elements(By.NAME, element_locator)
        if selector == "tag name":
            return cls._browser.find_elements(By.TAG_NAME, element_locator)
        if selector == "class name":
            return cls._browser.find_elements(By.CLASS_NAME, element_locator)
        if selector == "css selector":
            return cls._browser.find_elements(By.CSS_SELECTOR, element_locator)

    @classmethod
    def click_element(cls,locator,selector):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call pytest_start_browser() first.")
        element=cls.findElement(locator,selector)
        element.click()