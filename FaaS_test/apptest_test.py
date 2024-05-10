import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import AppiumBy
from PIL import Image
import pytesseract



#환경변수 지정이 필요 할듯 ... 일단 ocr 되는거만 해보기


#
# capabilities = {
#     "platformName": "ios",
#     "appium:deviceName": "iPhone 13 mini",
#     "appium:platformVersion": "15.3",
#     "appium:automationName": "xcuitest",
#     "appium:udid": "00008110-001A184C0AE3801E",
#     "browserName": "Chrome"
#     # "appium:bundleId": "kr.co.finda.finda",
#     # "appium:xcodeOrgId": "5UGTTL8VT9"
# }
#
#
# appium_server_url = 'http://localhost:4723'
#
# driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
#
#
# time.sleep(5)

file_name = "img.png"
# driver.save_screenshot(file_name)

path = "/Users/ahrim/github/automation/FaaS_test/"+ file_name
print("file name :", path )
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

a = Image.open(path)
result = pytesseract.image_to_string(a,lang='kor')
print(result)

#ocr 로 숫자추출



