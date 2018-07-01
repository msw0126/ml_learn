# -*- coding: utf-8 -*-

"""
GMM与图像
"""
from imageop import scale
from random import gauss

from PIL import Image
from statsmodels.sandbox.regression.gmm import GMM


def composite(band, parameter):
    c1 = parameter[0]
    mu1 = parameter[2]
    sigma1 = parameter[3]
    c2 = parameter[1]
    mu2 = parameter[4]
    sigma2 = parameter[5]

    p1 = []
    p2 = []
    for pixel in band:
        p1.append(c1 * gauss(pixel, mu1, sigma1))
        p2.append(c2 * gauss(pixel, mu2, sigma2))

    scale(p1) # 灰度均衡
    scale(p2)
    return [p1, p2]


if __name__ == '__main__':
    im = Image.open('./Pic/test.bmp')
    # print(im.format, im.size, im.mode)

    im = im.split()[0] # 只处理第一个通道
    nb = []
    data = list(im.getdata())
    # todo GMM不知道从那个包导入的
    parameter = GMM(data)
    t =composite(data, parameter)

    im1 = Image.new('L', im.size)
    im1.putdata(t[0])
