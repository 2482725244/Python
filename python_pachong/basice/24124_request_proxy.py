import requests

url = 'https://www.baidu.com/s?wd=ip'

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

proxy = {
    'https': '59.54.238.29:16918'
}

# data = {
#     'wd': 'ip'
# }

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
with open('../html/ip.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)

