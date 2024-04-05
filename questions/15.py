"""
Co to jest ARP?

ARP - Address Resolution Protocol - to protokół sieciowy, który umożliwia
mapowanie logicznych adresów warstwy sieciowej (3 warstwa) na fizyczne
adresy warstwy łącza danych np. MAC(warstwa 2). Umożliwienie komunikacji
w tej samej sieci.
- Aby ustalić adres fizyczny hosta docelowego, wysyłane żądanie ARP
do wszystkich hostów (broadcastowanie) w tej samej sieci.
- Zapytanie zawiera adres logiczny hosta docelowego oraz adres fizyczny
hosta wysyłąjącego zapytanie
- na zapytanie odpowiada tylko ten host, którego adres logiczny jest
identyczny z adresem logicznym w zapytaniu
- odpwiedź zawiera adres logiczny i fizyczny hosta docelowego
- odebrany adres fizyczny zapisywany jest w tablicy ARP i parowany z
adresem logicznym hosta docelowego, dzięki czemu nie będzie
wymagane ponowne odkrywanie adresu fizycznego do momentu wyczyszczenia
tablicy
"""