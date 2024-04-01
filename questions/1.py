"""
Model OSI (Open Systems Interconnection) to standardowa architektura sieci komputerowych,
opracowana przez ISO, aby ustandaryzować komunikację pomiędzy różnymi systemami komputerowymi.
Składa się on z siedmiu warstw, każda zajmuje się innym aspektem kompunikacji.
1. Warstwa fizyczna - najniższa warstwa. Odpowiada za przesył surowych danych binarnych
między urządzeniami. Są to przewody, syngały elekryczne/optyczne/radiowe. Dane pzesyłane w
formie binarnej.
2. Warstwa łącza danych - odpowiada za bezbłędną transmisję danych między dwoma urządzeniami
(kontrola i nadzór nad warstwą fizyczną). Zapewnia kontrolę błędów - wykrywanie i korekcję.
Pakowanie danych w ramki.
3. Warstwa sieciowa - ma wiedzę na temat topologii sieci. Rozpoznaje drogi łączące dwa urządzenia
i decyduje ile informacji jaką drogą/połączeniem przesłać. Odpowiada za adresowaniu, routowanie, i wybór najlepszej ścieżki dla pakietów danych. Tutaj
działają protokoły IP.
4. Warstwa transportowa -
"""