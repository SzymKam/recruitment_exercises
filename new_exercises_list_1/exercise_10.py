def doubler():
    x = 5

    def inner_doubler():
        global x
        return x * 2

    return inner_doubler()


x = 2
y = doubler()
print(y)
print(x)

"""it returns 4, because the function inner calls x value as global. x in global we add out of function
as x=2. Valus out fnc are global. global x loads this variable into function, not create new local variable"""