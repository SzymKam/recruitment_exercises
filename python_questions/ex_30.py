"""
Co będzie rezultatem poniższego kodu?

class A:
  pass

class B:
  pass

a = A()
b = B()
print(type(a) == type(b), type(a), type(b))


A. False, instance, instance
B. True, instance, instance
C. True, object, object
D. False, A, B

"""

"""odpowiedź D
false bo jedna z nich jest instancją klasy A, druga B
 A i B bo zwrócą się jako typy A i B
"""
