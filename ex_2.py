"""
Given an integer n and two other values, build an array of size n filled with these two values alternating.
Examples
5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []
"""


def arr(number, value_1, value_2):
    list = []
    for num in range(number):
        if num % 2 == 0:
            list.append(value_1)
        else:
            list.append(value_2)
    return list


assert arr(5, True, False) ==  [True, False, True, False, True]
assert arr(10, "blue", "red") ==  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
assert arr(0, "one", "two") == []