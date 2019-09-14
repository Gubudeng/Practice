import numpy as np
import math
from matplotlib import pyplot as plt
from softmax import SoftmaxRegression
from softmax import Classification
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

theta, loss_record = SoftmaxRegression(dataset=X, labels=y, lamda=0.1, learning_rate=1e-4, max_iter=5000, eps1=1e-6,
                                       eps2=1e-4, EPS=1e-6)
predict = Classification(theta, X)
(predict == y).astype(np.int).mean()  # 训练集上精度
plt.plot(np.arange(len(loss_record)), loss_record)