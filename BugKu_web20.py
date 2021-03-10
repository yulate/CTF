import requests
import base64

url = 'http://114.67.246.176:10713/'
response = requests.session()
result = response.get(url=url)
print(result.headers)
headers = result.headers

str_flag = base64.b64decode(headers['flag']).decode("utf-8")
print(str_flag)

min_flag = base64.b64decode(str_flag.split(':')[1])

data = {
    'margin': min_flag
}
print(response.post(url,data).text)
