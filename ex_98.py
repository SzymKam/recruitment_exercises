def zewnetrzna_funkcja(x):
    def wewnetrzna_funkcja(y):
        return x + y
    return wewnetrzna_funkcja


closure = zewnetrzna_funkcja(10)
wynik = closure(5)

print(wynik)