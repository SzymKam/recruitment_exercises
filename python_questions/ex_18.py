"""
Jaki będzie rezultat poniższego kodu?

import random

def func(type='a'):
 if type == 'a':
   return 'Mark'
 elif type == 'i':
   return random.randint(0, 1000)

def dec(func, type_):
 x = 8
 def wrapper():
   value = func(type_)
   if isinstance(value, int):
     return value * x
   elif isinstance(value, basestring):
     return 'H1' + value
 return wrapper

print(dec(func,'i')())


A. Zostanie rzucony wyjątek, ponieważ funkcja nie może przyjmować parametru, który jest inną funkcją oraz zwracać funkcje jako rezultat
B. dec jest wołany i zwraca wrapper. Wrapper jest wywołany i zwraca losowego integer-a, który jest wydrukowywany
C. Pojawi się SyntaxError w linii dec(func, ‘i’)()
D. Pojawi się NameError przy “return value + c”, ponieważ x jest niezdefiniowany wewnątrz func

"""
import random


def func(type='a'):
    if type == 'a':
        return 'Mark'
    elif type == 'i':
        return random.randint(0, 1000)


def dec(func, type_):
    x = 8
    def wrapper():
        value = func(type_)
        if isinstance(value, int):
            return value * x
        elif isinstance(value, str):
            return 'H1' + value
    return wrapper


print(dec(func,'i')())

"B"
