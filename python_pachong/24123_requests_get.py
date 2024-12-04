import requests
url = 'https://www.baidu.com/s?'
data = {
    'wd': '周杰伦'
}
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
response = requests.get(url=url, params=data, headers=headers)
with open('../html/zhou.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
