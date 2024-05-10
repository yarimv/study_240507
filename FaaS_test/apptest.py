import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import AppiumBy

capabilities = {
    "platformName": "ios",
    "appium:deviceName": "iPhone 13 mini",
    "appium:platformVersion": "15.3",
    "appium:automationName": "xcuitest",
    "appium:udid": "00008110-001A184C0AE3801E",
    "browserName": "Chrome"
    # "appium:bundleId": "kr.co.finda.finda",
    # "appium:xcodeOrgId": "5UGTTL8VT9"
}


appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

driver.get('https://www.finda.co.kr/faas/kjb-default')
time.sleep(3)
#최대 10초간 기다림
wait = WebDriverWait(driver, 30)
time.sleep(10)



element = driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeButton[@name="확인"]')    #AppiumBy.ACCESSIBILITY_ID , accessibility-id
print("텍스트를 포함한 요소가 발견되었습니다!")
time.sleep(5)
print(element)
element.click()
time.sleep(10)

element = driver.find_element(AppiumBy.ID, '신용대출 조건 비교하기')  # AppiumBy.ACCESSIBILITY_ID , accessibility-id
print("텍스트를 포함한 요소가 발견되었습니다!")
time.sleep(2)
print(element)
element.click()
time.sleep(10)

element = driver.find_element(AppiumBy.ID, '이름 이름 입력')
print("텍스트를 포함한 요소가 발견되었습니다!이름 이름 입력")
time.sleep(10)
print(element)
element.click()
element.send_keys("이아림")
print("send_keys 완료!이름 이름 입력")
time.sleep(10)

element = driver.find_element(AppiumBy.ID, '생년월일 6자리')
print("텍스트를 포함한 요소가 발견되었습니다!")
time.sleep(2)
print(element)
element.send_keys("880609")
print("send_keys 완료! 880609")
time.sleep(5)

element = driver.find_element(AppiumBy.ID, '뒷 7자리')
print("텍스트를 포함한 요소가 발견되었습니다!")
time.sleep(2)
print(element)
element.send_keys("2019217")
print("send_keys 완료! 2019217")
time.sleep(5)

element = driver.find_element(AppiumBy.ID, '휴대폰 번호 ‘-’ 없이 숫자만 입력')
print("텍스트를 포함한 요소가 발견되었습니다!")
time.sleep(2)
print(element)
element.send_keys("01093691420")
print("send_keys 완료! 휴대폰 번호")
time.sleep(5)


element = driver.find_element(AppiumBy.ID, '통신사 선택')
print("텍스트를 포함한 요소가 발견되었습니다!통신사 선택")
time.sleep(2)
print(element)
element.click()



element = driver.find_element(AppiumBy.ID, 'KT 알뜰폰')
print("텍스트를 포함한 요소가 발견되었습니다!KT 알뜰폰")
time.sleep(3)
print(element)
element.click()
time.sleep(5)

element = driver.find_element(AppiumBy.ID, '확인')
print("텍스트를 포함한 요소가 발견되었습니다! 확인")
time.sleep(2)
print(element)
element.click()
time.sleep(10)


#약관 바텀싯
element = driver.find_element(AppiumBy.ID, '필수 약관 전체 동의')
print("텍스트를 포함한 요소가 발견되었습니다! 필수 약관 전체 동의")
time.sleep(2)
print(element)
element.click()
time.sleep(10)



element = wait.until(EC.element_to_be_clickable((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "확인"`][2]')))
# element = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "확인"`][2]')
# element = driver.find_element(AppiumBy.ID, '확인')
print("텍스트를 포함한 요소가 발견되었습니다! 약관 동의 바텀싯에서 확인")
time.sleep(10)
print(element)
element.click()
print("텍스트를 포함한 요소가 발견되었습니다! 약관 동의 바텀싯에서 확인 선택함")
time.sleep(20)



#문자입력
element = driver.find_element(AppiumBy.XPATH, "//*[contains(@value,'6자리 입력')]")
print("텍스트를 포함한 요소가 발견되었습니다! 6자리")
time.sleep(2)
print(element)
element.click()
time.sleep(5)




time.sleep(2)
# driver.quit()


# # 참고사항
# # element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[name()='계속하기']")))
# # element = driver.find_element(AppiumBy.ID, "나중에")  #name
# # element = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`label == "신용대출 조건 비교하기"`]')
# # 스크롤다운
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # print("전체동의 후 스크롤 다운?")
# # time.sleep(20)



if __name__ == '__main__':
    pass