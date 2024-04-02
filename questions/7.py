"""
Jaka jest różnica pomiędzy ping localhost i ping 127.0.0.1?

Są one bardzo podobne i odwołują się do adresu loopback, używanego do komunikacji kompuera
z samym sobą. ping localhost musi być najpierw zmapowane na adres loopback w plików hostów
systemu operacyjnego, musi najpierw przetłumaczyć localhost na adres IP i przejść na niego.

ping 127.0.0.1 - ping zostanie od razu wysłane na ten adres docelowy.

W praktyce jeśli localhost zostało ustawione inaczej w systemie, może nie zadziałąć
(skrajnie rzadka i niepolecana praktyka)
"""