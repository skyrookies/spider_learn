def my_sum3(a, b, *c,d):          #各数字累加和
    total = a + b+d
    for n in c:
       total = total + n
    return total
print(my_sum3(1, 2,d=1))            #计算1+2
print(my_sum3(1, 2, 3, 4, 5,d=1))      #计算1+2+3+4+5
print(my_sum3(1, 2, 3, 4, 5, 6, 7,8,8,8,8,8,d=1))  #计算1+2+3+4+5+6+7
