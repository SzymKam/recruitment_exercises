"""
Które zdanie jest prawdziwe?

S1: l = [i for i in range(10000)]
S2: x = (i for i in range(10000))


A. S1 tworzy listę. Wszystkie elementy (liczby od 0 do 9999) przechowywane są w pamięci
B. S2 tworzy funkcję generatora. Jego elementy nie są przechowywane w pamięci, ponieważ są generowane przy każdym wywołaniu metody next().
C. S1 tworzy listę, elementy nie są przechowywane w pamięci - są one generowane przy wywołaniu metody next()
D. S2 tworzy funkcję generatora. Wszystkie elementy (liczby od 0 do 9999) przechowywane są w pamięci

"""
'poprawne A i B'