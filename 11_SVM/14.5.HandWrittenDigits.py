#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn import svm
import matplotlib.colors
import matplotlib.pyplot as plt
from PIL import Image
import os
from sklearn.metrics import accuracy_score


def show_accuracy(a, b, tip):
    acc = a.ravel() == b.ravel()
    print tip + '正确率：%.2f%%' % (100*np.mean(acc))


def save_image(im, i):
    im *= 15.9375
    im = 255 - im
    a = im.astype(np.uint8)
    output_path = '.\\HandWritten'
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    Image.fromarray(a).save(output_path + ('\\%d.png' % i))


if __name__ == "__main__":
    print 'Load Training File Start...'
    data = np.loadtxt('14.optdigits.tra', dtype=np.float, delimiter=',')
    x, y = np.split(data, (-1, ), axis=1)  # 下标-1之前的是x
    images = x.reshape(-1, 8, 8)  # -1是行，由numpy自行计算。三维列表中的元素也是8个元素
    y = y.ravel().astype(np.int)

    print 'Load Test Data Start...'
    data = np.loadtxt('14.optdigits.tes', dtype=np.float, delimiter=',')
    x_test, y_test = np.split(data, (-1, ), axis=1)
    images_test = x_test.reshape(-1, 8, 8)  # 对多少行不管，变成8乘8的矩阵
    y_test = y_test.ravel().astype(np.int)
    print 'Load Data OK...'

    # x, x_test, y, y_test = train_test_split(x, y, random_state=1)
    # images = x.reshape(-1, 8, 8)
    # images_test = x_test.reshape(-1, 8, 8)

    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(15, 9), facecolor='w')
    for index, image in enumerate(images[:16]):
        plt.subplot(4, 8, index + 1)  # 要生成两行两列，这是第一个图plt.subplot('行','列','编号')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')  # 展示图片
        plt.title(u'训练图片: %i' % y[index])
    for index, image in enumerate(images_test[:16]):
        plt.subplot(4, 8, index + 17)
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        save_image(image.copy(), index)
        plt.title(u'测试图片: %i' % y_test[index])
    plt.tight_layout()  # 调整子图之间的距离，防止堆叠
    plt.show()

    clf = svm.SVC(C=1, kernel='rbf', gamma=0.001)   # 这样的参数配置，类似KNN算法
    print 'Start Learning...'
    clf.fit(x, y)
    print 'Learning is OK...'
    y_hat = clf.predict(x)
    show_accuracy(y, y_hat, '训练集')  # 自定义计算函数
    print(accuracy_score(y, y_hat))  # 自带的包函数

    y_hat = clf.predict(x_test)
    print y_hat
    print y_test
    show_accuracy(y_test, y_hat, '测试集')

    err_images = images_test[y_test != y_hat]  # 提取出预测错误的图片
    err_y_hat = y_hat[y_test != y_hat]  # 提取出预测错误的数字
    err_y = y_test[y_test != y_hat]  # 提取出预测错误的数字的真实值
    print err_y_hat
    print err_y
    plt.figure(figsize=(10, 8), facecolor='w')
    for index, image in enumerate(err_images):
        if index >= 12:
            break
        plt.subplot(3, 4, index + 1)
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title(u'错分为：%i，真实值：%i' % (err_y_hat[index], err_y[index]))
    plt.tight_layout()
    plt.show()
