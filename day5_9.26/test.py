''' #从系统调入输入求和
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
sum=a+b
print(sum,'of',a,'plus',b)
'''
import cmath
a=3.25
print(type(a))
print(a.as_integer_ratio())
print(a.hex())
b=3.00
print(b.is_integer())
x=3+4j
print(x)
print(type(x))
y=4+3j
print(x*y)
print(x-y)
print(x/y)
d=cmath.sqrt(-4.0)
print(d)
print(type(1/2))
#string 类型
a="iu"
b=1
print(int('20',16),int('101',2))
print(type(1/2))