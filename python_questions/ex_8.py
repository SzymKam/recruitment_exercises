"""
Zad. 8
Poniżej znajdują się złożoności obliczeniowe następujących struktur danych:


Tablica
Tablica skrótów
(przypadek średni)
Tablica skrótów
(przypadek
pesymistyczny)
Wyszukiwanie
O(1)
O(1)
?
Wstawianie
O(n)
O(1)
?
Usuwanie
O(n)
O(1)
?



Podaj złożoność obliczeniową dla tablicy skrótów w przypadku pesymistycznym, tzn. takim, w którym  dla różnych elementów występują kolizje przy wyznaczaniu indeksu:
A. Wszystkie operacje mają złożoność O(n)
B. Wyszukiwanie ma złożoność O(1), pozostałe operacje O(n^2)
C. Wszystkie operacje mają złożoność O(1)
D. Żadna z powyższych odpowiedni nie jest poprawna

"""
"""
Wyszukiwanie
O(n) - > trzeba przeszukiwać po elementach tablicy

Wstawianie
O(1) -> trzeba wstawić w dane miejsce

Usuwanie
O(n) -> trzeba przeszukiwać po elementach

czyli D
"""