
import requests
import urllib3


#request 를 이용한 api 응답 받기 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

applicationId = '473'
# API 엔드포인트 URL
url = f'http://stg-eks-backend-internal.findainsight.co.kr/faas-api/v1/application/{applicationId}'


# 요청 헤더 설정
headers = {
"user-id": "1000000000001"
}



response = requests.get(url, headers=headers, verify=False)

# 응답 확인
if response.status_code == 200:
    # JSON body 값 추출
    data = response.json()
    print("응답 데이터:", data)
else:
    print("오류 발생:", response.status_code)
