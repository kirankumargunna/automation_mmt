from selenium.webdriver.common.by import By


class homepage_locators:
    LOGIN_MOBILE_NUMBER=(By.XPATH,"//input[@placeholder='Enter Mobile Number']")
    close_login_modal=(By.XPATH,"//span[@class='commonModal__close']")
    MMT_LOGO=(By.XPATH,"//a[@class='mmtLogo makeFlex']")
    LIST_YOUR_PROPERTY=(By.XPATH,"//li[@class='makeFlex hrtlCenter']")
    INTROUDUCING_MYBIZ=(By.ID, "showBizUpgradePopup" )
    TOOLTIP_INTROUDUCING_MYBIZ=(By.XPATH,"//p[@class='latoBlack whiteText appendBottom2']")
    LOGIN_OR_CREATEACCOUNT=(By.XPATH,"//li[@class='makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut']")
    ICONS_NAVIGATION_BAR=(By.XPATH,"//span[@class='headerIconTextAlignment chNavText darkGreyText']")

    FROM_CITY=(By.ID,"fromCity")
    TO_CITY=(By.ID,"toCity")
    INPUT_FIELD=(By.CSS_SELECTOR, '.react-autosuggest__input.react-autosuggest__input--open')
    DEPATURE=(By.ID,"departure")
    SEARCH=(By.XPATH,"//*[contains(@class,'primaryBtn font24 latoBold widgetSearchBtn')]")

    buses_icon=(By.XPATH,"//span[@class='chNavIcon appendBottom2 chSprite chBuses inactive']")
    travel_date_clalander = (By.ID,'travelDate')
