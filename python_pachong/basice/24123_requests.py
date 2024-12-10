import requests
url = 'http://www.baidu.com'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
# print(response.text)
# print(response.content)
print(response.status_code)
print(response.url)
print(response.history)
print(type(response))
