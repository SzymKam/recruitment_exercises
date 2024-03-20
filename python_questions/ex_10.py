"""
Aplikację mobilną do przyjmowania zamówień od klientów pizzerii, której jedną z funkcji jest
dodawanie zamówień do listy korzystając z niej zarówno kelnerzy i kucharze.
Kelnerzy dodają do niej  zamówienia, kucharze je pobierają i następnie wypiekają pizzę.
Interakcje między tymi 2 stronami  można zobrazować w postaci kolejki, w której kelnerzy dodają zamówienia na jej końcu,
a kucharze pobierają z jej początku i przygotowują zamówienie. Zastanów się, jakiej struktury danych
powinieneś użyć do implementacji takiego rozwiązania. Czy byłaby to tablica (Array) czy lista wiązana  (LinkedList)?

A. Array, ponieważ jest lepsza od LinkedList w dostępie swobodnym do elementów
B. LinkedList, ponieważ jest lepsza od Array we wstawianiu i usuwaniu elementów
C. LinkedList, ponieważ jest lepsza od Array w dostępie swobodnym do elementów
D. Array, ponieważ jest lepsza od LinkedList we wstawianiu i usuwaniu elementów

"""

'B - bo chcemy brać pierwsze z kolei zamówienie, nie będzie potrzeby dostępu do elementoów ze środka'