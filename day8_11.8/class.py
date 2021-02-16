class Atest:
    def __init__(self,a,b,*c):
        self.__num1=float(a)
        self.__num2=float(b)
        self.__list_1=list(c)
    def sum(self):
        sum=0
        for num_to_sum in self.__list_1:
            sum+=num_to_sum
        sum+=self.__num1+self.__num2
        return sum
    def gai(self,v1,v2):
        self.__num1=v1
        self.__num2=v2
test_1=Atest(input("请输入需要求和的第一个值："),input("请输入需要求和的第二个值："),input("请输入需要求和的后几个值："))
print('求和值为：{0:.2f}'.format(test_1.sum()))
test_1.sum(input('修改第一个数的值为： '),input('修改第二个数的值为： '))
print('修改后的求和值为：{0:.2f}'.format(test_1.sum()))