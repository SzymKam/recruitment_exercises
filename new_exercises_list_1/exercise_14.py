from random import randint

def main():
    """Returns a list of integers, sometimes 1-5, otherwise 1-10"""
    x = (1, 2, 3, 4, 5)
    if randint(1, 10) >= 7:
        x.extend(6, 7, 8, 9, 10)
    return x

"""tuple is non mutable, should use list"""
print(main())