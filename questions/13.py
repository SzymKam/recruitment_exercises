"""
Jakie zakresy IPv4 są ustanowione jako prywatne przez standard RFC 1918?

Te zakresy adresów IPv4, są przeznaczone dla wykorzystania w wewnętrznych sieciach i nie są publucznie
routowane w Internecie. Są to zakresy:

* 10.0.0.0 - 10.255.255.255 (10.0.0.0/8) - czyli adresy zaczynające się od 10.xx.xx.xx - sieci korporacyje i domowe
* 172.16.0.0 - 172.31.255.255 (172.16.0.0/12) - adresy z zakresu 172.16-31.xx.xx - korporacyjne
* 192.168.0.0 - 192.168.255.255 (192.168.0.0/16) - adresy 192.168.xx.xx - sieci domowem małe firmy i prywatne środowiska

"""