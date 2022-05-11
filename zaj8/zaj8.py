import numpy as np

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

def projection(u, v, u_len_2=0):
    if u_len_2 == 0:
        u_len_2 = np.dot(u,u)

    return np.dot(u,v)*u/u_len_2

def ortonormalize(a):
    m, n = a.shape
    u_columns = []
    u_lens_2 = []

    for i in range(n):
        v = a[:, i].copy()
        u = v.copy()

        for j in range(i-1,-1,-1):
            u = u - projection(u_columns[j], v, u_lens_2[j])

        u_columns.append(u)
        u_lens_2.append(np.dot(u,u))

    u_lens = [x**0.5 for x in u_lens_2]
    return np.array([ [ u_columns[j][i] / u_lens[j] for j in range(n) ] for i in range(m) ])

def QR_decompose(a):
    Q = ortonormalize(a)
    Q_T = transpose(Q)
    R = multiply(Q_T, a)

    return {'Q' : Q, 'R' : R}

a = np.array([
    [12, -51, 4],
    [6, 167, -68],
    [-4, 24, -41],
])

matrices = QR_decompose(a)
Q, R = matrices.values()
print(a)
print(multiply(Q,R))