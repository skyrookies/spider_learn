# -*- coding: utf-8 -*-


# @Time    : 2021/2/16 0:30
# @Author  : olknow76
# @FileName: testgoogle.py
# @Software: PyCharm
'''
描述：
'''
import sys
import io
import urllib
from bs4 import BeautifulSoup#网页解析
import re   #正则表达式
import urllib.request,urllib.error   #指定统一资源定位器URL
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 修改print函数默认输出编码，方便重定向
def geturl(urlofgoal):
    # dict = {
    #     'hello': 'world'
    # }
    # data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
    # 添加包头
    headersofgoal = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50"

    }
    # method = 'GET'
    # url = 'https://www.baidu.com'
    #标准Request函数构造
    #req = urllib.request.Request(url=urlofgoal,date=dataofgoal,headers=headersofgoal,method=methodofgoal)
    req = urllib.request.Request(url=urlofgoal, headers=headersofgoal)
    #封装包
    html=''
    try:
        response = urllib.request.urlopen(req,timeout=3)
        html=response.read().decode('utf-8')
        #print(html)
        #response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    except:
        print('TIME OUT')
    else:
        print("Request Successfully")

    return html

if __name__=="__main__":
    # 主函数入口
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    # 修改print函数默认输出编码，方便重定向
    url = "https://www.google.com/"
    html=geturl(url)
    print(html)

