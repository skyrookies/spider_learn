class Temperature:
    degree=0
    def ToFahrenheit(self,Cdegree):
        Cdegree=float(Cdegree)
        Fdegree = (Cdegree * 9 / 5) + 32
        return Fdegree
    def ToCelsius(self,Fdegree):
        Fdegree=float(Fdegree)
        Cdegree=(Fdegree - 32) * 5 /9
        return Cdegree

#测试代码
Cdegree=float(input("请输入摄氏温度："))
Trans1=Temperature()
print("摄氏温度为： {0:.1f},华氏温度为：{1:.1f}".format(Cdegree,Trans1.ToFahrenheit(Cdegree)))
Fdegree=float(input("请输入华氏温度："))
Trans2=Temperature()
print("华氏温度为： {0:.1f},摄氏温度为：{1:.1f}".format(Fdegree,Trans2.ToCelsius(Fdegree)))


