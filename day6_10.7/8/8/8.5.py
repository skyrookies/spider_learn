def f(n,l):
    if(n==11):
        return
    else:
        l*=0.5
        L.append(l)
        return f(n+1,l)
L=[100]
f(1,100)
a=sum(L)
print(str.format('共经过{0}米，第十次反弹{1}米',a,L[9]))