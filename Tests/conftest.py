import pytest
import toml
from _pytest.nodes import Item

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

    # Read pyproject.toml
    config = toml.load("pyproject.toml")

    browser = item.config.getoption("driver")

    # Get the base_url from the pyproject.toml
    base_url = config.get("tool", {}).get("myapp", {}).get("base_url", "default_url")

    #initilize driver

    Webdrivers().pytest_start_browser(browser=browser)
    driver=Webdrivers._browser
    driver.get(base_url)


# def pytest_runtest_teardown()-> None:
#     """Pytest hook for teardown after each test.
#
#         Checks if the 'driver' variable is present in the local or global namespace.
#         If found, it calls the 'quit()' method on the 'driver' object to close the browser.
#
#         Note: This function assumes that the 'driver' variable is used for browser automation,
#         and its presence is necessary for cleanup.
#
#         Returns:
#             None
#         """
#
#     if "driver" in locals() or "driver" in globals():
#         driver.quit()