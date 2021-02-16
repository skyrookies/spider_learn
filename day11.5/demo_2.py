import numpy as np
import matplotlib.pyplot as plt

tmp = np.array([[0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]])
tmp = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 0]])


class GameOfLife(object):
    def __init__(self, cells_shape):
        """
        Parameters
        ------
        cells_shape:一个元组，表示画布的大小

        Examples
        ------
        建立一个高20，宽30的画布
        game = GameOfLife((20,30))

        """

        # 矩阵的四周不参与运算
        self.cells = np.zeros(cells_shape)
        # 实际参与运算的矩阵的宽和高
        real_width = cells_shape[0] - 2
        real_height = cells_shape[1] - 2

        # 初始化随机整数矩阵
        # 相当于设置了原始的LUCC情况的栅格图
        self.cells[1:-1, 1:-1] = np.random.randint(2, size=(real_width, real_height))
        #numpy.random.randint(low, high=None, size=None, dtype='l')
        #函数的作用是，返回一个随机整型数，范围从低（包括）到高（不包括），即[low, high)。
        #如果没有写参数high的值，则返回[0,low)的值。
        # 可以自己初始化背景矩阵
        # self.cells=tmp

        # 运算步数
        self.timer = 0
        # 检测窗口的初始化 3*3 中间元胞初始值为0
        # 这里相当于人为设置了检测窗口，每个临近元胞对于中心元胞的影响程度是一致的

        self.mask = np.ones(9)
        #ones()返回一个全1的n维数组，同样也有三个参数：
        # shape（用来指定返回数组的大小）、
        # dtype（数组元素的类型）、
        # order（是否以内存中的C或Fortran连续（行或列）顺序存储多维数据）。
        self.mask[4] = 0

    def update_state(self):
        """
        更新一次状态
        """

        buf = np.zeros(self.cells.shape)
        #用cell的shape 全零初始化buf
        cells = self.cells

        for i in range(1, cells.shape[0] - 1):
            for j in range(1, cells.shape[0] - 1):
                # 检测细胞周围的存活细胞数

                neighbor = cells[i - 1:i + 2, j - 1:j + 2].reshape((-1,))
                #周围9点值全部转换为一维数组
                neighbor_num = np.convolve(self.mask, neighbor, 'valid')[0]

                if neighbor_num == 3:
                    buf[i, j] = 1
                    #周围有三个晶体则保证存活
                elif neighbor_num == 2:
                    buf[i, j] = cells[i, j]
                    #周围两个晶体保持不变
                else:
                    buf[i, j] = 0
                    #周围无晶体概率消失
        self.cells = buf
        #状态更新
        self.timer += 1

    def plot_state(self):

        """
            画出当前的状态
        """

        plt.title('Iter : {}'.format(self.timer))
        plt.imshow(self.cells)
        plt.show()

    def update_and_plot(self, n_iter):
        """
            更新状态并画图
            Parameters
            -------
            n_iter:更新的轮数

        """

        # 切换plt的显示模式 阻塞/交互
        plt.ion()

        for _ in range(n_iter):
            plt.title('Iter :{}'.format(self.timer))
            plt.imshow(self.cells)
            self.update_state()
            plt.pause(0.5)

        plt.ioff()


if __name__ == '__main__':
    game = GameOfLife(cells_shape=(20, 20))
    game.update_and_plot(100)