import random
n=random.randint(0,10)
sn=0
tn=0
for i in range(1,n+1):
    tn+=10**(i-1)
    sn += tn
print('Tn=',tn)
print(str.format('n={0},\tSn={1}',n,sn))