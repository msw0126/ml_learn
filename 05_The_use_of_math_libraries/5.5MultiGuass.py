# -*- coding: utf-8 -*-


from __future__ import print_function
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
import scipy.optimize as opt
import scipy
import matplotlib.pyplot as plt
# from scipy.stats import norm, poisson, stats
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import math
import matplotlib as mpl
import scipy.stats

mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = 'SimHei'

if __name__ == '__main__':
    x1, x2 = np.mgrid[-5:5:51j, -5:5:51j]
    x = np.stack((x1, x2), axis=2)

    plt.figure(figsize=(9, 8), facecolor='w')
    sigma = (np.identity(2), np.diag((3,3)), np.diag((2,5)), np.array(((2,1), (2,5))))
    for i in np.arange(4):
        ax = plt.subplot(2, 2, i+1, projection='3d')
        norm = scipy.stats.multivariate_normal((0, 0), sigma[i])
        y = norm.pdf(x)
        ax.plot_surface(x1, x2, y, cmap=cm.Accent,  rstride=1, cstride=1, alpha=0.9, lw=0.5)
        ax.set_xlabel(u'X')
        ax.set_ylabel(u'Y')
        ax.set_zlabel(u'Z')
    plt.suptitle(u'二元高斯分布方差比较', fontsize=18)
    plt.tight_layout(1.5)
    plt.show()