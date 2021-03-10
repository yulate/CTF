import requests
from lxml import etree

url = 'http://114.67.246.176:14957/'
response = requests.session()
res = response.get(url=url).content.decode('utf-8')
ele = etree.HTML(res).xpath('//div/text()')[0][0:-3]
result = eval(ele)
print(result,'\n')

data = {
    'value':result
}

flag = response.post(url=url,data=data).content.decode('utf-8')
print(flag)
