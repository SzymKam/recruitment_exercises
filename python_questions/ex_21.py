"""
Dlaczego listy nie mogą być użyte jako klucze słownika?

A. Ponieważ mogą stać się za duże
B. Ponieważ są mutowalne, a więc nie są hashowalne
C. Ponieważ listy mogą mieć zduplikowane elementy
D. Listy mogą być użyte jako klucze słownika

"""
"B - alternatywą jest użycie krotki"


my_dict = {(88, 77): [1,2,3,4,5,6,7,8,9] }
print(my_dict.keys())