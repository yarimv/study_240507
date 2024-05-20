import requests



class ProxyValue:

    def findABtestValue(self, test_key):
        # Set the proxy to the address where Proxyman is running
        proxy_address = "http://localhost:9090"  # Change this to the actual Proxyman proxy address

        # Define the URL of the API you want to call
        api_url = "https://stg-service-api.finda.co.kr/account/abtest/user/39ecb18c0b1c7f0f"

        # Set up proxy configuration for requests
        proxies = {
            "http": proxy_address,
            "https": proxy_address,
        }

        # Make the API request through Proxyman with SSL verification disabled
        response = requests.get(api_url, proxies=proxies, verify=False)

        # Check if the response is in JSON format
        if 'application/json' in response.headers.get('Content-Type', ''):
            # Parse the JSON response
            json_response = response.json()

            # # Print the API response as a JSON object
            # print("API Response (JSON):")
            # print(json_response)

            desired_test_key = test_key

            # Find the dictionary corresponding to the desired testKey
            desired_test_dict = next(item for item in json_response['data'] if item['testKey'] == desired_test_key)

            # Get the 'testGroup' value
            test_group_value = desired_test_dict['testGroup']

            # Print the result
            print("test_group_value:", test_group_value)
            return(test_group_value)


        else:
            # Print the raw API response as text
            print("json 형식이 아니어서 모두 보여주기, API Response (Text):")
            print(response.text)

    def extractValue(self):
        # Set the proxy to the address where Proxyman is running
        proxy_address = "http://localhost:9090"  # Change this to the actual Proxyman proxy address

        # Define the URL of the API you want to call
        api_url_to_search = "https://service-api.finda.co.kr/la/v1/application"
        # Set up proxy configuration for requests
        proxies = {
            "http": proxy_address,
            "https": proxy_address,
        }

        # Make the API request through Proxyman with SSL verification disabled
        response = requests.get(api_url_to_search, proxies=proxies, verify=False)

        # Check if the response is in JSON format
        if 'application/json' in response.headers.get('Content-Type', ''):
            # Parse the JSON response
            json_response = response.json()

            # # Print the API response as a JSON object
            # print("API Response (JSON):")
            # print(json_response)

            desired_test_key = "channel"

            # Find the dictionary corresponding to the desired testKey
            desired_test_dict = next(item for item in json_response['applicaton'] if item['applicaton'] == desired_test_key)

            # Get the 'testGroup' value
            test_group_value = desired_test_dict['channel']

            # Print the result
            print("value is: ", test_group_value)
            return (test_group_value)


        else:
            # Print the raw API response as text
            print("json 형식이 아니어서 모두 보여주기, API Response (Text):")
            print(response.text)



if __name__ == '__main__':
    proxy = ProxyValue()
    proxy.findABtestValue('T240203')
