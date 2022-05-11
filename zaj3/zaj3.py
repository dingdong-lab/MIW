from telnetlib import STATUS


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

filename = 'zaj3/australian.dat'
data = loadData(filename)
# Praca domowa
#status = {euclideanDist(data[0],x) : x[14] for x in data}
status = {0 : [], 1 : []}
for row in data[1:]:
    status[int(row[-1])].append(euclideanDist(data[0][:-1], row[:-1]))
status[0] = sorted(status[0])
status[1] = sorted(status[1])
print(status)
#print(status)
#status = {k: v for k, v in sorted(status.items(), key=lambda item: item[1])}
