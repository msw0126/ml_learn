# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def triangle_wave(size, T):
    t = np.linspace(-1, 1, size, endpoint=False)
    # where
    # y = np.where(t < 0, -t, 0)
    # y = np.where(t >= 0, t, y)
    y = np.abs(t)
    y = np.tile(y, T) - 0.5
    x = np.linspace(0, 2*np.pi*T, size*T, endpoint=False)
    return x, y


def sawtooth_wave(size, T):
    t = np.linspace(-1, 1, size)
    y = np.tile(t, T)
    x = np.linspace(0, 2*np.pi*T, size*T, endpoint=False)
    return x, y


def triangle_wave2(size, T):
    x, y = sawtooth_wave(size, T)
    return x, np.abs(y)


def non_zero(f):
    f1 = np.real(f)
    f2 = np.imag(f)
    eps = 1e-4
    return f1[(f1 > eps) | (f1 < -eps)], f2[(f2 > eps) | (f2 < -eps)]


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    # 在控制台输出过程中，默认小数会以科学计数法的形式输出，若不需要，则可以用以下代码
    np.set_printoptions(suppress=True)

    # np.pi是：3.14159265359
    # 创建等差数列。随机16个元素。不包含最大值
    x = np.linspace(0, 2*np.pi, 16, endpoint=False)
    print '时域采样值：', x
    y = np.sin(2*x) + np.sin(3*x + np.pi/4)
    # y = np.sin(x)

    N = len(x)
    print '采样点个数：', N
    print '\n原始信号：', y
    # #快速傅里叶变换
    f = np.fft.fft(y)
    print '\n频域信号：', f/N
    # 计算数组各元素的绝对值
    a = np.abs(f/N)
    print '\n频率强度：', a

    iy = np.fft.ifft(f)
    print '\n逆傅里叶变换恢复信号：', iy
    print '\n虚部：', np.imag(iy)
    print '\n实部：', np.real(iy)
    print '\n恢复信号与原始信号是否相同：', np.allclose(np.real(iy), y)

    # 第一个画板的第一个子图
    plt.subplot(211)
    plt.plot(x, y, 'go-', lw=2)
    plt.title(u'时域信号', fontsize=15)
    plt.grid(True)
    # 第二个画板的第二个子图
    plt.subplot(212)
    w = np.arange(N) * 2*np.pi / N
    print u'频率采样值：', w
    # stem画出来是离散函数，杆图。 plot是连续函数
    plt.stem(w, a, linefmt='r-', markerfmt='ro')
    plt.title(u'频域信号', fontsize=15)
    plt.grid(True)
    plt.show()

    # 三角/锯齿波
    x, y = triangle_wave(20, 5)
    # x, y = sawtooth_wave(20, 5)
    N = len(y)
    f = np.fft.fft(y)
    # print '原始频域信号：', np.real(f), np.imag(f)
    print '原始频域信号：', non_zero(f)
    a = np.abs(f / N)

    # np.real_if_close
    f_real = np.real(f)
    eps = 0.1 * f_real.max()
    print eps
    f_real[(f_real < eps) & (f_real > -eps)] = 0
    f_imag = np.imag(f)
    eps = 0.1 * f_imag.max()
    print eps
    f_imag[(f_imag < eps) & (f_imag > -eps)] = 0
    f1 = f_real + f_imag * 1j
    y1 = np.fft.ifft(f1)
    y1 = np.real(y1)
    # print '恢复频域信号：', np.real(f1), np.imag(f1)
    print '恢复频域信号：', non_zero(f1)

    plt.figure(figsize=(8, 8), facecolor='w')
    # subplot(x y z)%把屏幕分成x*y个窗口取第z个.
    # 这里是分成三个窗口，取第一个
    plt.subplot(311)
    plt.plot(x, y, 'g-', lw=2)
    plt.title(u'三角波', fontsize=15)
    plt.grid(True)
    # 取第二个
    plt.subplot(312)
    w = np.arange(N) * 2*np.pi / N
    plt.stem(w, a, linefmt='r-', markerfmt='ro')
    plt.title(u'频域信号', fontsize=15)
    plt.grid(True)
    # 取第三个
    plt.subplot(313)
    plt.plot(x, y1, 'b-', lw=2, markersize=4)
    plt.title(u'三角波恢复信号', fontsize=15)
    plt.grid(True)
    plt.tight_layout(1.5, rect=[0, 0.04, 1, 0.96])
    plt.suptitle(u'快速傅里叶变换FFT与频域滤波', fontsize=17)
    plt.show()
