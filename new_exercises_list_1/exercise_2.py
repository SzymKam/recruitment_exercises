"""
What’s the value of x?
x = map(lambda i: i**2, range(5))
"""
# map() zwraca iterator czyli <map object at 0x000000>
# trzeba użyć na nim list() aby zwrócił wartości

x = map(lambda i: i**2, range(5))
print(x)