def test(a,b,c=2):
    s=(a+b)/c
    return s
x=test(4,2)
y=test(4,2,1)
print(x,y)
