#결과 리스트에 승인 건들이 모두 노출되는 지 확인
#결과 api response  vs 화면상 노출되는 특정 태그값 비교


#응답에서 "productName" 과 "loanAmount" 만을 추출하여 딕셔너리 만들기

import json

response_text = '''
{
    "applicationId": 1145,
    "faasManagementNo": "f159621",
    "bankCode": "SMART_SAVINGS_BANK",
    "bankName": "스마트저축은행",
    "productName": "애드론 신용대출",
    "productCode": "231",
    "bankLogo": "/v1/product-logo/bank-code-SMART_SAVINGS_BANK/product-code-231",
    "conditionStatus": "APPROVED",
    "conditionStatusName": "승인",
    "loanAmount": 50000000,
    "loanRate": 13.7,
    "loanPeriod": 96,
    "interestType": "FIXED",
    "repayMethod": "LEVEL",
    "earlyRedemptionFeeRate": 0,
    "preferredLoanLimit": null,
    "preferredLoanRate": null,
    "bridgeUrl": null,
    "productTags": [
        {
            "tag": "24시간 내 입금"
        }
    ],
    "productTermsAndConditions": [
        {
            "key": "한도",
            "value": "최소 100만원 ~ 최대 5,000만원"
        },
        {
            "key": "대출대상",
            "value": "소득증빙 가능한 만 19세 이상 직장인, <br>NICE 신용평점 601점 이상인 내부 심사 기준 통과자"
        },
        ...
    ],
    "businessHour": "월 ~ 금 (09:00 ~ 18:00)",
    "customerServiceContactNumber": "1661-3651",
    "requiredOpenAccount": false,
    "earlyRedemptionFeeCharged": true,
    "earlyRedemptionFeeRateMinimum": 0,
    "earlyRedemptionFeeRateMaximum": 1.5
},
{
    "applicationId": 1145,
    "faasManagementNo": "f159630",
    "bankCode": "WOORI_SAVINGS_BANK",
    "bankName": "우리금융저축은행",
    "productName": "사잇돌2",
    "productCode": "8401",
    "bankLogo": "/v1/product-logo/bank-code-WOORI_SAVINGS_BANK/product-code-8401",
    "conditionStatus": "APPROVED",
    "conditionStatusName": "승인",
    "loanAmount": 21000000,
    "loanRate": 12.3,
    "loanPeriod": 60,
    "interestType": null,
    "repayMethod": "ETC1",
    "earlyRedemptionFeeRate": 0,
    "preferredLoanLimit": null,
    "preferredLoanRate": null,
    "bridgeUrl": null,
    "productTags": [
        {
            "tag": "30분 내 입금"
        }
    ],
    "productTermsAndConditions": [
        {
            "key": "한도",
            "value": "최대 3천만원"
        },
        {
            "key": "대출대상",
            "value": "<font color=red>1. 현 직장 재직기간 5개월 이상 경과 자<br>ex) 입사일자 2023.07.05의 경우 대출신청 가능일자 2023.12.05<br>2. 서울보증보험의 보증서 발급이 가능한 고객<br>3. SGI서울보증 내부 심사기준 통과자</font><br>(단, 신용관리대상자 및 채무불이행/연체중인 고객 대출 불가"
        },
        ...
    ],
    "businessHour": "월 ~ 금 (09:00 ~ 18:00)",
    "customerServiceContactNumber": "1599-0038",
    "requiredOpenAccount": false,
    "earlyRedemptionFeeCharged": false,
    "earlyRedemptionFeeRateMinimum": 0,
    "earlyRedemptionFeeRateMaximum": 0
}
'''

# JSON 문자열을 파이썬 객체로 변환
response_data = json.loads(response_text)

# productName과 loanAmount 추출하여 딕셔너리 생성
product_info_dict = {}
for item in response_data:
    product_info_dict[item["productName"]] = item["loanAmount"]

# 결과 출력
print(product_info_dict)
#
# #_______________________________________________________________
# #화면상에서 특정 태그의 값만 추출하기
# import requests
# from bs4 import BeautifulSoup
#
# # URL 설정
# url = "https://www.finda.co.kr/faas/kjb-default/"
#
# # GET 요청 보내고 응답 받기
# response = requests.get(url)
#
# # 응답이 성공적인지 확인
# if response.status_code == 200:
#     # BeautifulSoup 객체 생성
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # 원하는 요소를 찾아서 내용을 출력
#     target_element = soup.find('p', class_='font-13 text-fgray-400')
#     if target_element:
#         extracted_text = target_element.text
#         print("추출된 내용:", extracted_text)
#     else:
#         print("해당 요소를 찾을 수 없습니다.")
# else:
#     print("페이지를 가져오는 데 문제가 발생했습니다. 상태 코드:", response.status_code)
