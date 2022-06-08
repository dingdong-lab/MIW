import numpy as np
from numpy.linalg import inv
import math

def multiply(a,b):
    m1, n1 = a.shape
    m2, n2 = b.shape

    if n1 != m2:
        return 0

    c = np.zeros((m1,n2))

    for i in range(m1):
        for j in range(n2):
            c[i,j] = np.dot(a[i,:], b[:,j])

    return c

def transpose(a):
    m, n = a.shape
    a = np.array([[x for x in y] for y in a])
    a_t = np.array([a[:,x] for x in range(n)])
    
    return a_t

def triangularize(a):
    a = np.array([[x for x in y] for y in a])
    m, n = a.shape

    for i in range(m):
        a_ii = a[i, i]
        for j in range(i+1, m):
            if a[j, i] == 0:
                continue
            a_ji = a[j, i]/a_ii
            for k in range(i, n):
                a[j, k] = a[j, k] - a[i,k]*a_ji

    return a

def triang_det(a):
    m, n = a.shape
    determinant = -1.0
    if m != n:
        return determinant

    for i in range(m):
        determinant = determinant*a[i,i]

    return -determinant

def gauss_jordan(a):
    m, n = a.shape
    a_temp = a
    a = np.array([[float(a[i,j]) if j < n else 0 for j in range(n*2)] for i in range(m)])
    for i in range(m):
        a[i, m+i] = 1
    n = n*2

    for i in range(m-1):
        a_ii = a[i,i]
        if a_ii == 0:
            depth = 1
            while (i+depth) < m and a[i+depth, i] == 0:
                depth += 1
            if (i+depth) < m:
                a_ij = a[i+depth, i]
                for j in range(i, n):
                    a[i,j] = a[i+depth, j]/a_ij
            else:
                return a_temp
            a_ii = a[i,i]
        elif abs(a_ii) != 1:
            for j in range(i, n):
                a[i, j] = a[i, j]/a_ii
            a_ii = a[i,i]

        depth = 1
        while (i+depth) < m and a[i+depth, i] == 0:
            depth += 1
        if (i+depth) == m:
            continue

        for j in range(i+depth, m):
            if a[j,i] == 0:
                continue
            a_ji = a[j, i]
            for k in range(i, n):
                a[j,k] = a[j,k] - a[i,k]*a_ji/a_ii

    a_ii = a[m-1, m-1]
    for i in range(n):
        a[m-1, i] = a[m-1,i]/a_ii

    for i in range(1, m):
        if a[i, i] == 0:
            return a
        a_ii = a[i, i]
        for j in range(i-1, -1, -1):
            if a[j,i] == 0:
                continue
            a_ji = a[j,i]
            for k in range(i, n):
                a[j,k] = a[j,k] - a[i,k]*a_ji/a_ii

    a = np.array([[a[i,j] for j in range(n//2, n)] for i in range(m)])

    return a

def fast_inverse(a, k):
    m, n = a.shape
    if n != m:
        return -1

    a2 = np.array([[1 if i == j else 0 for j in range(n)] for i in range(m)])
    a_inv = a2
    a2 = a2-a
    a_i = a2+a

    while k > 0:
        a_i = multiply(a_i, a2)
        a_inv = a_inv + a_i
        k -= 1

    return a_inv

# Oblicz całe te całe te B = (X^T*X)^-1*X^T*Y
X = [
    [1,2],
    [1,5],
    [1,7],
    [1,8]
]

Y = [1,2,3,3]

X = np.array(X)
Y = np.reshape(np.array(Y), (4,1))

X_T = transpose(X)
X_T_X = multiply(X_T,X)
X_T_X_1 = gauss_jordan(X_T_X)
X_T_X_1_X_T = multiply(X_T_X_1, X_T)
B = multiply(X_T_X_1_X_T, Y)

'''
print(X)
print(Y)
print(X_T)
print(X_T_X)
print(X_T_X_1)
print(X_T_X_1_X_T)
'''
print(B)

B = np.matmul(np.matmul(inv(np.matmul(X.transpose(), X)), X.transpose()), Y)
print(B)