"""
Jaki będzie rezultat poniższego kodu?

class Organization(object):
 __employees = []

google = Organization()
google.__employees.append('Erik')



A. Zostanie rzucony wyjątek AttributeError, gdyż w obiekcie nie ma atrybutu __employees.
B. Nowe pole __employees jest dynamicznie tworzone i zostaje w nim umieszczone słowo ‘Erik’
C. Pojawia się wyjątek AttributeError ponieważ wszystkie atrybuty rozpoczynające się od __ są prywatne i nieosiągalne spoza kontekstu klasowego
D. String ‘Erik’ zostanie dodany do listy __employees

"""

"A oraz C"

class Organization(object):
 __employees = []

google = Organization()
google.__employees.append('Erik')