for i in range(1,11):print(i,end=' ')
print("\n")
for i in range(1,11,3):print(i,end=' ')
for i in (1,2,3):
    print(i,i**2,i**3)
sum_odd=0;sum_enen=0
for i in range(1,101):
    if i%2 !=0:
        sum_odd+=i
    else:
        sum_enen+=i
print("奇数合",sum_odd)
print("偶数合",sum_enen)
for i in(1,1,1):
    print(i)

#enumerate函数
seasons=['春','夏','秋','冬']
for i,s in enumerate(seasons,start=1):
    print("the {0}rd season:{1}".format(i,s))
#循环嵌套
for i in range(1,10):
    s=''
    for j in range(1,10):
        s+=str.format("\t{0:1}*{1:1}={2:<2}",i,j,i*j)
    print(s)
#zip函数
evens=[0,2,4,6,8]
odds=[1,3,5,7,9]
for e,o in zip(evens,odds):
    print("{0}*{1}={2}".format(e,o,e*o))
#map函数
for i in range(-3,21,4):
    print(i,end=' ')
q=-1
while(q<0):q*=q
print(q)