s=[9,7,8,3,2,1,5,6]
a=len(s)
b=max(s)
c=min(s)
sum=0
for i in s:
    sum+=i
d=sum/a
print(str.format('元素个数:{0},最大值:{1},最小值:{2},元素之和:{3},平均值:{4:.2f}',a,b,c,sum,d))