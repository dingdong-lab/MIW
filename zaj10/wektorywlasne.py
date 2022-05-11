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

    return (Q,R)

def eigen_qr(a, n):
    for i in range(n):
        Q, R = QR_decompose(a)
        a = multiply(R,Q)

    return a

def gauss_jordan(a):
    m, n = a.shape
    a_temp = a
    a = np.array([[float(a[i,j]) for j in range(n)] for i in range(m)])

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

    return a

def eigen_vectors(a, lambdas):
    m, n = a.shape
    a_temp = a
    vectors = {}

    #a = np.array([[float(a[i,j]) for j in range(n)] for i in range(m)])
    for l in lambdas:
        a = np.array([[float(a[i,j]) if j < n else 0 for j in range(n+1)] for i in range(m)])
        for i in range(m):
            a[i,i] = a[i,i] - l

        vectors[l] = gauss_jordan(a)

    return vectors

'''
a = np.array([
    [12, -51, 4],
    [6, 167, -68],
    [-4, 24, -41],
])
'''

a = np.array([[5,3],[-6,-4]])

print(np.linalg.eigvals(a))
U = eigen_qr(a, 10000)
m, n = U.shape
lambdas = [U[i,i] for i in range(m)]
print(lambdas)
print(eigen_vectors(a, lambdas))