# /usr/bin/python
# -*- encoding:utf-8 -*-

import numpy as np
from scipy.sparse import csr_matrix

# row = np.array([0, 0, 1, 2, 2, 2])
# col = np.array([0, 2, 2, 0, 1, 2])
# data = np.array([1, 2, 3, 4, 5, 6])
# a = csr_matrix((data, (row, col))).toarray()
# print(data)
# print("--------------------")
# print(row)
# print("----------------------")
# print(col)
# print("----------------------")
# print(a)


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

path = r"1.csv"
# 数据在https://archive.ics.uci.edu/ml/datasets/Activity+Recognition+from+Single+Chest-Mounted+Accelerometer
df = pd.read_csv(path, header=None)
df.columns = ['index', 'x', 'y', 'z', 'activity']

knn = KNeighborsClassifier()
knn_params = {'n_neighbors': [3, 4, 5, 6]}
X = df[['x', 'y', 'z']]
y = df['activity']

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
X_ploly = poly.fit_transform(X)
X_ploly_df = pd.DataFrame(X_ploly, columns=poly.get_feature_names())
