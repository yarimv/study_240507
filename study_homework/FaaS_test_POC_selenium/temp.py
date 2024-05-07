from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time


class Main:

    def __init__(self):
        self.url = 'https://www.finda.co.kr/faas/kjb-default'
        self.driver = webdriver.Chrome()
        self.browser = self.driver.get(self.url)

    def step_click_확인(self):
        # element = self.driver.find_elements(By.CLASS_NAME, 'news_tit')

        try:
            # 요소가 나타날 때까지 대기
            # p_tags = driver.find_elements(By.TAG_NAME, 'p')
            # element = WebDriverWait(self.driver, 5).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, "font-18"))
            # )
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, 'p'))
            )

            # 요소 클릭
            print(element)
            time.sleep(3)
            element.click()

            # step 성공여부
            method_name = sys._getframe().f_code.co_name
            print(f"{method_name}: pass")
        except:
            method_name = sys._getframe().f_code.co_name
            print(f"{method_name}: fail")
        # finally:
        #     self.driver.close()
        #     # 웹 드라이버 종료
        #     # self.driver.quit()


if __name__ == '__main__':
    main = Main()
    main.step_click_확인()