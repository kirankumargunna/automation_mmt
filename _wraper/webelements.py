import time
from asyncio import timeout

from Drivers.webdrivers import Webdrivers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @classmethod
    def is_element_displayed(cls,locator,selector):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call pytest_start_browser() first.")
        element = cls.findElement(locator, selector)
        return element.is_displayed()

    @classmethod
    def verify_page_refresh(cls,locator,selector):
        """
            Verifies if clicking the logo refreshes the page using window.onbeforeunload.

            Steps:
            1. Injects a JavaScript listener to track page refresh.
            2. Clicks the logo.
            3. Waits for the page reload.
            4. Checks if the page refreshed.

            :param driver: Selenium WebDriver instance
            :param logo_xpath: XPath of the logo element
            :param wait_time: Time to wait for page reload (default: 2 seconds)
            :return: True if the page refreshed, False otherwise
            """
        # Inject JavaScript to set a flag before the page unloads
        cls._browser.execute_script("""
                window.onbeforeunload = function() { 
                    localStorage.setItem('page_refreshed', 'true'); 
                };
            """)

        # tirgger a potential refresh
        element=cls.findElement(locator,selector)
        element.click()

        # wait for the page to refresh
        time.sleep(3)

        # check local storage for refresh dedection
        is_refreshed = cls._browser.execute_script("return localStorage.getItem('page_refreshed') === 'true';")

        # Reset the flag after checking
        cls._browser.execute_script("localStorage.removeItem('page_refreshed');")

        if is_refreshed:
            print("✅ Page refreshed successfully after clicking the logo.")
            return True
        else:
            print("❌ Page did not refresh.")
            return False

    @classmethod
    def verify_new_tab(cls,locator,selector):

        # get the no of tabs before clicking
        initial_tabs=cls._browser.window_handles

        # click the hyperlink (expected to open a new tab)
        element=cls.findElement(locator,selector)
        element.click()

        #wait for the tab to open
        time.sleep(3)

        new_tabs=cls._browser.window_handles
        if len(new_tabs) > len(initial_tabs):
            print("✅ New tab opened successfully.")

            #switch to new tab

            cls._browser.switch_to.window(new_tabs[-1])
            print(cls._browser.title)

            # return the new tap page title

            return cls._browser.title
        else:
            print("❌ No new tab opened.")
            return "No new tab opened "

    @classmethod
    def close_current_tab(cls):
        cls._browser.close()

    @classmethod
    def wait(cls,timeout: int):
        return WebDriverWait(cls._browser,timeout)

    @classmethod
    def wait_for_element_presence(cls, element_locator,  selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.XPATH, element_locator)))
        if selector == "id":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.ID, element_locator)))
        if selector == "link text":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.NAME, element_locator)))
        if selector == "tag name":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return cls.wait(10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_all_elements_presence(cls, elements_locator, selector="xpath"):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        if selector == "xpath":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.XPATH, elements_locator)))
        if selector == "id":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.ID, elements_locator)))
        if selector == "link text":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.LINK_TEXT, elements_locator)))
        if selector == "partial link text":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, elements_locator)))
        if selector == "name":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.NAME, elements_locator)))
        if selector == "tag name":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, elements_locator)))
        if selector == "class name":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, elements_locator)))
        if selector == "css selector":
            return cls.wait(10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, elements_locator)))

    @classmethod
    def mousehover(cls,locator,selector):
        element=cls.findElement(locator,selector)
        cls.mouse.move_to_element(element).perform()
