'''import sys, random
n = int(sys.argv[1])
for i in range(n):
    print(random.randrange(0,100))

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--length', default=10, type=int, help='长度')
parser.add_argument('--width', default=5, type=int, help='宽度')
args = parser.parse_args()
area = args.length * args.width
print('面积=', area)

import datetime
sName = input("请输入您的姓名：")           #输入姓名
birthyear = int(input("请输入您的出生年份："))  #输入出生年份
age = datetime.date.today().year - birthyear    #根据当前年份和出生年份计算年龄
print("您好！{0}。您{1}岁。".format(sName, age))

import sys
n = int(sys.argv[1])   #命令行第一个参数确认所需求和的整数个数n
sum = 0            #设置求和初始值=0
for i in range(n):
    number = int(input('请输入整数：')) #输入整数
    sum += number                 #整数累加
print('累计和为：', sum)    #输出n个整数累计和

import getpass
username = input("用户名:")        #提示输入用户名
passwd = getpass.getpass("密码:")    #提示输入密码
if username == 'jianghong' and passwd == 'password':    #实际运用中，需要与数据库中的账户信息比较
    print('登录成功')
else:
    print('登录失败')
'''
import sys
filename = sys.argv[0]   #所读取并输出的就是本程序文件type_file.py
f=open(filename, 'r', encoding='utf8')    #打开文件
line_no=0            #统计行号
while True:
    line_no += 1      #行号计数
    line = f.readline()  #读取行信息
    if line:
        print(line_no, ":", line)  #输出行号和该行内容
    else:
        break
f.close()             #关闭打开的文件
