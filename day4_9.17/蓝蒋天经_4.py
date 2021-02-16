for i in range(1,10):
    s=''
    for j in range(1,10):
        s+=str.format("\t{0:1}*{1:1}={2:<2}",i,j,i*j)
    print(s)
print('\n')
for i in range(1,10):
    s=''
    for j in range(1,10):
        if(i<=j):s+=str.format("\t{0:1}*{1:1}={2:<2}",i,j,i*j)
    print(s)
print('\n')
for i in range(1,10):
    s=''
    for j in range(1,10):
        if(i>=j):s+=str.format("\t{0:1}*{1:1}={2:<2}",i,j,i*j)
    print(s)