import numpy as np
import random as rd
import math

def loadData(filename):
    dane = []

    with open(filename, 'r') as data:
        for wiersz in data:
            dane.append(list(map(lambda e : float(e), wiersz.replace('\n', '').split(' '))))
            
    return dane

def euclideanDist2(a, b):
    v = np.array(a)-np.array(b)
    return np.dot(v, v)**0.5

def baricentric(rows):
    centers = {}
    sizes = {}

    for x in rows:
        if x[-1] not in centers:
            centers[x[-1]] = [0 for x in range(len(x)-1)]
            sizes[x[-1]] = 0
        for y in range(len(x)-1):
            centers[x[-1]][y] += x[y]
        sizes[x[-1]] += 1

    for x in centers.keys():
        for y in range(len(centers[x])):
            centers[x][y] = centers[x][y]/sizes[x]

    return centers

def shuffle(rows, colors):
    newrows = [ [ x for x in y] for y in rows ]
    for x in newrows:
        x[-1] = rd.randint(0, colors-1)

    return newrows

def minimalna(slownik):
    values = sorted(slownik.values())
    slownik2 = {k : v for (v, k) in slownik.items()}

    return slownik2[values[0]]

def kolorowanie(rows, colors=2):
    rows = shuffle(rows, colors)

    again = True
    while again:
        again = False
        centers = baricentric(rows)
        for x in rows:
            distances = {k : euclideanDist2(v, x[:-1]) for (k, v) in centers.items()}
            min = minimalna(distances)
            if min != x[-1]:
                again = True
                x[-1] = min

    return rows

def linspace(a, b, n):
    diff = (b-a)/(n-1)
    return [a+diff*x for x in range(n)]

def monte_carlo(function, a, b, pointNum):
    #maxValue = max(map(lambda i : function(i), np.linspace(a, b, pointNum, True)))
    maxValue = max(map(lambda i : function(i), linspace(a, b, pointNum)))
    points = [(rd.uniform(a,b), rd.uniform(0, maxValue)) for x in range(pointNum)]

    lower = upper = 0
    for x in points:
        if x[1] < function(x[0]):
            lower += 1
        else:
            upper += 1

    return maxValue*(b-a)*(lower/(lower+upper))

def riemann(function, a, b, precision):
    #points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
    points = tuple(map(lambda i: function(i), linspace(a, b, precision)))
    diff = (b-a)/(precision-1)

    area = 0
    for x in points[1:]:
        area += diff*x

    return area

def trapmann(function, a, b, precision):
    #points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
    points = tuple(map(lambda i: function(i), linspace(a, b, precision)))
    diff = (b-a)/(precision-1)

    area = 0
    for x in range(1, precision):
        area += diff*(points[x]+points[x-1])/2

    return area


def linear(x):
    return x

filename = 'zaj5/australian.dat'
data = loadData(filename)
result = kolorowanie(data, 2)
#print(trapmann(linear, 0, 1, 50))
#print(riemann(linear, 0, 1, 50))
#print(monte_carlo(linear, 0, 1, 50))

#print(monte_carlo(math.sin, 0, math.pi, 100))
#print(riemann(math.sin, 0, math.pi, 100))
#print(trapmann(math.sin, 0, math.pi, 100))

# Oblicz całkę monte-carlo dla funkcji
# Oblicz całkę riemana dla funkcji