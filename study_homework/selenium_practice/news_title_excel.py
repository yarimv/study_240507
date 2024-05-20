import time
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import openpyxl
import pandas as pd


class Main:
    def __init__(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
        self.keyword = input("검색어를 입력하세요: ") #대선을 입력 했음
        self.search_url = self.base_url + self.keyword
        self.driver.get(self.search_url)
        time.sleep(2)  # 페이지가 로드되기를 기다립니다.
        self.openpyxl = openpyxl

    def get_news_titles(self):
        titles = []
        elements = self.driver.find_elements(By.CLASS_NAME, 'news_tit')
        # print("elements: " , elements)
        for element in elements:
            titles.append(element.get_attribute("title"))
        return titles


    def get_news_titles(self):
        titles = []
        elements = self.driver.find_elements(By.CLASS_NAME, 'news_tit')
        # print("elements: " , elements)
        for element in elements:
            titles.append(element.get_attribute("title"))
        return titles

    def save_data(self, list):
        list_to_be_saved = list
        # 데이터프레임 생성
        df = pd.DataFrame({'A': list_to_be_saved})

        # 엑셀 파일 생성 pd 이용
        writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
        df.to_excel(writer, index=False)

        # 데이터프레임 내용을 엑셀 파일에 추가
        writer._save()


    def close_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    main = Main()
    title_list = main.get_news_titles()
    print(title_list)
    main.save_data(title_list)
    main.close_driver()


