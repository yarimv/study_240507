
import requests
import urllib3


#request 를 이용한 api 응답 받기 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# API 엔드포인트 URL
url = "https://service-api.finda.co.kr/ams/v1/loanmanage/loans?cache=false&source=mainHome"

# x-auth 헤더 값
auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzE1NTgyNiwiZXhwIjoxNzQ2MTY2NTQxLCJpYXQiOjE3MTQ2MzA1NDF9.qG9it6v57F2tmq0NJvWDHmBB2KDKw-dGS1dC2mw0iIE"

# 요청 헤더 설정
headers = {
    "x-auth": auth_token
}



response = requests.get(url, headers=headers, verify=False)

# 응답 확인
if response.status_code == 200:
    # JSON body 값 추출
    data = response.json()
    print("응답 데이터:", data)
else:
    print("오류 발생:", response.status_code)
