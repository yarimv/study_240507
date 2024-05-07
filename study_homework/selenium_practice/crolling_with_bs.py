from bs4 import BeautifulSoup
import requests

# BeautifulSoup 을 이용한 크롤링

class main:
    # 검색 화면 진입 request 이용
    base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
    keyword = input("검색어를 입력하세요  : ")
    search_url = base_url + keyword

    r= requests.get(search_url)
    print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    print("soup: ", soup)

    # 모든 제목 가져오기
    news_titles = soup.find_all('a', class_='news_tit')

    # 결과를 담을 리스트 초기화
    list_a = []

    # 각 제목을 리스트에 추가
    for title in news_titles:
        list_a.append(title.get_text())

    # 결과 출력
    print(list_a)






    # 각 제목을 엑셀에 저장

    # 이전 연습 코드
    # soup2 = BeautifulSoup(r.content,
    #                      'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
    # print("soup2: ", soup2.prettify())
    #
    # items = soup.select(".api_txt_lines.total_title")
    # print("@@@", items)
    # for e, item in enumerate(items,1):
    #     print(f"{e}, {item.text}", "________________@@@@@@@@@@@@@@@@@@@@@@")
    #

if __name__ =='__main__':
    main()
