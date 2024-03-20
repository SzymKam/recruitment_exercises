"""
Zad. 9.
Załóżmy, że mamy tablicę skrótów pozwalającą na przechowywanie 10 elementów oraz 4 funkcje  obliczania skrótów,
z których każda przyjmuje jako argument napis i na jego podstawie wyznacza  indeks w tablicy skrótów:
- Funkcja A zwracająca jako indeks liczbę 3 dla wszystkich napisów
- Funkcja B zwracają jako indeks długość napisu
- Funkcja C zwracająca jako indeks pierwszą literę napisu to znaczy wszystkie napisy które zaczynają się  na przykład
nocach umieszczone są pod jednym indeksem
- Funkcja D zwracająca jako indeks wynik następującej operacji (z uwzględnieniem polskich znaków): kolejne liczby naturalne sumujemy je dla podanego napisu i wynik podzielmy modulo przez rozmiar tablicy skrótu
Zad. 9.1
Które z powyższych funkcji zapewniłyby optymalny rozkład elementów tablicy skrótów dla imion  Anna Michał Maciej Daniel.
1. A
2. B
3. C
4. D
Zad. 9.2
Które z powyższych funkcji zapewniłyby optymalny rozkład elementów w tablicy skrótów dla cyfr  rzymskich: x, xx, xxx.
1. A
2. B
3. C
4. D
Zad. 9.3
Które z powyższych funkcji zapewniłyby optymalny rozkład elementów w tablicy skrótów dla tytułów  filmów „Gladiator”, „Zielona mila”, „Dwunastu gniewnych ludzi”
1. A
2. B
3. C
4. D

"""
"""9.1
Anna 3, 4, A, (65+110+110+97)%4 -> 382%4 =  2;
Michał 3, 6, M, (77, 105, 99, 104, 97, 108)%6 ->590%6 = 2
Maciej 3, 6, M, (77, 97, 99, 105, 101, 106) -> 585%6 = 3
Daniel 3, 6, D, (68, 97, 110, 105, 101, 108) -> 589%6 = 1

D - prawdopodobnie
9.2
B

9.3
B, C - dłuższe,"""