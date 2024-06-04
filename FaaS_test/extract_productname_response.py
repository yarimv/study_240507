import requests
import requests
import urllib3
import json

class ApiValue:


#product 추출하기
    def callApplication(self, applicaitonId, userId):
        # 결과 상품리스트 api 응답 받기

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        applicationId = applicaitonId
        # API 엔드포인트 URL
        url = f'http://stg-eks-backend-internal.findainsight.co.kr/faas-api/v1/application/{applicationId}'

        # 요청 헤더 설정
        headers = {
            "user-id": f"{userId}"
        }

        response = requests.get(url, headers=headers, verify=False)

        # 응답 확인
        if response.status_code == 200:
            # JSON body 값 추출
            self.data = response.json()
            print("응답 데이터:", self.data)
            #text 로 변환
            result = json.dumps(self.data, ensure_ascii=False)
            return result
        else:
            print("오류 발생:", response.status_code)



    def extractProductFromApiResponse(self, response_data):
        self.response_data_text = response_data

        # 결과를 저장할 리스트 생성
        product_names = []

        # response_text에서 productName의 시작 인덱스를 찾음
        index_start = self.response_data_text.find('"productName": "')

        # response_text에서 더 이상 "productName": " 문자열을 찾을 수 없을 때까지 반복
        while index_start != -1:
            # productName 시작 인덱스 이후의 끝 따옴표(")의 인덱스를 찾음
            index_start += len('"productName": "')
            index_end =self.response_data_text.find('"', index_start)

            # productName 값을 추출하여 리스트에 추가
            product_name = self.response_data_text[index_start:index_end]
            product_names.append(product_name)

            # 다음 productName을 찾기 위해 다시 검색 시작 위치를 설정
            index_start = self.response_data_text.find('"productName": "', index_end)

        return product_names
        # 결과 출력
        print("################################################", product_names)








if __name__ == '__main__':
    api_value = ApiValue()
    application_API_Response = api_value.callApplication(643, 1000000000023)
    product_names_in_API_Response = api_value.extractProductFromApiResponse(application_API_Response)
    print("product_names_in_API_Response: ", product_names_in_API_Response)


