# -*- coding: utf-8 -*-

from __future__ import print_function

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def calc_statistic(x):
    n = x.shape[0] # 样本数量

    # 手动计算
    m = 0
    m2 = 0
    m3 = 0
    m4 = 0
    for t in x:
        m += t
        m2 += t*t
        m3 += t**4
    m /= n
    m2 /= n
    m3 /= n
    m4 /= n

    mu = m
    sigma = np.sqrt(m2 - mu*mu)
    skew = (m3 - 3*mu*m2 + 2*mu**3) / sigma**3
    kurtosis = (m4 - 4*mu*m3 + 6*mu*mu*m2 - 4*mu**3*mu + mu**4) / sigma**4 - 3
    print('手动计算均值、标准差、偏度、峰度：', mu, sigma, skew, kurtosis)

    # 使用系统函数验证
    mu = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    skew = scipy.stats.skew(x)
    kurtosis = scipy.stats.kurtosis(x)
    return mu, sigma, skew, kurtosis


if __name__ == '__main__':
    d = np.random.randn(100000, 2)
    mu, sigma, skew, kurtosis = calc_statistic(d)
    print('函数库计算均值、标准差、偏度、峰度：', mu, sigma, skew, kurtosis)
    # 二维图像
    # 二元高斯分布
    N = 30
    density, edges = np.histogramdd(d, bins=[N, N])  # 高阶函数
    print('样本总数= ', np.sum(density))
    density /= density.max()
    x = y = np.arange(N)
    # x = y = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]
    """
    t = 
    [array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       ...
       ...
       [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]]), 
    array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    ...
    ...
    [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29,
    29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29]])]
    """
    t = np.meshgrid(x, y)  # 将两个一维数组变为二维矩阵

    fig = plt.figure(facecolor='w')  # 设置figure对象
    ax = fig.add_subplot(111, projection='3d')  # 设置3d
    # 画散点图 文档：https://blog.csdn.net/anneqiqi/article/details/64125186
    ax.scatter(t[0], t[1], density, c='r', s=15*density, marker='o', depthshade=True)
    # 用取样点(x,y,z)去构建曲面
    ax.plot_surface(t[0], t[1], density, cmap=cm.Accent, rstride=2, cstride=2, alpha=0.9, lw=0.75)
    ax.set_xlabel(u'X')
    ax.set_ylabel(u'Y')
    ax.set_zlabel(u'Z')
    plt.title(u'二元高斯分布，样本个数：%d' % d.shape[0], fontsize=20)
    plt.tight_layout(0.1)
    plt.show()