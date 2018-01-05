# encoding:utf8
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def func(x, y, x_move=0, y_move=0):
    def mul(X, Y, alis=1):
        return alis * np.exp(-(X * X + Y * Y))

    return mul(x, y) + mul(x - x_move, y - y_move, 2)


def show(x, y):
    fig = plt.figure()
    ax = Axes3D(fig)
    x, y = np.meshgrid(x, y)
    Z = func(x, y, 1.7, 1.7)
    plt.title("demo_hill_climbing")
    ax.plot_surface(x, y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    # ax.scatter(X,Y,Z,c='r') #绘点
    plt.show()


if __name__ == '__main__':
    X = np.arange(-2, 4, 0.1)
    Y = np.arange(-2, 4, 0.1)
    print(np.math.pow(4, 2));
    show(X, Y)
