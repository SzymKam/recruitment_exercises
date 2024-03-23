import datetime


class Human(object):
    name = None
    gender = None
    birthdate = None

    def __getattr__(self, name):
        if name == 'age':
            return datetime.datetime.now() - self.birthdate
        else:
            return None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)


h = Human()
h.birthdate = datetime.datetime(1980, 8, 20)
h.age = 28

print(getattr(h, 'age'))
print(h.age)


"""
A. datetime.timedelta object
B. 28
C. datetime.datetime object
D. Nieskończona rekursja oraz RuntimeError

"""

'odpowiedź B - 28'