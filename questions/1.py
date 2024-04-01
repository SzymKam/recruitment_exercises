"""
Model OSI (Open Systems Interconnection) to standardowa architektura sieci komputerowych,
opracowana przez ISO, aby ustandaryzować komunikację pomiędzy różnymi systemami komputerowymi.
Składa się on z siedmiu warstw, każda zajmuje się innym aspektem kompunikacji.

NIŻSZE - znajdują drogę do celu. Dzielą dane. Weryfikacja danych. Nie sprawdzają sensu danych.

1. Warstwa fizyczna - najniższa warstwa. Odpowiada za przesył surowych danych binarnych
między urządzeniami. Są to przewody, syngały elekryczne/optyczne/radiowe. Dane pzesyłane w
formie binarnej.
2. Warstwa łącza danych - odpowiada za bezbłędną transmisję danych między dwoma urządzeniami
(kontrola i nadzór nad warstwą fizyczną). Zapewnia kontrolę błędów - wykrywanie i korekcję.
Pakowanie danych w ramki.
3. Warstwa sieciowa - ma wiedzę na temat topologii sieci. Rozpoznaje drogi łączące dwa urządzenia
i decyduje ile informacji jaką drogą/połączeniem przesłać. Odpowiada za adresowaniu, routowanie, i wybór najlepszej ścieżki dla pakietów danych. Tutaj
działają protokoły IP.
4. Warstwa transportowa - odpowiada za dostarczanie danych w sposób niezawodny i kontrolowanie
przepływu danych między urządzeniami końcowymi. Gwarantuje, że dane zostaną dostarczone w całości
i w odpowiedniej kolejności. Działąją protokoły TCP.

WARSTWY WYŻSZE - współpraca z oprogramowaniem. Pozwalają na komunijację z warstwami niższymi

5. Warstwa sesji - zarządza komunikacją między aplikacjami na różnych urządzeniach (synchronizacja).
Odpowiada za rozpoczęcie, utrzymanie oraz zakończenie sesji między urządzeniami. Ma mechanizmy
odzyskiwania sesji.
6. Warstwa prezentacji - Przetwarzają dane płynące z aplikacji do postaci kanonicznej.
żeby warstwy niższe zawsze otrzymywały dane w tym samym formacie. W drugą stronę tłumaczy dane
przychodzące na zgodne z wewnętrzną reprezentacją systemu docelowego (różne systemy róznie
interpertują dane).
7. Warstwa aplikacji - dostarcza interfejsy dla aplikacji. Odpowiada za komunikację między
aplikacjami i obsługuje konktretne protokoły i usługi: HTTP, SMTP, FTP.
"""