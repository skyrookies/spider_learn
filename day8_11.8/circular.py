import math
class Yuan:
    @staticmethod
    def calculate_len(r):
            r = float(r)
            lenth_of_circular = (2*r*math.pi)
            return lenth_of_circular
    @staticmethod
    def calculate_area(r):
            r = float(r)
            area_of_circular = (r**2*math.pi)
            return area_of_circular
    @staticmethod
    def calculate_area_of_sphere(r):
        r = float(r)
        area_of_sphere=(4*math.pi*r**2)
        return area_of_sphere
    @staticmethod
    def calculate_volume_of_sphere(r):
        r = float(r)
        volume_of_sphere=(math.pi*r**3*4/3)
        return volume_of_sphere
#测试代码
r = float(input("请输入半径："))
len=Yuan.calculate_len(r)
print("圆的周长= {0:.2f}".format(len))
area=Yuan.calculate_area(r)
print("圆的面积= {0:.2f}".format(area))
area_sphere=Yuan.calculate_area_of_sphere(r)
print("球的表面积= {0:.2f}".format(area_sphere))
volume_sphere=Yuan.calculate_volume_of_sphere(r)
print("球的体积= {0:.2f}".format(volume_sphere))

