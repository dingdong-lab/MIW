import numpy as np

def transpose(a):
    m, n = a.shape
    a_t = np.array([a[:,i] for i in range(n)])
    
    return a_t

def multiply(a, b):
    m1, n1 = a.shape
    m2, n2 = b.shape
    c = np.array([[np.dot(a[i], b[:,j]) for j in range(n2)] for i in range(m1)])

    return c

def ortonormalize(a):
    m, n = a.shape
    b = np.array([a[:,i]/(np.dot(a[:,i], a[:,i]))**0.5 for i in range(n)])
        
    return transpose(b)

A_T = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, -1, -1],
    [1, 1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, -1, -1],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, -1]
    ])

X_b = transpose(np.array([[8, 6, 2, 3, 4, 6, 6, 5]])) # B = I
print(X_b)

A = transpose(A_T)
print(np.matmul(A_T, A))
A_N = ortonormalize(A)
A_N_T = transpose(A_N)
X_a = multiply(A_N_T, X_b)
print(X_a)

