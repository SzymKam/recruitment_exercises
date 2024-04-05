"""
Jak byś podejrzał zawartość pakietu IP?

Można skorzystać z kilku narzędzi
- tcpdump - dostępne w unix-owych systemach. Umożliwia przechwycenie oraz
analizę ruchu sieciowego. Można przechwywywać ruch na określonym
interfejsie sieciowym i wyświetlania informacji o przechwyconych
pakietach i nagłówkach IP.
tcpdump -xx -i eth0
-xx - wyświetlanie nagłówków i danych w formie heksagonalnej
-i eth0 - określa interfejs sieciowy na jakim ma być przechwytywany ruch


- tshark - wiersz poleceń, odpowiednik Wiresharka. Umożliwia analizę
przechwyconych pakietów bez potrzby uruchamiania interfejsu graficznego.
Używany tak samo jak tcpdump, ale większe możliwości filtrowania i
analizy pakietów.
tshark -i eth0 -x
-i eth0 - sprawdzanie interfejsu eth0
-x forma szesnastkowa


la /sys/class/net - lista interfejsów sieciowych, u mnie to:
 - enp7s0 - interfejs ethernet
 - lo  - interfejs pętli zwrotnej, używany do komunikacji wewnatrz systemu
 - wlp8s0 - interfejs bezprzewodowy WiFi

"""