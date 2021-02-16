print('请输入您要获得的杨辉三角行数（大于2）：')
a=int(input())
line=[1, 1]
line_string = ''
print(' 1'.center(5*a))
for n in range(0, len(line)):  # 对每行字符转化
    line_string = line_string + ' ' + str(line[n])
print(line_string.center(5*a))  #居中输出

for n in range(0, len(line)):
    line_string = line_string + str(line[n])
for i in range(2, int(a)): #从第三行开始处理
    line_string = ''
    r = []
    for j in range(0, len(line) - 1):
        r.append(line[j] + line[j + 1]) #计算公式 由上一行前两位相加而来
    line = [1] + r + [1]
    for n in range(0,len(line)):    #对每行字符转化
        line_string=line_string+' '+str(line[n])
    print(line_string.center(5*a))  #居中输出