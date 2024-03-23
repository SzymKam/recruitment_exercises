"""
Co będzie rezultatem poniższego kodu?

import copy

class A(object):
  pass

a = A()
a.lst = [1, 2, 3, 4]
a.str = 'cats and dogs'
b = copy.copy(a)
a.lst.append(100)
a.str = 'cats and mice'

print(b.lst)
print(b.str)


A. [1, 2, 3, 4, 100], ‘cats and mice’
B. [1, 2, 3, 4], ‘cats and mice’
C. [1, 2, 3, 4, 100], ‘cats and dogs’
D. [1, 2, 3, 4], ‘cats and dogs’

"""

"""
Rezultatem poniższego kodu będzie:

C. [1, 2, 3, 4, 100], ‘cats and dogs’

Wyjaśnienie:

Pierwsza kopia b jest wykonana przy użyciu copy.copy(a). copy.copy() tworzy płytką kopię obiektu, co oznacza, że nowy 
obiekt b będzie zawierał referencje do tych samych obiektów, co obiekt a.
W wyniku dodania 100 do listy a.lst, zmiana ta będzie widoczna także w liście b.lst, ponieważ obiekt b zawiera 
referencję do tej samej listy, co obiekt a.
Jednak zmiana wartości atrybutu a.str na 'cats and mice' nie ma wpływu na obiekt b, ponieważ zmiana ta odnosi się 
do referencji do innego obiektu stringa. Obiekt b nadal zawiera referencję do oryginalnego stringa 'cats and dogs', 
ponieważ nie został on zmieniony.
"""

import copy

class A(object):
  pass

a = A()
a.lst = [1, 2, 3, 4]
a.str = 'cats and dogs'

b = copy.copy(a)
a.lst.append(100)
a.str = 'cats and mice'

print(b.lst)
print(b.str)