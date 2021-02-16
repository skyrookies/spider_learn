import cmath
def test(a,b):
    num=a+b
    l=cmath.sqrt(num)
    return l
a=float(input("请输入一个数a:"))
b=float(input("请输入一个数b："))
x=test(a,b)
print(x)