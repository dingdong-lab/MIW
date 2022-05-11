# Posortuj słownik według wartości
capitals = {"Polska": "Warszawa", "Niemcy": "Berlin", "Rosja": "Moskwa", "Czechy": "Praga", "Słowacja": "Bratysława", "Ukraina": "Kijów", "Białoruś":"Mińsk", "Litwa": "Wilno"}
capitals2 = capitals.copy()
capital = capitals.values()
capital = sorted(capital)
capitals2 = {k : v for (v, k) in capitals.items()}
print(capitals2)
capitals = {capitals2[k] : k for k in capital}
del capitals2
del capital
print(capitals)

# Co to jest wyznacznik ?
# Wyznacznik to odwzorowanie elementów macierzy na wartość rzeczywistą, tworząc z nich iloczyny
# gdzie każdy element potwarza się tylko raz

# Kiedy można uzyskać macierz odwrotną ?
# Kiedy mamy macierz kwadratową i macierz jest nieosobliwa

# Jak obliczyć macierz odwrotną
# Macierz obliczamy ze wzoru (algorytmu) A^-1 = (A^d)^T/(det A), gdzie
# A^d - macierz dopełnień algebraicznych
# ^T - macierz transponowana
# det A - wyznacznik macierzy
# Dopełnienie algebraiczne liczymy z algorytmu, który dla każdego elementu przyporządkowuje mu jego dopełnienie ze wzoru
# A^d_i,j = (-1)^(i+j)*(det A_i,j), z kolei det A_i,j liczymy poprzez
# wyznacznenie wyznacznika macierzy A po wykreśleniu i-tego wiersza i j-tej kolumny