s=input("请输入字符串:")
count=0
for i in s:
    if(i==' '):
        count+=1
if(count==0):
    print(str.format('单词的个数为:{0}', count))
else:
    print(str.format('单词的个数为:{0}', count + 1))


