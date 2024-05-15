from bs4 import BeautifulSoup


#화면에 노출되는 상품리스트
# example_result.html 파일을 읽어와서 BeautifulSoup 객체로 파싱합니다.
with open("example_result.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

# 클래스가 "font-13 text-fgray-400"인 모든 <p> 태그를 찾습니다.
paragraphs = soup.find_all("p", class_="font-13 text-fgray-400")

# 추출된 <p> 태그의 텍스트 내용을 출력합니다.
a = []
for paragraph in paragraphs:
    print(paragraph.get_text())
    a.append(paragraph.get_text())

print(a)



#api 에서 반환된 상품 리스트

b = ['장기카드대출(카드론)', '하나원큐비상금대출',  '가계신용대출(즉시대출)','JB 위풍당당 대출']

if len(a) != len(b):
    print("두 리스트는 요소의 개수가 다릅니다.")
else:
    # 2. 두 리스트의 요소를 정렬한 후에 요소 단위로 비교
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    if sorted_a == sorted_b:
        print("두 리스트는 순서에 상관없이 같은 요소를 갖습니다.")
    else:
        print("두 리스트는 순서에 상관없이 같은 요소를 갖지 않습니다.")