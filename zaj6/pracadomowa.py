import numpy as np
import random as rd

def loadData(filename):
    dane = []

    with open(filename, 'r') as data:
        for wiersz in data:
            dane.append(list(map(lambda e : float(e), wiersz.replace('\n', '').split(' '))))
            
    return dane

def mean_matrix(a):
    m = len(a)
    n = len(a[0])
    av = np.array(a)
    v1 = [1 for x in range(m)]

    return [np.dot(v1, av[:,x])/m for x in range(n)]
    
def mean(a):
    n = len(a)
    v = np.array(a)
    v1 = np.array([1 for x in range(n)])

    return np.dot(v1, v)/n

def center_matrix(a, a_mean):
    n = len(a)
    av = np.array(a)
    a_meanv = np.array(a_mean)

    return [x-a_meanv for x in av]

def center(a, a_mean):
    n = len(a)
    av = np.array(a)

    return [x-a_mean for x in av]

def variance_matrix(a_center):
    m = len(a_center)
    n = len(a_center[0])
    a_centerv = np.array(a_center)

    return [np.dot(a_centerv[:,x], a_centerv[:,x])/m for x in range(n)]

def variance(a_center):
    n = len(a_center)
    a_centerv = np.array(a_center)

    return np.dot(a_centerv, a_centerv)/n

def deviation_matrix(a_variance):
    return [x**0.5 for x in a_variance]

def deviation(a_variance):
    return a_variance**0.5

filename = 'zaj6/australian.dat'
data = loadData(filename)

lista1 = [[1,4,7],[2,5,8],[3,6,9]]
a_mean = mean_matrix(lista1)
a_center = center_matrix(lista1, a_mean)
a_variance = variance_matrix(a_center)
a_deviation = deviation_matrix(a_variance)
print(a_mean, a_center, a_variance, a_deviation, sep='\n')
#print(mean(lista1), center(lista1), variance(lista1), deviation(lista1))