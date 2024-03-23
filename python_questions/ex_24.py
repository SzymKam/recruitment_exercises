"""
Rozważ poniższe “snippety”. Które zdanie jest prawdziwe?

lst = ["I", "am", "Python", "programmer"]


S1: s = ""
   for x in lst:
     s += x


S2: s = "".join(lst)

A.   S2 jest mniej wydajne, ponieważ join() wywołuje się dla każdego elementu w liście
B.   S2 jest bardziej efektywne ponieważ konkatenacja jest wykonywana w jednej iteracji i każda litera kopiowana jest tylko raz
C.   S1 jest mniej efektywne, ponieważ stringi są niemutowalnymi obiektami, więc każda iteracja tworzy nowy obiekt.
D.   Nie ma znaczącej różnicy między dwoma podejściami

S2 jest bardziej wydaje ponieważ konkatenacja jest wykonywana w jednej iteracji i każda litera kopiowana jest tylko raz
"""