s=[9,7,8,3,2,1,5,6]
count=-1
print(str.format('变换前:{0}',s))
for i in s:
    count+=1
    if(i%2==0):
        del s[count]
        s.insert(count,i*i)
print(str.format('变换后:{0}',s))