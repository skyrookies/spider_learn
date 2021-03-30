# -*- coding: utf-8 -*-


# @Time    : 2021/2/20 22:42
# @Author  : olknow76
# @FileName: savefile.py
# @Software: PyCharm
'''
描述：本地保存一些有意思的网页内容
'''
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 修改print函数默认输出编码，方便重定向
