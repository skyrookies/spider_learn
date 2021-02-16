def test(a,*b,c):
    total=a+c
    for i in b:
        total=total+i
    h=max(b)
    Max=max(a,h,c)
    k=min(b)
    Min=min(a,h,c)
    print("这几个数的和为：",total)
    print("最大值为:",Max)
    print("最小值为:",Min)
test(1,2,3,4,5,c=8)

