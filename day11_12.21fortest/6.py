class student:
    def __init__(self,a,b,c,d,e):
        self.name=str(a)
        self.age=int(b)
        self.num_ch=int(b)
        self.num_math=int(c)
        self.num_en=int(e)
    def getname(self):
        return self.name
    def getmaxscore(self):
        ma1=max(self.num_ch,self.num_en,self.num_math)
        return ma1
a=student('a',10,100,90,80)
b=a.getname()
c=a.getmaxscore()
print(b,c)