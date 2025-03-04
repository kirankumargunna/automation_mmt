import pytest
import toml
from _pytest.nodes import Item
from pygments.lexer import default

from _wraper.DriverInitilization import DriverInitilization


from Drivers.webdrivers import Webdrivers

drivers = ("chrome", "firefox", "chrome_headless", "remote")

def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        choices=drivers,
        default="chrome",
        help="specify the driver to run the test"
    )
    



def pytest_runtest_setup(item:Item) -> None:
    """
    python hook for setup brfore each test
    it will automatically execution of each test
    :return: none
    """
    global browser,driver

    # # If driver is already initialized, skip initializing it again
    # if DriverInitilization._browser is not None:
    #     return
    
    # Read pyproject.toml
    config = toml.load("pyproject.toml")

    # Get browser type from CLI options
    browser = item.config.getoption("driver")

    # Get the base_url from the pyproject.toml
    base_url = config.get("tool", {}).get("myapp", {}).get("base_url", "default_url")

    #initilize a seperate webdriver inistance for each test
    webdriver_instance=Webdrivers()

    webdriver_instance.pytest_start_browser(browser=browser)  # start browser

    # Store the WebDriver instance in test class instance to avoid conflicts
    web_driver=webdriver_instance._browser
    item.cls.driver = web_driver
    item.cls.driver.get(base_url)


def pytest_runtest_teardown(item:Item)-> None:
    """Pytest hook for teardown after each test.

        Checks if the 'driver' variable is present in the local or global namespace.
        If found, it calls the 'quit()' method on the 'driver' object to close the browser.

        Note: This function assumes that the 'driver' variable is used for browser automation,
        and its presence is necessary for cleanup.

        Returns:
            None
        """

    if hasattr(item.cls, "driver"):  # Check if WebDriver exists
            item.cls.driver.quit()  # Close the browser
            item.cls.driver = None 