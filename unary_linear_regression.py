import numpy as np


def ave(arr: np.ndarray) -> np.longdouble:
    '''
    数据的总平均
    '''
    res = np.longdouble(0.)
    for line in arr:
        for num in line:
            res += num
    res /= arr.size
    return res


def S_T(arr: np.ndarray, X_bar=np.Infinity) -> np.longdouble:
    '''
    总偏差平方和（总变差）
    '''
    res = np.longdouble(0.)
    if X_bar == np.Infinity:
        X_bar = ave(arr)
        pass
    for line in arr:
        for num in line:
            res += (num-X_bar)**2
    return res


def X_bar_j(arr: np.ndarray,  j: int) -> np.longdouble:
    '''
    水平 A_j 下的样本均值
    '''
    res = np.longdouble(0.)
    for num in arr[j]:
        res += num
    res /= arr[j].size
    return res


def S_E(arr: np.ndarray) -> np.longdouble:
    '''
    误差平方和
    '''
    res = np.longdouble(0.)
    for i in range(0, arr.shape[0]):
        X_bar_j_val = X_bar_j(arr, i)
        for num in arr[i]:
            res += (X_bar_j_val-num)**2
    return res


def S_A(arr: np.ndarray, X_bar=np.Infinity) -> np.longdouble:
    '''
    效应平方和
    '''
    res = np.longdouble(0.)
    if X_bar == np.Infinity:
        X_bar = ave(arr)
        pass
    res -= arr.size*(X_bar**2)
    for i in range(0, arr.shape[0]):
        res += arr[i].size*(X_bar_j(arr, i)**2)
    return res
