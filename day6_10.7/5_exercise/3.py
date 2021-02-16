l=list(input('请输入一个列表:'))
l1=list()
for i in l:
    if(i not in l1):
        l1.append(i)
print(str.format('删除重复元素后的列表为:'))
print(l1)