"""
Jaki będzie rezultat poniższego kodu?

class A(object):
  def __repr__(self):
    return 'instance of A'

a = A()
b = a
del a
print(b)

A. a zostało usunięte i b odnosi się do None, ponieważ obiekt, do którego się odnosił, został skasowany
B. a zostało usunięte, ale obiekt, do którego się odnosiło nie, ponieważ b jest do niego wciąż przypisane
C. a i b zostało usunięte ponieważ obiekt, do którego te zmienne się odnosiły, został usunięty
D. a zostało usunięte, więc obiekt do którego się odnosiło też został usunięty

"""

"odpowiedz B"
