import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from _wraper.DriverInitilization import DriverInitilization


class Webdrivers(DriverInitilization):

    @classmethod
    def pytest_start_browser(cls, browser):

        if "chrome" in browser:
            options = ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            driver = webdriver.Chrome(options=options)

        elif "edge" in browser:
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("--inprivate")
            options.add_argument("--start-maximized")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Edge(options=options)

        elif "firefox" in browser:
            options = FirefoxOptions()
            options.set_preference("browser.privatebrowsing.autostart", True)
            options.add_argument("--start-maximized")
            options.accept_untrusted_certs = True
            options.assume_untrusted_cert_issuer = True
            driver = webdriver.Firefox(options=options)

        elif "safari" in browser:
            if platform.system() == 'Darwin':
                from selenium.webdriver.safari.options import Options as SafariOptions
                options = SafariOptions()
                options.set_capability("safari:useAutomaticInspection", False)
                options.set_capability("safari:useTechnologyPreview", False)
                options.set_capability("acceptInsecureCerts", True)
                driver = webdriver.Safari(options=options)
            else:
                raise ValueError(f"Invalid OS to run: {browser}")
        else:
            raise ValueError(f"Invalid browser name: {browser}")

        driver.maximize_window()

        # Add any additional setup logic (e.g., window handling, mouse setup)
        cls.mouse = webdriver.ActionChains(driver)
        cls.window_handle = driver.window_handles[0]

        DriverInitilization().set_driver(driver)


