"""
Jak wybrać losowy, wolny port?

Można użyć portu zero. Wtedy zostanie automatycznie przyznany wolny losowy (efemeryczny)
port z puli aktualnie dostępnych (niezastrzeżonych).
Nie wszystkie systemy obsługują tę funkcję. Jednak wówczas
nie mamy kontroli nad tym jaki port został przydzieony. Może to prowadzić do konfliktów.
"""