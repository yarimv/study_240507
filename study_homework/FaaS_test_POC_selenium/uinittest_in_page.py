from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import unittest
from steps import Steps

class 시작바텀싯화면테스트(unittest.TestCase):

#바텀싯화면 내의 모든 버튼 선택
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


    def test_1(self):
        try:
            self.step.시작바텀싯_확인버튼선택()
            self.test_name = sys._getframe().f_code.co_name
            #다음화면의 타이틀이 기대와 같다면 테스트 성공
            element = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.XPATH, "//p[text()='앱 설치 없이 간편하게']"))
            )
            print(element.text)
            self.assertIn('앱 설치 없이 간편하게', element.text)
            print(f"{self.test_name}: pass")
            # self.driver.back()
        except AssertionError as e:
            print(f"{self.test_name}: fail 기대결과 맞지않음")
        except:
            print(f"{self.test_name}: fail 테스트 완료되지 못함")


    def test_2(self):
        try:
            self.step.시작바텀싯_닫기버튼선택()
            self.test_name = sys._getframe().f_code.co_name
            # 다음화면의 타이틀이 기대와 같다면 테스트 성공
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[text()='원하는요소텍스트']"))
            )
            print(element.text)
            self.assertIn('앱 설치 없이 간편하게', element.text)
            print(f"{self.test_name}: pass")
        except AssertionError as e:
            print(f"{self.test_name}: fail 기대결과 맞지않음")
        except:
            print(f"{self.test_name}: fail 테스트 완료되지 못함")



if __name__ == '__main__':
    unittest.main()
