s=list(input('请输入字符串:'))
a=len(s)
i=0
while(i<a):
    t=ord(s[i])
    del s[i]
    s.insert(i,t)
    i+=1
print(s)