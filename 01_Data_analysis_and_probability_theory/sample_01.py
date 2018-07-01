# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [float(i)/100.0 for i in range(1, 300)]
    y = [math.log(i) for i in x]
    # 定义x轴，y轴，颜色，线宽
    plt.plot(x, y, 'r-', linewidth=3, label='log Curve')
    a = [x[20], x[175]]
    b = [y[20], y[175]]
    plt.plot(a, b, 'g-', linewidth=2)
    # markersize：标记符的大小. alpha：标记的颜色深浅
    plt.plot(a, b, 'b*', markersize=15, alpha=0.75)
    # legend：显示图例。 loc：设置图例显示的位置。参考文档：https://blog.csdn.net/you_are_my_dream/article/details/53440964
    plt.legend(loc='upper left')
    # 设置网格
    plt.grid(True)
    # 设置x轴的名字
    plt.xlabel('x')
    # 设置y轴的名字
    plt.ylabel('log(x)')
    plt.show()