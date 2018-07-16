# /usr/bin/python
# -*- encoding:utf-8 -*-

import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split   # cross_validation


def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]


if __name__ == "__main__":
    path = u'./8.iris.data'  # 数据文件路径
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    x, y = np.split(data, (4,), axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=50)

    data_train = xgb.DMatrix(x_train, label=y_train)
    data_test = xgb.DMatrix(x_test, label=y_test)
    watch_list = [(data_test, 'eval'), (data_train, 'train')]
    """
    参考文档：https://www.cnblogs.com/mfryf/p/6293814.html
    max_depth, 一直分裂到指定的最大深度(max_depth)，然后回过头来剪枝。
    eta, 和GBM中的 learning rate 参数类似。 通过减少每一步的权重，可以提高模型的鲁棒性。 典型值为0.01-0.2。
    silent, 当这个参数值为1时，静默模式开启，不会输出任何信息。 一般这个参数就保持默认的0，因为这样能帮我们更好地理解模型。
    objective, 这个参数定义需要被最小化的损失函数
    num_class, 类别数目
    """
    param = {'max_depth': 3, 'eta': 1, 'silent': 1, 'objective': 'multi:softmax', 'num_class': 3}

    bst = xgb.train(param, data_train, num_boost_round=6, evals=watch_list)
    y_hat = bst.predict(data_test)
    result = y_test.reshape(1, -1) == y_hat
    print '正确率:\t', float(np.sum(result)) / len(y_hat)
    print 'END.....\n'
