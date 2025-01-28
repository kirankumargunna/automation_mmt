from selenium.webdriver.remote.webdriver import WebDriver

class DriverInitilization:

    _browser=None      # class variable to store the driver

    @classmethod
    def set_driver(cls,driver:WebDriver):
        if not isinstance(driver,WebDriver):
            raise  TypeError("INVALID driver type, it must be an instance of WebDriver")
        cls._browser=driver

    @property
    def browser(self):
        return self._browser

