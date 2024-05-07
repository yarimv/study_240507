from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time


class Steps:
    def __init__(self):
        self.url = 'https://www.finda.co.kr/faas/kjb-default'
        self.driver = webdriver.Chrome()
        self.browser = self.driver.get(self.url)


    def 시작바텀싯_확인버튼선택(self):
        # element = self.driver.find_elements(By.CLASS_NAME, 'news_tit')
        time.sleep(3)
        try:
            # 요소가 나타날 때까지 대기
            # p_tags = driver.find_elements(By.TAG_NAME, 'p')
            # element = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, "font-18"))
            # )
            # element = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((By.TAG_NAME, 'p'))
            # )
            time.sleep(3)
            # 확인 버튼 선택
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button.confirm'))
            )
            # 이 코드는 클래스 이름이 "confirm"인 <button> 요소를 찾습니다.
            # CSS 선택자로 클래스를 지정할 때는 점(.)을 사용하여 클래스 이름을 지정합니다.
            # element = driver.find_element(By.CSS_SELECTOR, 'button.confirm')
            print(element,"찾은 요소 내 텍스트:", element.text)
            element.click()
            # step 성공여부
            method_name = sys._getframe().f_code.co_name
            print(f"{method_name}: ok")
            return "ok"
        except:
            # step 성공여부
            method_name = sys._getframe().f_code.co_name
            print(f"{method_name}: error")
        # finally:
        #     self.driver.quit()

    def 시작바텀싯_닫기버튼선택(self):
        time.sleep(4)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.close')))
        element.click()
        method_name = sys._getframe().f_code.co_name
        print(f"{method_name}: ok")


#인트로 화면
    def 인트로_조회하기선택(self):
        time.sleep(4)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.confirm')))
        element.click()
        method_name = sys._getframe().f_code.co_name
        print(f"{method_name}: ok")


if __name__ == '__main__':
    step = Steps()
    step.시작바텀싯_확인버튼선택()