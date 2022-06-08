from asyncio.windows_events import NULL
from audioop import reverse
from re import M
import numpy as np
import math

def scalar_multiply(v, u):
    l1 = v.shape[0]
    l2 = u.shape[0]

    if l1 != l2:
        return NULL

    value = 0
    for i in range(l1):
        value = value + v[i]*u[i]

    return value

def multiply(a, b):
    m1, n1 = a.shape
    m2, n2 = b.shape

    if n1 != m2:
        return NULL

    c = np.zeros((m1,n2))

    for i in range(m1):
        for j in range(n2):
            c[i,j] = scalar_multiply(a[i, :], b[:, j])

    return c

def transpose(a):
    m, n = a.shape
    a = matrix_copy(a)
    a_t = np.array([a[:,x] for x in range(n)])
    
    return a_t

def vector_len(v):
    return scalar_multiply(v, v)**0.5

def normalize(v, v_len=0):
    m = v.shape[0]

    if v_len == 0:
        v_len = vector_len(v)

    if v_len == 0:
        return np.zeros((m))

    for j in range(m):
        v[j] = v[j]/v_len

    return v

def projection(u, v, u_len_2=0):
    l1 = v.shape[0]
    l2 = u.shape[0]

    if l1 != l2:
        return NULL

    if math.isclose(u_len_2, 0., abs_tol=1e-5):
        u_len_2 = scalar_multiply(u, u)

    if math.isclose(u_len_2, 0., abs_tol=1e-5):
        return np.zeros((l1))

    t = scalar_multiply(u, v)*u
    if not math.isclose(u_len_2, 1., abs_tol=1e-5):
        return t/u_len_2
    return t

def ortonormalize(a):
    m, n = a.shape
    u_columns = []

    for i in range(n):
        v = vector_copy(a[:, i])
        u = vector_copy(v)

        for j in range(i):
            u = u - projection(u_columns[j], v, 1)

        u = normalize(u)
        u_columns.append(u)

    return np.array([ [ u_columns[j][i] for j in range(n) ] for i in range(m) ])

def QR_decompose(a):
    Q = ortonormalize(a)
    Q_T = transpose(Q)
    R = multiply(Q_T, a)

    return (Q, R)

def eigen_qr(a, n):
    for i in range(n):
        Q, R = QR_decompose(a)
        a = multiply(R, Q)

    return a

def vector_copy(v):
    m = v.shape[0]
    return np.array([float(v[i]) for i in range(m)])

def matrix_copy(a):
    m, n = a.shape
    return np.array([[float(a[i,j]) for j in range(n)] for i in range(m)])

def gauss_jordan(a):
    m, n = a.shape
    a_temp = a
    a = matrix_copy(a)

    for i in range(m-1):
        a_ii = a[i, i]
        if math.isclose(a_ii, 0., abs_tol=1e-5):
            depth = 1
            while i+depth < m and math.isclose(a[i+depth, i], 0., abs_tol=1e-5):
                depth += 1
            if (i+depth) < m:
                a_ij = a[i+depth, i]
                for j in range(i, n):
                    a[i, j] = a[i+depth, j]/a_ij
            else:
                return a
            a_ii = a[i,i]
        elif not math.isclose(abs(a_ii), 1.0, abs_tol=1e-5):
            for j in range(i, n):
                a[i, j] = a[i, j]/a_ii
            a_ii = a[i, i]

        depth = 1
        while (i+depth) < m and math.isclose(a[i+depth, i], 0., abs_tol=1e-5):
            depth += 1
        if (i+depth) == m:
            continue

        for j in range(i+depth, m):
            if math.isclose(a[j, i], 0., abs_tol=1e-5):
                continue
            a_ji = a[j, i]/a_ii
            for k in range(i, n):
                a[j, k] = a[j, k] - a[i, k]*a_ji

    a_ii = a[m-1, m-1]
    if not math.isclose(a_ii, 0., abs_tol=1e-5):
        for i in range(n):
            a[m-1, i] = a[m-1,i]/a_ii

    for i in range(1, m):
        if math.isclose(a[i, i], 0., abs_tol=1e-5):
            return a
        a_ii = a[i, i]
        for j in range(i-1, -1, -1):
            if math.isclose(a[j, i], 0., abs_tol=1e-5):
                continue
            a_ji = a[j, i]/a_ii
            for k in range(i, n):
                a[j, k] = a[j, k] - a[i, k]*a_ji

    return a

def rank_triangle(a):
    m, n = a.shape
    i = 0

    for j in range(m):
        if not math.isclose(a[j, j], 0., abs_tol=1e-5):
            i+=1

    return i

def eigen_vectors(a, lambdas):
    m, n = a.shape
    a_temp = a
    vectors = []

    for l in lambdas:
        a = matrix_copy(a_temp)
        for i in range(m):
            a[i,i] = a[i,i] - l

        a = gauss_jordan(a)
        rank = rank_triangle(a)
        a, reduction = triang_to_pair(a, rank)

        vectors.append(normalize(pair_to_vector(a, rank, reduction)))

    return np.array([ [ vectors[j][i] for j in range(len(lambdas)) ] for i in range(m) ])

def triang_to_pair(a, rank):
    a = matrix_copy(a)
    newRank = rank
    reduction = []

    for i in range(rank-1, -1, -1):
            if math.isclose(a[i, i+1], 0., abs_tol=1e-5):
                newRank -= 1
                reduction.append(i)
                for j in range(i-1, -1, -1):
                    a[j, i] = a[j, i+1]
                continue
            r_i = a[i, i]/a[i, i+1]
            for j in range(i-1, -1, -1):
                a[j, i] = a[j, i] - a[j, i+1]*r_i
                a[j, i+1] = 0

    return (a, reduction.copy())

def pair_to_vector(a, rank, reduction):
    a = matrix_copy(a)
    m, n = a.shape
    params = np.zeros((m))

    params[-1] = 1
    for i in range(rank-1, -1, -1):
        if i in reduction:
            params[i] = 0
            continue

        depth = 1
        while params[i+depth] == 0:
            depth += 1
        params[i] = -params[i+depth]*a[i, i+1]/a[i, i]

    return params

def svd_decomposition(a):

    m, n = a.shape
    a_t = transpose(a)

    aa_t = multiply(a, a_t)
    a_ta = multiply(a_t, a)

    if n < m:
        triangle = eigen_qr(a_ta, 10000)
        lambdas = []
        for i in range(n):
            lambdas.append(triangle[i,i])
        
        lambdas.sort(reverse=True)
        v = eigen_vectors(a_ta, lambdas)
        v_t = transpose(v)
        
        u_temp = []
        e = np.zeros((m, n))
        for i in range(n):
            e[i, i] = lambdas[i]**0.5
            u_temp.append(np.array(multiply(a, v[:, i].reshape((n,1)))/e[i, i]))

        u_temp.append(eigen_vectors(aa_t, [0])[:,0].reshape((m,1)))
        u = np.array([ [ u_temp[i][j] for j in range(m) ] for i in range(m) ]).reshape(m,m)
        print(u, e, v_t, sep='\n')
        print(multiply(u,multiply(e,v_t)))
        
    else:
        triangle = eigen_qr(aa_t, 10000)
        lambdas = []
        for i in range(m):
            lambdas.append(triangle[i,i])
        
        lambdas.sort(reverse=True)
        u = eigen_vectors(aa_t, lambdas)
        
        v_temp = []
        u_t = transpose(u)
        e = np.zeros((m, n))
        for i in range(m):
            e[i, i] = lambdas[i]**0.5
            v_temp.append(np.array(multiply(np.array([u_t[:,i]]), a)/e[i, i])[0])

        v_temp.append(eigen_vectors(a_ta, [0])[:,0])
        v_t = np.array([ [ v_temp[i][j] for j in range(n) ] for i in range(n) ])
    
    return (u, e, v_t)

def svd_decomposition_np(a):
    m, n = a.shape
    a = a.copy()
    a_t = np.transpose(a)
    aa_t = np.matmul(a, a_t)
    a_ta = np.matmul(a_t, a)

    if m < n:
        lambdas = np.linalg.eigvals(aa_t)
    else:
        lambdas = np.linalg.eigvals(a_ta)

    lambdas = np.flip(np.sort(lambdas))
    e = np.zeros((m,n))
    for i in range(min(m,n)):
        e[i,i] = lambdas[i]

    u_l, u = np.linalg.eig(aa_t)
    v_l, v = np.linalg.eig(a_ta)
    v_t = np.transpose(v)

    u_id = u_l.argsort()[::-1]
    v_id = v_l.argsort()[::-1]

    u = u[u_id]
    v_t = v_t[v_id]

    return (u, e, v_t)

a = np.array([[2, 1, 4],[-1, 2, -2]], np.float32)
#print(svd_decomposition(a))
#print(svd_decomposition_np(a))

