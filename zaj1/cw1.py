print("No siema")
 
slowo1 = "No "
slowo2 = "siema"
slowo3 = "co tam"
 
zmienna1 = {17}
zmienna2 = 17
zmienna3 = 'string'
 
print (type(int))
print (type(zmienna2))
print (type(zmienna3))
 
# print ('{}{}{}'.format("No ","siema ","co tam"))
#
# imie  = input('Podaj imie: ')
# print ('czesc{}'.format(imie))
# print (imie[::-1])
 
lista = ["siema","nie", "wiem","co"]
 
joined = ' '.join(lista)
print(joined)
 
splitted = joined.split(' ')
print(splitted)
 
zmiennakolejna = "Metody Inżynierii Wiedzy są najlepsze"
 
print('{} ma długość {}'.format(zmiennakolejna,len(zmiennakolejna)))
 
nopl = zmiennakolejna.replace("ą","a").replace("ż","z").replace(" ","")
print('{} ma długość {}'.format(nopl,len(nopl)))
 
jakisset = set(nopl)
print('{} ma długość {}'.format(jakisset,len(jakisset)))
 
jakas_liczba = 1
lakis_string = "siema"
z = (lakis_string,jakas_liczba)
print (z)
print(type(z))
 
letterlist=["a","b","c"]
numberlist= [1,2,3]
 
added = letterlist + numberlist
 
print(added)
print(type(added))
 
print(added[3:4])
print(type(added[3:4]))
 
print(added.index("c"))
 
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
 
lista1.extend(lista2)
print(lista1)
 
capitals = {"Polska": "Warszawa", "Niemcy": "Berlin", "Rosja": "Moskwa", "Czechy": "Praga", "Słowacja": "Bratysława", "Ukraina": "Kijów", "Białoruś":"Mińsk", "Litwa": "Wilno"}