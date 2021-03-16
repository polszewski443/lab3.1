import random

# Zad1
# definiuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,4^7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}
print('#############ZAD1#############')
A = [1-x for x in range(1, 11)]
print(A)
B = [4**x for x in range(0, 8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1,
# następnie wykorzystując Python Comprehension zdefiniuj nową listę,
# która będzie zawierała tylko parzyste elementy
print('#############ZAD2#############')


lista1 = []
for i in range(10):
    x = random.randint(1, 10)
    lista1.append(x)
print(lista1)
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista2)

# Zad3 Utwórz słownik z produktami spożywczymi do kupienia.
# Klucz to niech będzie nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
print('#############ZAD3#############')
slownik1 = {'mleko': 'l', 'mąka': 'kg', 'jajka': 'sztuki'}
print(slownik1)
slownik2 = {key: value for key, value in slownik1.items() if value == 'sztuki'}
print(slownik2)

# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
print('#############ZAD4#############')


def sprawdzenie(a, b, c):
    if a == b == c:
        return 'Trojkat nie jest prostokatny, jest rownoboczny'
    if a >= b and a >= c:
        if a ** 2 == b ** 2 + c ** 2:
            return 'Trojkat jest prostokatny'
        else:
            return 'Trojkat nie jest prostokatny'
    elif b >= a and b >= c:
        if b ** 2 == a ** 2 + c ** 2:
            return 'Trojkat jest prostokatny'
        else:
            return 'Trojkat nie jest prostokatny'
    elif c >= a and c >= b:
        if c ** 2 == a ** 2 + b ** 2:
            return 'Trojkat jest prostokatny'
        else:
            return 'Trojkat nie jest prostokatny'


print(sprawdzenie(2, 4, 7))

# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
print('#############ZAD5#############')


def poletrapezu(a=7, b=6, h=8):
    return ((a + b) * h) / 2


print(poletrapezu(1, 4, 5))
print(poletrapezu())

# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy),
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
print('#############ZAD6#############')


def iloczyn(a=1, b=4, ile=10):
    lista = []
    ile += 2
    lista.append(a)
    for i in range(2, ile):
        lista.append(i * b)
    return lista


print(iloczyn())
print(iloczyn(3, 2, 7))
print(iloczyn(2, 3, 5))


# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.
print('#############ZAD7#############')
#niestety mialem problem z tym zadaniem i nie udalo mi sie znalezc poprawnego rozwiazania


#def iloczyn(*wartosci):
#    if len(wartosci) != 3:
#       print('Konieczne jest wpisanie trzech wartosci!')
#       return -1
#   else:
#      wartosci = list(wartosci)
#      lista = []
#      ile[0] = ile[0] + 2
#      lista.append(wartosci[0])
#      for i in range(2, wartosci[2]):
#         lista.append(i * wartosci[1])
#         return lista


#print(iloczyn(1,2,10))
#print(iloczyn(1))


# Zad8
# Napisz funkcję, która wykorzystuje symbol **.
# Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.
print('#############ZAD8#############')


def slownik(**wartosci):
    ilosc = len(wartosci)
    licz = sum(x for x in wartosci.values())
    return ilosc, licz


print(slownik(wino=15, ocet=53, musztarda=32, chleb=12))

# Zad9 S
# twórz pakiet ciągi.
# Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi,
# a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.
print('#############ZAD9#############')
from ciagi import *

print(arytmetyczne.ntywyrazaryt(2, 6, 3))
print(arytmetyczne.sumanparyt(1, 3, 2))
print(geometryczne.ntywyrazgeom(1, 4, 2))
print(geometryczne.sumanpgeom(2, 4, 1))
