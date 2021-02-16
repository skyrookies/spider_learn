class Study:
    def __init__(self,input_1,input_2):
        self.num11=float(input_1)
        self.num12=float(input_2)
    def multiplus(self):
        return self.num11*self.num12
    @classmethod
    def __f1(cls,number1,number2):
        __n=float(number1)
        __m=float(number2)
        print(__n**__m)
        print(Study.__name__)
    @classmethod
    def f2(cls,number3=None,number4=None):
        if(number4==None or number3==None):
            Study.__f1(0,0)
        else:
            Study.__f1(number3,number4)
    #@staticmethod
    #def f3(self.chice1,self.num12):
     #   print(self.num11,self.num12)
    #print(self.num11)
    '''静态方法无法调用实例变量'''
class Study_2(Study):
    def __init__(self,input_3,input_4):
        Study.__init__(self,input_3,input_4)
    def multipus(self):
        return self.num11**self.num12

a=Study(2,2)
print(a.multiplus())
b1=a.f2(2,4)
b2=a.f2(1)
c=Study_2(3,3)
print(c.multiplus())