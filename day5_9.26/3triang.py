import math
print("请输入三角形的直角边a(a>0)长度")
a=float(input())
print("请输入三角形的直角边b(b>0)长度")
b=float(input())
c=math.sqrt(a**2+b**2)
d=a+b+c
sq=a*b/2
print(str.format("三角形的三条边分别为 a={0:1.1f},b={1:1.1f},c={2:1.1f}",a,b,c))
print(str.format("三角形的周长={0:1.1f},面积={1:1.1f}",d,sq))
sinA=math.asin(a/c)
sinB=math.asin(b/c)
print(str.format("三角形的两个锐角度数为{0:1.1f},和{1:1.1f}",round(sinA*180/math.pi,0),round(sinB*180/math.pi,0)))
