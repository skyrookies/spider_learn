# -*- coding: utf-8 -*-


# @Time    : 2021/1/23 14:35
# @Author  : olknow76
# @FileName: testURL.py
# @Software: PyCharm
'''
描述：urllib学习测试
'''

# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response)
# print(response.read().decode('utf-8'))

#post请求
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))

# import socket
# import urllib.request
# import urllib.error
#
# import urllib.request
# # response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# # print(response.read().decode('utf-8'))
#
# #超时设置
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
#
#
# 响应类型
# import urllib
# import urllib.request
# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.status)
# print(response.getheader("Server"))

import urllib.request
import urllib
#明确目标url
urlofgoal='https://jwxt5.ahu.edu.cn/'
#添加附加数据
dict={
    'hello':'world'
}
dataofgoal=bytes(urllib.parse.urlencode(dict),encoding='utf8')
#添加包头
headersofgoal = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50"

}
#标准Request函数构造
#req = urllib.request.Request(url=urlofgoal,date=dataofgoal,headers=headersofgoal,method='GET')
req = urllib.request.Request(url=urlofgoal,headers=headersofgoal,method='GET')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

