
def abbrev_name(name):
    first_name, last_name = name.split()

    return f"{first_name[0].upper()}.{last_name[0].upper()}"

# print(abbrev_name("Sam Harris"))


assert abbrev_name("Sam Harris") == "S.H"
assert abbrev_name("patrick feenan") == "P.F"
assert abbrev_name("Evan C") ==  "E.C"
assert abbrev_name("P Favuzzi") == "P.F"
assert abbrev_name("David Mendieta") =="D.M"