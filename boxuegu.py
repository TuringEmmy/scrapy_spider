# life is short, you need use python to create something!
# author    TuringEmmy
# time      18-11-24 下午8:54
# project   scrapy_spider


import requests
cookies_str = '''zg_did=%7B%22did%22%3A%20%22165c7e40dc71-0762ea9a8df652-37664109-100200-165c7e40dca167%22%7D; UM_distinctid=165c7e410eefe-07d49ed0aedf3a-37664109-100200-165c7e410ef358; bad_idb91bf240-868c-11e8-beff-b3a73470030e=51180c21-b5a2-11e8-ba6f-c79f44375129; Hm_lvt_c11880ab74b1d3cd437ca5f41060fd17=1536656936,1536656954; zg_ea5fe1a9d6d94bfdbdd8a54e0ac598c2=%7B%22sid%22%3A%201536656936405%2C%22updated%22%3A%201536656953686%2C%22info%22%3A%201536656936413%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22cn.bing.com%22%7D; SESSION=f3e33925-c02e-40ff-81f4-b66eab0b18d0'''

# cookie_dic ={cookie.split('=')[0]:cookie.split('=')[1]
#              for cookie in cookies_str.split('; ')}
headers = {
    'Cookie': cookies_str
}

# print(cookie_dic)
url='http://ntlias-stu.boxuegu.com/student/queryClassInfo?r_=416140136239755.1'
s = requests.session()
s.cookies = cookies
ret = s.get()
print(ret.content.decode())