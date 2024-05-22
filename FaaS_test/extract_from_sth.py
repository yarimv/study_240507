from bs4 import BeautifulSoup
from extract_productname_response import ApiValue
from extract_productname_response import ApiValue
import re
# 상품 리스트 response 를 파일로 수기 저장한 것을 열기
with open("data.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# #미리 만들어둔 메서드로 하나의 값만 추출
# extract = ApiValue()
#
# result = extract.extractProductFromApiResponse(html_content)
#
# print(result)



# 정규 표현식을 사용하여 productName과 productCode를 추출
product_name_pattern = re.compile(r'"productName":\s*"([^"]+)"')
product_code_pattern = re.compile(r'"productCode":\s*"([^"]+)"')

product_names = product_name_pattern.findall(html_content)
product_codes = product_code_pattern.findall(html_content)

# 결과 출력
for name, code in zip(product_names, product_codes):
    print(f"Product Name: {name}, Product Code: {code}")