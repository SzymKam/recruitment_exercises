"""
Opisz różnice pomiędzy protokołami TCP a UDP

TCP - Transmission Control Protocol
UDP - User Datagram Protocol
Oba protokoły służą służą do transferu danych w sieciach komputerowych.

Połączenie vs. bezpołączeniowość -
TCP jest zorientowany na połączenie
(musi najpierw połączyć się z odbiorcą, potwierdzenie i synchronizacja)
potem rozłączyć połączenie.
UDP - bezpołączeniowe. Każdy pakiet jest wysyłany osobno, bez dodatkowych
formalności.

Potwierdzenia i kontrola przepływu -
TCP używa potwierdzeń, dzięki czemu dane są przekazywane w odpowiedniej
kolejności, kontrola przepływu oraz błędów. Mniejsze przeciążenie sieci.
UDP - nie daje takiej gwarancji, ale szybsze

TCP gdy ważna jest niezawodność, np. przesył plików, stron.
UDP - gdy potrzeba szybkości np. gry online, transmije strumieniowe
"""