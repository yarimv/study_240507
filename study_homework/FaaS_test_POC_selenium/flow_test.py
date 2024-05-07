from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import unittest
from steps import Steps


class 한도조회(unittest.TestCase):
    def setUp(self) -> None:
        self.step = Steps()
        self.driver = self.step.driver



    def tearDown(self) -> None:
        pass
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def test_flow_1(self):
        self.test_name = sys._getframe().f_code.co_name
        self.step.시작바텀싯_확인버튼선택()
        self.step.인트로_조회하기선택()
        time.sleep(5)
        #본인정보 입력
        #이름
        element = input_element = self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='이름 입력']")
        element.send_keys("이아림")
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        time.sleep(5)
        #주민번호 앞 생년월일
        element = input_element = self.driver.find_element(By.XPATH, "//input[@type='text' and @placeholder = '생년월일 6자리']")
        element.send_keys("880609")
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        #주민번호 뒷
        element = input_element = self.driver.find_element(By.XPATH, "//input[@type='password' and @placeholder = '뒷 7자리']")
        element.send_keys("2019217")
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        #휴대전화번호
        element = input_element = self.driver.find_element(By.XPATH, "//input[@type='tel' and @name = 'mobile']")
        element.send_keys("01093691420")
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        #통신사 KT알뜰
        element = input_element = self.driver.find_element(By.XPATH, "//label[@for='faas-loan-verification-mobile-carrier-kt-mvno']")
        element.click()
        time.sleep(2)
        #다음
        element = input_element = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        element.click()
        time.sleep(2)

        #본인인증 약관 바텀싯
        #전체동의
        element = self.driver.find_element(By.XPATH,'//p[contains(text(), "필수 약관 전체 동의")]')
        element.click()
        time.sleep(2)
        #확인
        element = input_element = self.driver.find_element(By.XPATH, "//button[@type='button']")
        element.click()
        time.sleep(2)

        #텍스트 입력(문자 수신).........blocker....
        sms_number = input()







        # try:
        #     self.test_name = sys._getframe().f_code.co_name
        #     self.step.시작바텀싯_확인버튼선택()
        #     self.step.인트로_조회하기선택()
        #     time.sleep(5)
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, 'input.text')))
        #     element.send_keys(Keys.ENTER)
        #
        #
        #     # #다음화면의 타이틀이 기대와 같다면 테스트 성공
        #     # element = WebDriverWait(self.step.driver, 10).until(
        #     #  EC.presence_of_element_located((By.XPATH, "//p[text()='앱 설치 없이 간편하게']"))
        #     # )
        #     # print(element.text)
        #     # self.assertIn('앱 설치 없이 간편하게', element.text)
        #     # print(f"{self.test_name}: pass")
        #     # # self.driver.back()
        # except AssertionError as e:
        #     print(f"{self.test_name}: fail 기대결과 맞지않음")
        # except:
        #     print(f"{self.test_name}: fail 테스트 완료되지 못함")







if __name__ == '__main__':
    unittest.main()