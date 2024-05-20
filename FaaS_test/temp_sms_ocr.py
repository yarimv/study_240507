import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import AppiumBy
from PIL import Image
import pytesseract
import re





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

# 스크린샷에서 문자추출하는 method 로 구현하기



file_name = "img2.png"
# driver.save_screenshot(file_name)
lang = 'kor+eng'
path = "/Users/ahrim/github/automation/FaaS_test/"+ file_name
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
korean_data_path = '/opt/homebrew/bin/tessdata/'
#a = Image.open(path)
result = pytesseract.image_to_string(path, lang=lang, config=f'--tessdata-dir "{korean_data_path}"')
print(result)



#ocr 로 숫자추출

# 결과 문자열을 줄 단위로 분할
lines = result.split('\n')
# '메 시 지 에 서 가 져 옴' 다음 줄에 있는 문자열과 그 다음 줄의 숫자를 추출
for i in range(len(lines)):
    if '메 시 지 에 서 가 져 옴' in lines[i]:
        if i + 1 < len(lines):  # 다음 줄이 있다면
            next_line = lines[i + 1]
            # 다음 줄에 있는 숫자 추출
            numbers = re.findall(r'\d+', next_line)
            if numbers:  # 숫자가 존재한다면
                print(next_line)
                break



