from appium import webdriver
from appium.webdriver import Remote
from appium.options.common import AppiumOptions

class get_appium_driver():
    options_iOS = AppiumOptions().load_capabilities(
        {
            "platformName": "ios",
            "appium:deviceName": "iPhone 13 mini",
            "appium:platformVersion": "15.3",
            "appium:automationName": "xcuitest",
            "appium:udid": "00008110-001A184C0AE3801E",
            "appium:bundleId": "kr.co.finda.finda",
            "appium:xcodeOrgId": "5UGTTL8VT9",
            "appium:xcodeSigningId": "iPhone Developer"
        }
    )
    driver = Remote("http://127.0.0.1:4723", options=options_iOS)






