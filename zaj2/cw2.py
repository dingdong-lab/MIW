print(bool(' '))
print(bool(''))
print(bool(0))
print(bool(1))
print(bool('0'))
print(bool('1'))
print(bool([]))
print(bool([',']))
 
lancuch = "Super przedmiot bamberko"
if 'a' in lancuch:
    print('W lancuchu jest a')
else:
    print('W lancuchu nie ma a')
    
for y in range(0, 20+1):
    print(y)
    
ciag = ""
lista = []
for x in range(len(lancuch)):
    if lancuch[x] != ' ':
        ciag += lancuch[x]
    if lancuch[x] == ' ' or x == len(lancuch)-1:
        lista.append(ciag)
        ciag = ""
        
print(lista)
 
haslo = "testHasla!"
 
def passValid(haslo):
    if len(haslo) < 10:
        return False
    elif '!' not in haslo:
        return False
    
    valid = False
    for x in haslo:
        if ord(x) >= ord('A') and ord(x) <= ord('Z'):
            valid = True
            break
    
    if not valid:
        return False
    
    valid = False
    for x in haslo:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            valid = True
            break
    
    return valid
 
print(passValid(haslo))
 
lista = [1,2,99,4,5]
for x in lista:
    if x == 99:
        continue
    print(x)
    
def czyNalezy(lancuch, element):
    nalezy = False
    x = len(lancuch)-1
    
    while x >= 0:
        if lancuch[x] == element:
            nalezy = True
            break
        x -= 1
        
    return nalezy
 
print(czyNalezy(lista, 1))
 
handle = open("zaj2\data.txt", "r")
for line in handle:
    print(line)
handle.close()
  
handle = open("zaj2\data.txt", "r")  
for line in handle:
    print(line, end='')
handle.close()