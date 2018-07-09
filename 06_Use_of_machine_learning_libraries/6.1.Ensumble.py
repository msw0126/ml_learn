#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
数值计算：
对于某二分类问题，若构造了10个正确率都是0.6的分类器，采用少数服从多数的原则进行最终分类，则最终分类
正确率时多少？
若构造100个分类器呢？
"""
"""
做集成的时候，往往用的是决策树(弱分类器)
弱分类器：决策树（如果不加剪枝的话，一定会过拟合的）
强分类器：Logistic回归/11_SVM,在训练样本上可以学的很好的一种分类器
随机森林，就是若干个决策树所形成的
"""

import operator

# reduce() 函数会对参数序列中元素进行累积。
def c(n, k):
    x = reduce(operator.mul, range(n-k+1, n+1)) / reduce(operator.mul, range(1, k+1))
    # operator.mul 乘
    # reduce(operator.mul, range(n-k+1, n+1)):对每一个值都做连乘操作
    return reduce(operator.mul, range(n-k+1, n+1)) / reduce(operator.mul, range(1, k+1))


def bagging(n, p):
    s = 0
    for i in range(n / 2 + 1, n + 1):  # 6， 11
        # c(n, i)：从n个里面，做i次的选择
        s += c(n, i) * p ** i * (1 - p) ** (n - i)
    return s


if __name__ == "__main__":
    for t in range(10, 101, 10):
        print t, '次采样正确率：', bagging(t, 0.6)
