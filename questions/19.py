"""
co to maska podsieci?

Ang. subnet mask. Jest to liczba binarna, używana w sieciach komputerowych do określenia które bity w adresie
IP identyfikują sieć, a które konkretne urządzenie w tej sieci.
Maska podsieci składa się z serii bitów o wartości 1 na początku - reprezentujące indentyfikator sieci; oraz
serii bitów o wartości 0 na końcu - reprezentujące identyfikator hosta. Maska separuje część sieciową od części
hosta w IP.


Np dla IP 192.168.1.10 stosując maskę podsieci 255.255.255.0 - pierwsze 4 bity czyli pierwsze 3 oktety, reprezentują
identyfikator sieci, a ostatni identyfikator hosta. Wówczas IP 192.168.1.0 to adres sieci, a 10 to adres hosta w sieci.
"""