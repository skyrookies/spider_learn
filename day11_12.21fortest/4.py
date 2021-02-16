class Ljtj:
    def __init__(self,inputname,inputyear):
        self.age=2020-inputyear
        self.name=inputname
    def who(self):
        print('Ljtj向你报到，我叫{0}, {1}岁'.format(self.name,self.age))


class Ljdy(Ljtj):
    def __init__(self,inname,inyear,innum):
        Ljtj.__init__(self,inname,inyear)
        self.id=innum
    def who(self):
        print('Ljdy向你报到，我叫{0}, {1}岁,我是{2}号'.format(self.name,self.age,self.id))
a=Ljtj('NB',1998)
a.who()
b=Ljdy('SN',1999,23)
b.who()