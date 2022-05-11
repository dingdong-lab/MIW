def loadData(filename):
    dane = []

    with open(filename, 'r') as data:
        for wiersz in data:
            dane.append(list(map(lambda e : float(e), wiersz.replace('\n', '').split(' '))))
            
    return dane

def euclideanDist(a, b):
    al = len(a)
    
    if al != len(b):
        return -1
    
    wynik = 0
    for x in range(al):
        wynik = wynik + (a[x]-b[x])**2
        
    wynik = wynik**0.5
    
    return wynik

def klasaDec(x, lista):
    
    lista2 = []
    for row in lista:
        lista2.append((row[-1], euclideanDist(x, row[:-1])))
        
    return lista2

def grupowanie(lista):
    slownik = {}
    for y in lista:
        if y[0] not in slownik:
            slownik[y[0]] = []
        slownik[y[0]].append(y[1])
        
    return slownik

def sumowanie(slownik, k):
    slownik2 = {}
    for x in slownik.keys():
        slownik[x] = sorted(slownik[x])
        slownik2[x] = 0
    
    for x in range(k):
        for y in slownik.keys():
            slownik2[y] += slownik[y][x]
            
    return slownik2

def najmniejsza(slownik2):
    values = sorted(slownik2.values())
    slownik3 = {k : v for (v, k) in slownik2.items()}

    if values[0] == values[1]:
        return -1
    return slownik3[values[0]]

filename = 'zaj4/australian.dat'
data = loadData(filename)

x = [1.0 for x in range(len(data[0])-1)]

lista = klasaDec(x, data)
slownik = grupowanie(lista)
slownik2 = sumowanie(slownik, 5)
print(najmniejsza(slownik2))

