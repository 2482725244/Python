import requests
url = 'https://fanyi.baidu.com/sug'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
data = {
    'kw': 'english'
}

response = requests.post(url=url, data=data, headers=headers)

# with open('fan.html','w',encoding='utf-8') as fp:
#     fp.write(response.text)

# import json
# obj = json.load(open('fan.html','r',encoding='utf-8'))
# print(obj)

import json

obj = json.loads(response.text)
print(obj)


