"""
Zad. 6
Załóżmy, że mamy posortowaną tablicę 1 000 000 000 liczb. Chcemy znaleźć indeks w tablicy liczby o  danej wartości.
- algorytm A przeszukuje tablicę metodą brute force o złożoności O(n)
- algorytm B przeszukuje tablicę wyszukiwaniem binarnym o złożoności O(logn).

Przyjmijmy, że sprawdzenie jednego elementu w tablicy zajmuje 1 ms. Które z poniższych zdań jest  prawdziwe?
A. Algorytm A wykona się szybciej od algorytmu B
B. Algorytm B wykona się co najmniej 1 milion razy szybciej od algorytmu A C.
C. Algorytm B wykona się 1000 razy szybciej od algorytmu A
D. Oba algorytmy wykonają się w czasie krótszym niż 24 godziny

"""

("A będzie się wykonywać tyle razy ile jest liczb - n razy - dla całej 10^9 raza"
 "czyli 10^9 ms = 10^6 s = 11.57 dnia"
 "B wykona sie log10(n) = 10^9 -> x = 9"
 
 "odp. B")
