def prime(innum):
    for i in range(2,innum):
        i+=1
        if innum % i == 0:
            return False
        if i == innum-1:
            return True
num=0
print(prime(5))
for j in  range(20,71):
    if prime(j):num+=1;print(j,end=' ')
print(' ')
print(num)