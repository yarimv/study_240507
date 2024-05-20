from appium import webdriver
from appium.webdriver import Remote
from appium.options.common import AppiumOptions

class get_appium_driver():
    options_android = AppiumOptions().load_capabilities(
        {
            "appium:deviceName": "R5CRB2P3KDM",
            "appium:platformName": "Android",
            "appium:automationName": "uiautomator2"
        }
    )
    driver = Remote("http://127.0.0.1:4723", options=options_android)






