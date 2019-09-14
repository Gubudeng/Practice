import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn import datasets


# 计算假设的“相对概率”分布,注意防止指数运算数据溢出  dataset: m*(n+1)    theta: k*(n+1)  m：样本数   n：特征数   k：标签类别数
def Hypothesis(theta, dataset):
    score = np.dot(theta, dataset.T)
    a = np.max(score, axis=0)
    exp_score = np.exp(score - a)
    sum_score = np.sum(exp_score, axis=0)
    relative_probability = exp_score / sum_score
    return relative_probability


# 计算损失函数
# theta为参数矩阵k*(n+1)
def Cost_function(theta, dataset, labels, lamda):
    m, n = dataset.shape
    new_code = One_hot_encode(labels)
    log_probability = np.log(Hypothesis(theta, dataset))
    cost = -1 / m * np.sum(np.multiply(log_probability, new_code)) + lamda * np.sum(theta) / 2
    return cost


# 对标签进行独热编码
# new_code为 k*m  k为标签数 m为样本数
def One_hot_encode(labels):
    m = len(labels)
    k = len(np.unique(labels))
    new_code = np.zeros((k, m))
    for i in range(m):
        new_code[labels[i], i] = 1
    return new_code


# 进行梯度检验
def Gradient_checking(gradient, theta, EPSILON, eps, dataset, labels, lamda):
    theta_vector = theta.ravel()  # 将参数矩阵向量化
    num = len(theta_vector)
    vector = np.zeros(num)
    for i in range(num):
        vector[i] = 1
        theta_plus = theta_vector + EPSILON * vector  # 将已求得参数进行微调求近似梯度
        theta_minus = theta_vector - EPSILON * vector
        approxiamte_gradient = (Cost_function(theta_plus.reshape(theta.shape), dataset, labels, lamda) - \
                                Cost_function(theta_minus.reshape(theta.shape), dataset, labels, lamda)) / (2 * EPSILON)
        vector[i] = 0
        a = abs(approxiamte_gradient - gradient[i])
        if a > eps:
            return False
    if np.linalg.norm(approxiamte_gradient - gradient, ord=2) / (np.linalg.norm(approxiamte_gradient, ord=2)) > eps:
        return False
    return True


# 使用Batch Gradient Descent优化损失函数
# 迭代终止条件：  1：达到最大迭代次数   2：前后两次梯度变化小于一个极小值   3：迭代前后损失函数值变化极小
# dataset为原始数据集：m*n     labels:标签   lamda：正则项系数   learning_rate：学习率   max_iter：最大迭代次数
# eps1：损失函数变化量的阈值  eps2：梯度变化量阈值
def SoftmaxRegression(dataset, labels, lamda, learning_rate, max_iter, eps1, eps2, EPS):
    loss_record = []
    m, n = dataset.shape
    k = len(np.unique(labels))
    new_code = One_hot_encode(labels)
    iter = 0
    new_cost = 0
    cost = 0
    dataset = np.column_stack((dataset, np.ones(m)))
    theta = np.random.random((k, n + 1))
    gradient = np.zeros(n)
    while iter < max_iter:
        new_theta = theta.copy()
        temp = new_code - Hypothesis(new_theta, dataset)
        for j in range(k):
            sum = np.zeros(n + 1)
            for i in range(m):
                a = dataset[i, :]
                sum += a * temp[j, i]
            j_gradient = -1 / m * sum + lamda * new_theta[j, :]  # 计算属于第j类相对概率的梯度向量
            new_theta[j, :] = new_theta[j, :] - learning_rate * j_gradient
        iter += 1
        print("第" + str(iter) + "轮迭代的参数：")
        print(new_theta)
        new_cost = Cost_function(new_theta, dataset, labels, lamda)
        loss_record.append(new_cost)
        print(new_theta)
        print("损失函数变化量：" + str(abs(new_cost - cost)))
        if abs(new_cost - cost) < eps1:
            break
        theta = new_theta
    return theta, loss_record


def SoftmaxRegression2(dataset, labels, lamda, learning_rate, max_iter, eps1, eps2, EPS):
    loss_record = []
    m, n = dataset.shape
    k = len(np.unique(labels))
    new_code = One_hot_encode(labels)
    iter = 0
    new_cost = 0
    cost = 0
    dataset = np.column_stack((dataset, np.ones(m)))
    theta = np.random.random((k, n + 1))
    gradient = np.zeros(n)
    while iter < max_iter:
        new_theta = theta.copy()
        temp = new_code - Hypothesis(new_theta, dataset)
        for j in range(k):
            sum = np.zeros(n + 1)
            for i in range(m):
                a = dataset[i, :]
                sum += a * temp[j, i]
            j_gradient = -1 / m * sum + lamda * new_theta[j, :]  # 计算属于第j类相对概率的梯度向量
            new_theta[j, :] = new_theta[j, :] - learning_rate * j_gradient
        iter += 1
        print("第" + str(iter) + "轮迭代的参数：")
        print(new_theta)
        new_cost = Cost_function(new_theta, dataset, labels, lamda)
        loss_record.append(new_cost)
        print(new_theta)
        print("损失函数变化量：" + str(abs(new_cost - cost)))
        if abs(new_cost - cost) < eps1:
            break
        theta = new_theta
    return theta, loss_record


def Classification(theta, dataset):
    X = dataset.copy()
    X = np.column_stack((X, np.ones(X.shape[0])))
    relative_probability = Hypothesis(theta, X)
    return np.argmax(relative_probability, axis=0)

