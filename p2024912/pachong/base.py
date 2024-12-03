# import urllib.request
# # url_html = 'http://www.baidu.com'
# # url_img = 'https://img2.baidu.com/it/u=3515990136,2889089570&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=948'
# # url_video = 'https://vfiles.gtimg.cn/tvideo/libcocos-frame/0.1.81/index.html?isEngineTune=0&report_recomm_player=ptag%3Dv_qq_com%7Crtype%3D%7CalgId%3D%7CbucketId%3D%7Creason%3D%7CreasonType%3D%7Ccid%3D%7Cvid%3D%7Cpid%3D%7Cmodule%3D%E5%8D%B3%E5%B0%86%E4%B8%8A%E6%98%A0%7CpageType%3DfilmIndex%7Cseqnum%3D&aid=97fe9534-3898-4677-9cf1-c14fa13a3370&uin=be08bb4c13f5e1c0&ext1=&ext2=version%3D1.0.2.56074%26vuid%3D%26env%3Dweb_formal%26url%3Dhttps%253A%252F%252Fv.qq.com%252Fx%252Fcover%252Fmzc00200zfbgy6f.html%253Freport_recomm_player%253Dptag%25253Dv_qq_com%25257Crtype%25253D%25257CalgId%25253D%25257CbucketId%25253D%25257Creason%25253D%25257CreasonType%25253D%25257Ccid%25253D%25257Cvid%25253D%25257Cpid%25253D%25257Cmodule%25253D%2525E5%25258D%2525B3%2525E5%2525B0%252586%2525E4%2525B8%25258A%2525E6%252598%2525A0%25257CpageType%25253DfilmIndex%25257Cseqnum%25253D&ext3=100000%23100000%23100000%23100000%23100000%23100000'
# #
# # # response = urllib.request.urlopen(url_html)
# # # print(response.read().decode('utf-8'))
# #
# # # urllib.request.urlretrieve(url_html,'baidu.html')
# # # urllib.request.urlretrieve(url_img,'古月方源.jpg')
# # urllib.request.urlretrieve(url_video,'tun.mp4')
# # print("Download complete!")
# import urllib.request
# url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url)
# print(response.read(5))
# print(response.readlines())
# print(response.getcode())
# print(response.geturl())
# print(response.getheaders())
# import urllib.request
# import urllib.parse
# url = 'https://www.baidu.com/s?ie=utf-8&'
#
# # name = '方源'
# # name = urllib.parse.quote(name)
# data = {
#     'wd': '方源',
#     'sex': '男'
# }
# code = urllib.parse.urlencode(data)
#
# headers = {
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
# }
# request = urllib.request.Request(url=url+code,headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
# import urllib.request
# import urllib.parse
#
# headers = {
#  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
#  }
#
# url = 'https://fanyi.baidu.com/sug'
# data = {
#     'kw': 'spider'
# }
#
# data = urllib.parse.urlencode(data).encode('utf-8')
#
# request = urllib.request.Request(url=url,data=data,headers=headers)
# print(request)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# # print(content)
#
# import json
# obj = json.loads(content)
# print(obj)

#豆瓣网
# import urllib.request
# import urllib.parse
# base_url = ('https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&')
# data = {
#     'start':0,
#     'limit':20
# }
# data = urllib.parse.urlencode(data)
# url = base_url+data
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
# }
#
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# with open('video_info.json','w',encoding='utf-8') as file:
#     file.write(content)
# print('Dwonload over!')

# 循环获取
# import urllib.request
# import urllib.parse
#
# def create_request(index):
#     base_url = f'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={index}&limit=20'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
#     }
#     return urllib.request.Request(url=base_url,headers=headers)
#
# def create_response(request):
#     return urllib.request.urlopen(request).read().decode('utf-8')
#
# for index in range( 0, 10 + 1):
#     request = create_request(index * 20)
#     content = create_response(request)
#     with open(f'豆瓣{index + 1}.json','w',encoding='utf-8') as file:
#         file.write(content)
#     print("Dwonload success!")

#肯德基门店
# import urllib.request
# import urllib.parse
#
#
#
# # post
# def create_request(index):
#     base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
#     }
#     data = {
#         'cname': '北京',
#         'pid': '',
#         'pageIndex': index,
#         'pageSize': '10'
#     }
#
#     data = urllib.parse.urlencode(data).encode('utf-8')
#     request = urllib.request.Request(url=base_url, data=data, headers=headers)
#     return request
#
# def create_response(request):
#     return urllib.request.urlopen(request)
#
# for index in range(1,10 + 1):
#     request = create_request(index)
#     response = create_response(request)
#     content = response.read().decode('utf-8')
#     try:
#         with open('肯德基门店.json','a',encoding='utf-8') as file:
#             file.write(content)
#     except :
#         with open('肯德基门店.json','w',encoding='utf-8') as file:
#             file.write(content)
#     finally:
#         file.close()
#         print("Dwonload success!")

# Cookie登录

# import urllib.request
# import urllib.parse
#
# url = 'https://i.mooc.chaoxing.com/space/index?t=1733040146269'
# headers = {
#     #'cookie':'lv=1; fid=893; _uid=192596498; uf=5d3a3b6893c99a74c5cca0e422da616f2feaf5a271f5fc05f3a43025190075620ed8898c950966795e9a23f09c44bf25c49d67c0c30ca5047c5a963e85f11099895ef0f4bdeed71dfd68be96b6183b1af4751d19f3fc537a49971ae2e1c81bf4e8c13e76fb3ecbb3; _d=1732622113167; UID=192596498; vc=92E15FA9FD305F2E6421AE2BBF09D4AD; vc2=B0CCFD032E1F1AB6343902FA80D912B8; vc3=a8Z01Ao5vSAW7GjUbU%2BmlAhztHAolh32iwL4yidB25r37PahAi9uCjCNUZUNgAFnM4OiYX%2Fq7yC6UU29w%2F5dzQenKI9sdUjDxTg5%2F%2BH96nho6t0H6QpOFKi7NN9SZ4Zp2VK1P2g5I%2F3uqeYJm9u5xC8nFUoGUDrSY0qU5dn5iLw%3D442b4af93cd649e51d98709190db6d9a; cx_p_token=1f38dbe6b83f0bb94cfcb3f15eed8b34; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxOTI1OTY0OTgiLCJsb2dpblRpbWUiOjE3MzI2MjIxMTMxNjksImV4cCI6MTczMzIyNjkxM30.2srGB2_63EAM8Y-I0k3wGQq6sF0yIOYQ7tie5UNKHz0; xxtenc=21e5a9c66436127d300f9249fe5f22f6; DSSTASH_LOG=C_38-UN_7789-US_192596498-T_1732622113169; fanyamoocs=657DB963900D47883606855810916A7B; _dd192596498=1733040146224; source=""; thirdRegist=0; k8s=1733040150.542.12235.241752; jrose=980EC3A55C97191A3DAD3205397002A6.mooc2-967984215-k93mk; tl=1; route=f9c314690d8e5d436efa7770254d0199',
#     'cookie':'lv=1; fid=893; _uid=192596498; uf=5d3a3b6893c99a74c5cca0e422da616f2feaf5a271f5fc05f3a43025190075620ed8898c950966795e9a23f09c44bf25c49d67c0c30ca5047c5a963e85f11099895ef0f4bdeed71dfd68be96b6183b1af4751d19f3fc537a49971ae2e1c81bf4e8c13e76fb3ecbb3; _d=1732622113167; UID=192596498; vc=92E15FA9FD305F2E6421AE2BBF09D4AD; vc2=B0CCFD032E1F1AB6343902FA80D912B8; vc3=a8Z01Ao5vSAW7GjUbU%2BmlAhztHAolh32iwL4yidB25r37PahAi9uCjCNUZUNgAFnM4OiYX%2Fq7yC6UU29w%2F5dzQenKI9sdUjDxTg5%2F%2BH96nho6t0H6QpOFKi7NN9SZ4Zp2VK1P2g5I%2F3uqeYJm9u5xC8nFUoGUDrSY0qU5dn5iLw%3D442b4af93cd649e51d98709190db6d9a; cx_p_token=1f38dbe6b83f0bb94cfcb3f15eed8b34; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIxOTI1OTY0OTgiLCJsb2dpblRpbWUiOjE3MzI2MjIxMTMxNjksImV4cCI6MTczMzIyNjkxM30.2srGB2_63EAM8Y-I0k3wGQq6sF0yIOYQ7tie5UNKHz0; xxtenc=21e5a9c66436127d300f9249fe5f22f6; DSSTASH_LOG=C_38-UN_7789-US_192596498-T_1732622113169; fanyamoocs=657DB963900D47883606855810916A7B; _dd192596498=1733040146224; jrose=D7B39F123E316161FCF0A77B5DC09A8C.ans; source=""; spaceFidEnc=8DE738136E1ED9B16DCAA882CC9A2A80; thirdRegist=0; tl=1',
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
#     'referer':'https://mooc1-2.chaoxing.com/visit/courses/study?s=862eff72a3932414d87541552d7eb4e9'
# }
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# with open('xuexitong.html','w',encoding='utf-8') as file:
#     file.write(content)

#代理ip
# import urllib.request
# import urllib.parse
#
# url = 'https://www.ipplus360.com/'
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
# }
#
# request = urllib.request.Request(url=url,headers=headers)
#
# # handler = urllib.request.HTTPHandler()
# # opener = urllib.request.build_opener(handler)
# # response = opener.open(request)
#
# # response = urllib.request.urlopen(request)
#
# proxy_ip = {
#     'https':'202.101.213.28:23541'
# }
#
# handler = urllib.request.ProxyHandler(proxy_ip)
# opener = urllib.request.build_opener(handler)
# response = opener.open(request)
#
# content = response.read().decode('utf-8')
# with open('ip.html','w',encoding='utf-8') as fp:
#     fp.write(content)
# print('Dwonload success!')

# XPath
print("aaa")
























