"""
Stwórz algorytm, który wykorzystując wszystkie możliwe permutacje danej liczby X, znajdzie taką najmniejszą liczbę Y powstałą z przestawienia cyfr liczby X, że Y > X. Przykładowo:

Gdy X = 123, to Y = 132
Gdy X = 313, to Y  = 331
Etc.

Gdy natomiast nie jest możliwe otrzymanie takiej liczby, gdy np.
X = 333,

To niech program wyświetla komunikat: “None”.

"""

from itertools import permutations


def permutations_func(number):

    digits = [digit for digit in str(number)]

    result = sorted(permutations(digits))

    for permutation in result:
        perm_number = int(''.join(map(str, permutation)))
        if perm_number > int(number):
            return perm_number

    return "None"


print(permutations_func(112))