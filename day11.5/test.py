
#就是一个4乘4的面
#上面随机多一个方块 也可多了一个方块再失去一个方块
#当多个方块聚在一起就不会消失了
#m模拟晶体生长 4*4 点阵
#生长基元在上可能消失 也可能被吸附
"""
元胞自动机 Python 实现
修改为模拟单层晶体光滑界面生长
"""
import numpy as np
#调用numpy库 处理矩阵的 as np 用 np简写
import matplotlib.pyplot as plt
#调用该库 用来画图
import numpy.matlib

class GameOfLife(object):

    def __init__(self, cells_shape):
        """
        Parameters
        ----------
        cells_shape : 一个元组，表示画布的大小。

        Examples
        --------
        建立一个高20，宽30的画布
        game = GameOfLife((20, 30))

        """

        # 矩阵的四周不参与运算
        self.cells = np.zeros(cells_shape)

        real_width = cells_shape[0] - 2
        real_height = cells_shape[1] - 2

        self.cells[1:-1, 1:-1] = np.random.randint(1, size=(real_width, real_height))
        #初始状态生成 为方便直接把随机函数[0-2) 改为 [0-1) 初始全为0
        self.timer = 0
        self.mask = np.ones(4)
        self.mask2 = np.ones(9)
        self.mask2[4] = 0

    def update_state(self):
        """更新一次状态"""
        buf = np.zeros(self.cells.shape)
        #按照前一矩阵形状生成全0矩阵 用做更新
        cells = self.cells
        for i in range(1, cells.shape[0] - 1):
            for j in range(1, cells.shape[0] - 1):
                # 计算该细胞周围的存活细胞数
                neighbor_lup = cells[i - 1 : i + 1, j-1:j + 1].reshape((-1,))#左上角
                neighbor_rup = cells[i:i + 2, j-1:j + 1].reshape((-1,))#右上角
                neighbor_ldown = cells[i - 1:i+1 , j :j + 2].reshape((-1,))#左下角
                neighbor_rdown = cells[i : i + 2, j : j + 2].reshape((-1,))#右下角
                # 周围9点值全部转换为一维数组
                neighbor = cells[i - 1:i + 2, j - 1:j + 2].reshape((-1,))
                neighbor_num = np.convolve(self.mask2, neighbor, 'valid')[0]
                neighbor_num_lup = np.convolve(self.mask, neighbor_lup, 'valid')[0]
                neighbor_num_rup = np.convolve(self.mask, neighbor_rup, 'valid')[0]
                neighbor_num_ldown = np.convolve(self.mask, neighbor_ldown, 'valid')[0]
                neighbor_num_rdown = np.convolve(self.mask, neighbor_rdown, 'valid')[0]
                #neighbor数组和mask数组卷积 反正结果就是数组所有值求和
                if (neighbor_num >=4 or neighbor_num_ldown > 3 or neighbor_num_lup>3 or neighbor_num_rup>3 or neighbor_num_rdown>3):
                    #周围9点 即一圈下来包括自己有四个以上就判定可吸附 保持不变
                    buf[i, j] = 1
                else:
                    num_ram = float(numpy.matlib.rand(1)) #用正态分布产生随机数 该数取值满足0-1正态分布
                    if num_ram > 0.1:   #随机数大于0.1时晶体消失 较大概率
                        buf[i, j] = 0
                    else:               #较小概率生成晶体
                        buf[i, j] = 1
        self.cells = buf    #循环完毕状态更新 用更新矩阵重置自身
        self.timer += 1     #计数

    def plot_state(self):
        """画出当前的状态"""
        plt.title('Iter :{}'.format(self.timer))
        plt.imshow(self.cells)
        plt.show()

    def update_and_plot(self, n_iter):
        """更新状态并画图
        Parameters
        ----------
        n_iter : 更新的轮数
        """
        plt.ion()
        for _ in range(n_iter):
            plt.title('Iter :{}'.format(self.timer))
            plt.imshow(self.cells)
            self.update_state()
            plt.pause(0.1) #每轮等待时间
        plt.ioff()

wide=int(input("请输入所需模拟宽度："))
num_of_turn=int(input("请输入模拟轮数："))
if __name__ == '__main__':
    game = GameOfLife(cells_shape=(wide-2, wide-2)) #选范围
    game.update_and_plot(num_of_turn)
    game.plot_state()
    #进行两百轮 可修改定轮数