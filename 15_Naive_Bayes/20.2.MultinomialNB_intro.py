#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
在scikit-learn中，一共有3个朴素贝叶斯的分类算法类。分别是GaussianNB，MultinomialNB和BernoulliNB。其中GaussianNB就是先
验为高斯分布的朴素贝叶斯，MultinomialNB就是先验为多项式分布的朴素贝叶斯，而BernoulliNB就是先验为伯努利分布的朴素贝叶斯。

这三个类适用的分类场景各不相同，一般来说，如果样本特征的分布大部分是连续值，使用GaussianNB会比较好。如果如果样本特
征的分大部分是多元离散值，使用MultinomialNB比较合适。而如果样本特征是二元离散值或者很稀疏的多元离散值，应该使用BernoulliNB。
"""

import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB


if __name__ == "__main__":
    np.random.seed(0)
    M = 20
    N = 5
    x = np.random.randint(2, size=(M, N))     # [low, high)
    x = np.array(list(set([tuple(t) for t in x])))
    M = len(x)
    y = np.arange(M)
    print '样本个数：%d，特征数目：%d' % x.shape
    print '样本：\n', x
    mnb = MultinomialNB(alpha=1)    # 动手：换成GaussianNB()试试预测结果？
    mnb.fit(x, y)
    y_hat = mnb.predict(x)
    print '预测类别：', y_hat
    print '准确率：%.2f%%' % (100*np.mean(y_hat == y))
    print '系统得分：', mnb.score(x, y)
    # from sklearn import metrics
    # print metrics.accuracy_score(y, y_hat)
    err = y_hat != y
    for i, e in enumerate(err):
        if e:
            print y[i], '：\t', x[i], '被认为与', x[y_hat[i]], '一个类别'
