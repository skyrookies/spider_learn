# -*- coding: utf-8 -*-


# @Time    : 2021/2/7 20:46
# @Author  : olknow76
# @FileName: test.py
# @Software: PyCharm
'''
描述：
'''
import sys
import io
import sqlite3

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 修改print函数默认输出编码，方便重定向
conn=sqlite3.connect("test.db")
print("成功建立连接")
c=conn.cursor()
sqlin='''
    insert into company(id,name,age,address,salary)
        values(2,"jiang",23,"here",40000)

'''

c.execute(sqlin)
conn.commit()
conn.close()
print("插入成功")
