from selenium.webdriver.common.by import By


class homepage_locators:
    close_login_modal=(By.XPATH,"//span[@class='commonModal__close']")
    MMT_LOGO=(By.XPATH,"//a[@class='mmtLogo makeFlex']")
    LIST_YOUR_PROPERTY=(By.XPATH,"//li[@class='makeFlex hrtlCenter']")
    INTROUDUCING_MYBIZ=(By.ID,"showBizUpgradePopup")