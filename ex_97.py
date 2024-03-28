# import asyncio
#
# async def wspolprogram():
#     print("Początek współprogramu")
#     await asyncio.sleep(2)  # Symulacja operacji asynchronicznej
#     print("Koniec współprogramu")
#
# # Utwórz pętlę asynchroniczną
# async def main():
#     print("Rozpoczęcie programu")
#     await wspolprogram()
#     print("Zakończenie programu")
#
# # Uruchom pętlę asynchroniczną
# asyncio.run(main())

from time import sleep


def wspolprogram():
    print("Początek współprogramu")
    sleep(2)  # Symulacja operacji asynchronicznej
    print("Koniec współprogramu")

# Utwórz pętlę asynchroniczną
def main():
    print("Rozpoczęcie programu")
    wspolprogram()
    print("Zakończenie programu")

# Uruchom pętlę asynchroniczną
main()