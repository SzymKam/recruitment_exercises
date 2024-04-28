"""
Jak traceroute wykonuje swoje zadanie?

Traceroute służy do śledzenia ścieżki pakietów danych w sieci. Wysyłane są specjalne pakiety danych
z rosnącym polem TLL (Time to Live). TTL określa maksymalną liczbę przystanków lub przekroczeń przed tym
jak zostanie odrzucony. Każdy router na trasie pakietu obniża TLL o 1. Kiedy TLL = 0, router odrzuca pakiet
i wysyła informację zwrotną o przekroczonym czasie - pozwala go to zlokazlizować wraz z IP.

Zaczynamy od TLL = 1 i zwiększamy go o 1 przy każdym etapie. Generowana jest listra routerów i czas ich odpowiedzi
(ping). Na docelowym hoście zwrócone zostanie prawdopodobnie PORT UNREACHABLE - ponieważ pakiet wysłany jest z
numerem portu powyżej 30000.

"""