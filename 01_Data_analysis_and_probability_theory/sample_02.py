# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high
    #  low: 采样下界，float类型，默认值为0；
    #  high: 采样上界，float类型，默认值为1；
    # size: 输出样本数目，为int或元组(tuple)类型
    u = np.random.uniform(0.0, 1.0, 10000)
    # hist： 画柱状图。x轴是u。80：有多少柱状图。facecolor：颜色。alpha：深浅度
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    # 是否有网格
    plt.grid(True)
    plt.show()

    # 一万次之后，平均再求直方图
    times = 10000
    for time in range(times):
        u += np.random.uniform(0.0, 1.0, 10000)
    print(len(u))
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()