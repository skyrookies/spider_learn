#非递归实现:
n=int(input("请输入一个数:"))
s=n
if(n==0 or n==1):
    print(str.format("{0}!={1}",n,1))
else:
    for i in range(1, n):
        s*=i
    print(str.format('{0}!={1}',n,s))



#递归实现:
def f(n):
    if(n==1):
        return n
    elif(n==0):
        return 1
    else:return n*f(n-1)
n=int(input("请输入一个数:"))
print(str.format('{0}!={1}',n,f(n)))