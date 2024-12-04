# import requests
# url = 'https://www.gushiwen.cn/user/collect.aspx'
# heads = {
#     'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     # 'accept-encoding':'gzip, deflate, br, zstd',
#     'accept-language':'zh-CN,zh;q=0.9',
#     'cache-control':'max-age=0',
#     #'cookie':'login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1733287079; HMACCOUNT=404364ECD4395E80; ASP.NET_SessionId=n31sjh4keotj4ffmr2l35h1w; wsEmail=2482725244%40qq.com; ticketStr=203636312%7cgQGt8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyS01FQ1I0bGVkN2kxbi1MVGhEMW4AAgT_4k9nAwQAjScA; codeyz=38577cd55636b2db; gsw2017user=6718812%7cBA9E4583654DDD56C901CC417BE97478%7c2000%2f1%2f1%7c2000%2f1%2f1; wxopenid=defoaltid; gswZhanghao=2482725244%40qq.com; gswEmail=2482725244%40qq.com; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1733289135',
#     'priority':'u=0, i',
#     'sec-ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile':'?0',
#     'sec-ch-ua-platform':'"Windows"',
#     'sec-fetch-dest':'document',
#     'sec-fetch-mode':'navigate',
#     'sec-fetch-site':'same-origin',
#     'sec-fetch-user':'?1',
#     'upgrade-insecure-requests':'1',
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
# }
#
# response = requests.get(url=url, headers=heads)
# response.encoding = 'utf-8'
# with open('gu.html','w',encoding='utf-8') as fp:
#     fp.write(response.text)

#古诗文网实战登录

import requests
from lxml import etree
from bs4 import BeautifulSoup

login_url = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'
page_url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'
p_url = 'https://www.gushiwen.cn/RandCode.ashx'

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}

data = {
    '__VIEWSTATE':'',
    '__VIEWSTATEGENERATOR':'',
    'from: http':'//www.gushiwen.cn/user/collect.aspx',
    'email':'2482725244@qq.com',
    'pwd':'Wu123456',
    'code':'',
    'denglu':'登录',
}
session = requests.session()
response = session.get(page_url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
tree = etree.HTML(response.text)

element = soup.select('#__VIEWSTATE')
element2 = soup.select('#__VIEWSTATEGENERATOR')

VIEWSTATE = element[0].get('value')
VIEWSTATEGENERATOR =element2[0].get('value')

data['__VIEWSTATE'] = VIEWSTATE
data['__VIEWSTATEGENERATOR'] = VIEWSTATEGENERATOR

response = session.get(p_url)

with open('../tu/tu.jpg', 'wb') as fp:
    fp.write(response.content)

data['code'] = input('请输入识别的验证码')

# 登录
response = session.post(url=login_url, headers=headers, data=data)
response.encoding = 'utf-8'
with open('../html/login.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)






