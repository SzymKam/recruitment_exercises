"""
Działające w nieskończonej pętli procesy ubiegają się o dostęp do sekcji krytycznej,
w której  modyfikują współdzieloną zmienną. Procesy ustawiają wartość tej zmiennej na aktualny czas.
Poza  modyfikacją współdzielonej zmiennej, procesy nie żądają dostępu do innej sekcji krytycznej.
W programie rozwiązującym tak zdefiniowany problem:
A. Może dojść do zakleszczenia (deadlock)
B. Może dojść do zagłodzenia (starvation)
C. Żadne z powyższych nie jest prawdą

"""
'C?'
