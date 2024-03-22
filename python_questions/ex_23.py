"""
Co będzie rezultatem poniższego kodu?


class A:
  brothers = []
  def __init__(self, name):
    self.name = name

a = A('Richard')
b = A('Elly')
a.brothers.append('John')

print(a.name, a.brothers, b.name, b.brothers)



A. ‘Richard’, [‘John’], ‘Elly’, []
B. ‘Richard’, [‘John’], ‘Elly’, [‘John’]
C. ‘Elly’, [‘John’], ‘Elly’, [‘John’]
D. ‘Elly’, [‘John’], ‘Elly’, []

"""

"odpowiedz A"

class A:
    brothers = []

    def __init__(self, name):
        self.name = name


a = A('Richard')
b = A('Elly')
a.brothers.append('John')

print(a.name, a.brothers, b.name, b.brothers)

# Richard, [John], Elly, []