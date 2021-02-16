# -*- coding: utf-8 -*-


# @Time    : 2021/2/2 15:44
# @Author  : olknow76
# @FileName: testxlwt.py
# @Software: PyCharm
'''联系使用xlwt 完成数据在excel的保存'''
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 修改print函数默认输出编码，方便重定向

import xlwt
# workbook=xlwt.Workbook(encoding='utf-8')
# worksheet=workbook.add_sheet('sheet1')#创建表单
# for i in range(0,9):
#     for j in range(0,i+1):
#         worksheet.write(i,j,"{0} * {1} = {2}".format(i+1,j+1,(i+1)*(j+1)))
# workbook.save("test.xls")

