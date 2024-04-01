"""Czym się różni Hub od Switcha od Routera?
urządzenia wykorzystywane w sieciach komputerowych.
Hub - najprostsze. Urządzenie fizyczne, działa na 1 warstwie modelu OSI. Dane z jednego
portu przsyła na wszystkie inne porty. Wszystkie urządzenia podłączone do Huba, widzą wszystkie
dane przesyłane przez inne urządzenia do niego podłączone. Powoduje to duże obciązenie sieci
oraz ryzyko kolizji.

Switch - urządzenie warstwy 2 modelu OSI - urządzenie dołączania na poziomie łącza danych.
Działa na zasadzie tablicy adresów MAC - przypisuje adresy urządzeń podłązconych do
odpowiednich portów. Przesyła dane tylko do odpowiedniego urządzenia, będącego docelowym.
Mniejszy ruch w sieci. Wydajność.

Router - urządzenie 3 warstwy modelu OSI - urządzenie warstwy sieciowej. Działa na podstawie
adresów IP, może przesyłać dane między sieciami. Podejmuje decyzje o wyborze najlepszej ścieżki
dla pakietów danych. Przekazuje dane miedzy np. LAN, Internet.
"""