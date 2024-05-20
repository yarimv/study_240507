
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from driver_setup_iOS import get_appium_driver
import sys
import time
from proxy_loanlist import ProxyValue
from appium.options.common import AppiumOptions
from appium.webdriver import Remote
from driver_setup_iOS import get_appium_driver
# 자산내용 비교하기
# 농협만 연결했을떄

class asset():

    def __init__(self):
        self.driver_instance = get_appium_driver()


    def 자산노출확인(self):
        proxy_value = ProxyValue()
        불러온자산 = proxy_value.자산호출하기()
        불러온자산.append("없는자산")
        result  = "pass"
        for i in 불러온자산:
            try:
                result = self.driver_instance.driver.find_element(By.ID, i)
                print("result found:", result.text)
            except:
                print("fail 기대결과 맞지않음")
                print("대출이름이 '", i, "'인 대출이 없음")
                result = "fail"
                return result
        return result



if __name__ == '__main__':
    asst = asset()
    asst.자산노출확인()
