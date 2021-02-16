'''def harmonic(n):  #计算n阶调和数（1 + 1/2 + 1/3 + … + 1/n）
    total = 0.0
    for i in range(1, n+1):
        total += 1.0 / i
    return total
x=harmonic(100)
print(x)
def my_max1(a, b):
    if a > b: print(a, '>', b)
    elif a == b: print(a, '=', b)
    else: print(a, '<', b)
my_max1(1, 2)
x = 11; y = 8
my_max1(x, y)
my_max1(1,2)
def my_sum( mid_score, mid_rate = 0.4,*,end_score): #期中成绩、期末成绩、期中成绩权重
    #基于期中成绩、期末成绩和权重计算总评成绩
    score = mid_score * mid_rate + end_score * (1 - mid_rate)
    print(format(score, '.2f'))  #输出总评成绩，保留2位小数
my_sum(mid_score = 88, end_score = 79) #期中88，期末79，期中权重为默认的40%
my_sum(end_score = 79, mid_score = 88) #期末79，期中88，期中权重为默认的40%
my_sum(88, end_score=79)'''            #报错，必须显式使用命名参数传递值
a=1
b=2
def f(a, b):
    x = 'abc'
    y = 'xyz'
    for i in range(2):  #i=0~1
        j = i
        k = i**2
        print(locals())
#测试代码
f(1,2)
print(globals())
