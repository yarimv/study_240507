import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Main:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://search.naver.com/search.naver?where=news&query="
        self.keyword = input("검색어를 입력하세요: ")
        self.search_url = self.base_url + self.keyword
        self.driver.get(self.search_url)
        time.sleep(2)
        for i in range(3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

    def get_news_data(self):
        news_data = []
        elements = self.driver.find_elements(By.CLASS_NAME, 'news_tit')
        for element in elements:
            title = element.get_attribute("title")
            url = element.get_attribute("href")
            news_data.append({'Title': title, 'URL': url})
        return news_data

    def save_data(self, news_data):
        with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'URL']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in news_data:
                writer.writerow(data)

    def close_driver(self):
        self.driver.quit()

if __name__ == '__main__':
    main = Main()
    news_data = main.get_news_data()
    main.save_data(news_data)
    main.close_driver()
