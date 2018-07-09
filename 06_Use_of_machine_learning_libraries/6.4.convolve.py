# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # skiprows=2 取消前两行
    # usecols=(2, 3, 4, 5)使用2-5列的数据。从0开始
    # unpack=True 返回四个值，形成一个元祖
    stock_max, stock_min, stock_close, stock_amount = np.loadtxt('6.SH600000.txt', delimiter='\t', skiprows=2, usecols=(2, 3, 4, 5), unpack=True)
    N = 100
    # 取前100个值
    stock_close = stock_close[:N]
    # print stock_close

    n = 5  # 5日均线
    weight = np.ones(n)  # 这里就相当于创建了一个数组，且为5个1/5的数组
    # weight.sum() = 5
    weight /= weight.sum()
    # todo 未理解
    stock_sma = np.convolve(stock_close, weight, mode='valid')  # 简单的移动平均线
    # 等比方差
    weight = np.linspace(1, 0, n)
    # 返回e的n次方，e是一个常数为2.71828
    weight = np.exp(weight)
    weight /= weight.sum()
    # print(weight)
    stock_ema = np.convolve(stock_close, weight, mode='valid')  # exponential moving average（指数移动平均线）

    t = np.arange(n-1, N)
    # 多项式拟合
    poly = np.polyfit(t, stock_ema, 10)
    # print poly
    stock_ema_hat = np.polyval(poly, t)

    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.plot(np.arange(N), stock_close, 'ro-', linewidth=2, label=u'原始收盘价')
    t = np.arange(n-1, N)
    plt.plot(t, stock_sma, 'b-', linewidth=2, label=u'简单移动平均线')
    plt.plot(t, stock_ema, 'g-', linewidth=2, label=u'指数移动平均线')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(9, 6))
    plt.plot(np.arange(N), stock_close, 'r-', linewidth=1, label=u'原始收盘价')
    plt.plot(t, stock_ema, 'g-', linewidth=2, label=u'指数移动平均线')
    plt.plot(t, stock_ema_hat, 'm-', linewidth=3, label=u'指数移动平均线估计')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
