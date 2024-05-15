import requests


class ProxyValue:


#product 추출하기
    def 결과리스트호출하기(self):
        # Set the proxy to the address where Proxyman is running
        proxy_address = "http://localhost:9090"  # Change this to the actual Proxyman proxy address

        # Define the URL of the API you want to call
        api_url = "https://www.finda.co.kr/faas/kjb-default/api/result/list"

        # Set up proxy configuration for requests
        proxies = {
            "http": proxy_address,
            "https": proxy_address
        }

        # Set up headers with X-Auth-Token
        headers = {
            # "X-Auth-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzE1NTgyNiwiZXhwIjoxNzQ2MjQxMTI1LCJpYXQiOjE3MTQ3MDUxMjV9.B6rmQa81AJWMjiclPEO2JRpepjGCFKNCRVgwupLZVU8",  # Replace "your_auth_token_here" with your actual token
            "Content-Type": "application/json"
        }

        body = {
             "applicationData": {
            "applicationId": 1149,
            "userId": 1000000000008,
            "isScrape": False
             }
            }
        # Make the API request through Proxyman with SSL verification disabled
        response = requests.post(api_url, proxies=proxies, headers=headers, json = body, verify=False)

        my_loan =[]
        # Check if the response is in JSON format
        if 'application/json' in response.headers.get('Content-Type', ''):
            # Parse the JSON response
            json_response = response.json()

            # Print the API response as a JSON object
            print("API Response (JSON):")
            print(json_response)
            print("json_response['list']:", json_response['list'])

            # desired_test_dict = next(item for item in json_response['list'] )
            # Iterate through each item in the list and print its productName
            for item in json_response['list']:
                my_loan.append(item.get('productName'))
                print("productName:", item.get('productName'))

            print("result: ",  my_loan)
            return my_loan
        else:
            # Print the raw API response as text
            print("json 형식이 아니어서 모두 보여주기, API Response (Text):")
            print(response.text)
            return my_loan







if __name__ == '__main__':
    proxy = ProxyValue()
    proxy.결과리스트호출하기()
