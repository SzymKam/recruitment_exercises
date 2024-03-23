"""
Co będzie rezultatem poniższego kodu?

class Human(object):
  def __setattr__(self, name, value):
    if name == 'gender':
      if value in ('male', 'female'):
        self.gender = value
      else:
        raise AttributeError('Gender can only be male or female')

h = Human()
h.name = 'Mary'
h.gender = 'female'
print(h.gender)


A. ‘female’
B. Nieskończona rekursja i RuntimeError
C. AttributeError
"""

"""
B. Nieskończona rekursja i RuntimeError.

Wyjaśnienie:

W metodzie __setattr__ zdefiniowano specjalne zachowanie dla przypadku, gdy atrybut gender jest ustawiany.
Jednakże, wewnątrz tej metody próbuje się ustawiać wartość atrybutu gender, co ponownie prowadzi do wywołania metody __setattr__. To spowoduje nieskończoną rekursję, ponieważ metoda __setattr__ jest wywoływana rekurencyjnie dla tego samego atrybutu gender w klasie Human.
Ostatecznie, po osiągnięciu maksymalnej głębokości rekursji interpreter wywoła RuntimeError.

"""