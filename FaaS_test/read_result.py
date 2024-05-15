from bs4 import BeautifulSoup

# example_result.html 파일을 읽어와서 BeautifulSoup 객체로 파싱합니다.
with open("example_result.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

# 클래스가 "font-13 text-fgray-400"인 모든 <p> 태그를 찾습니다.
paragraphs = soup.find_all("p", class_="font-13 text-fgray-400")

# 추출된 <p> 태그의 텍스트 내용을 출력합니다.
for paragraph in paragraphs:
    print(paragraph.get_text())
