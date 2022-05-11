import numpy as np
import random as rd

def loadData(filename):
    dane = []

    with open(filename, 'r') as data:
        for wiersz in data:
            dane.append(list(map(lambda e : float(e), wiersz.replace('\n', '').split(' '))))
            
    return dane

def euclideanDist(x,y):
    if len(x) != len(y):
        return -1

    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5

def shuffle(a, k):
    b = [[x for x in y] for y in a]
    
    for x in b:
        x[-1] = rd.randint(0, k-1)

    return b

def normalize(a):
    b = [[x for x in y] for y in a]
    m, n = len(b), len(b[0])

    minc = [a[0][x] for x in range(n-1)]
    maxc = [a[0][x] for x in range(n-1)]
    for x in range(n-1):
        for y in range(m):
            minc[x] = min(minc[x], b[y][x])
            maxc[x] = max(maxc[x], b[y][x])

    diffs = [maxc[y]-minc[y] for y in range(n-1)]
    for x in range(m):
        for y in range(n-1):
            b[x][y] = (b[x][y]-minc[y])/diffs[y]

    return b

def groupBy(a):
    dec = {}

    for x in a:
        if x[-1] not in dec:
            dec[x[-1]] = []
        dec[x[-1]].append([y for y in x[:-1]])

    return dec

def baricentric(a):
    centers = {}
    for x in a.keys():
        m = len(a[x])
        minDist = 0
        index = 0
        for y in range(m):
            curDist = 0
            for z in range(m):
                curDist += euclideanDist(a[x][y], a[x][z])/m
            if y == 0:
                minDist = curDist
            elif curDist < minDist:
                minDist = curDist
                index = y
        centers[x] = index

    return centers

def baricentric2(a, n):
    centers = {}
    for x in a.keys():
        m = len(a[x])
        minDist = 0
        index = 0
        for y in range(m):
            curDist = 0
            dists = []
            for z in range(m):
                if y == z:
                    continue
                dists.append(euclideanDist(a[x][y], a[x][z])/n)
            dists = sorted(dists)
            for z in range(n):
                curDist += dists[z]/n
            if y == 0:
                minDist = curDist
            elif curDist < minDist:
                minDist = curDist
                index = y
        centers[x] = index

    return centers

def minimalna(slownik):
    values = sorted(slownik.values())
    slownik2 = {k : v for (v, k) in slownik.items()}

    return slownik2[values[0]]

def kolorowanie(a, k, n):
    b = shuffle(normalize(a), k)

    again = True
    while again:
        again = False
        grouped = groupBy(b)
        if n > 0:
            centers = baricentric2(grouped, n)
        else:
            centers = baricentric(grouped)
        for i in range(len(b)):
            distances = {k : euclideanDist(b[i][:-1], grouped[k][v]) for (k,v) in centers.items()}
            minD = minimalna(distances)
            if minD != b[i][-1]:
                again = True
                b[i][-1] = minD

    return b

def compare(a, b):
    if len(a) != len(b):
        return -1
    m = len(a)

    diffs = 0
    for i in range(m):
        if a[i][-1] != b[i][-1]:
            diffs += 1

    return 1-diffs/m

data = loadData('zaj5/australian.dat')
#data2 = kolorowanie(data, 2, 10)
data2 = kolorowanie(data, 2, 0)
print(compare(data,data2))