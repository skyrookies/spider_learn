sum='1'
sums=1
t=1
for i in range(3,100,2):
    a=(-1)**t
    if(a>0):
        sum+=str.format('+{0}',a*i)
    else:
        sum+=str.format('{0}',a*i)
    t+=1
    sums=sums+(a*i)
print(str.format('{0}={1}',sum,sums))
