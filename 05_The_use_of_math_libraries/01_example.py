# -*- coding: utf-8 -*-

import numpy as np

# 数据生成
# （列）reshape((-1, 1)): 1:一列，-1，算出来是多少就是多少行。
# （行）np.arange(6):在当前行数子上再加0，1，2，3，4，5（做一个广播）
a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
print(a)

