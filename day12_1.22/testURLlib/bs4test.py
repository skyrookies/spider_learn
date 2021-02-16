# -*- coding: utf-8 -*-


# @Time    : 2021/1/26 15:33
# @Author  : olknow76
# @FileName: bs4test.py
# @Software: PyCharm
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 修改print函数默认输出编码，方便重定向
'''
描述：BeautifulSoup4将复杂HTHL文档转换成一个复杂的树形结构,每个节点都是Python对象，所有对象可I以归纳为4种:
Tag
NavigableString
BeautifulSoup
comment

'''
from bs4 import BeautifulSoup
file=open("./test.html",'rb')
htmlread=file.read()
afterread=BeautifulSoup(htmlread,"html.parser")


print(afterread.title)
print(type(afterread.title))

#Tag 标签及其内容;窑到宜所找到的第一个内容

print(afterread.title.string)
print(type(afterread.title.string))

print(afterread.a.attrs)
# 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
#2.NavigableString  标签里的内容(字符串〕


#print(htmlread)
print(afterread.name)
print(afterread.attrs)
#3、BeautifulSoup对象表示的是一个文档的内容。大部分时候，可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性


print(afterread.a.string)
print(type(afterread.a.string))
#4、Comment 对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号，即直接输出注释内容


#--------------
#遍历 tag 的 .content 属性可以将tag的子节点以列表的方式输出





#查找
#1)find_all
#2)search()正则表达式匹配
#3)kwargs
#4)text参数