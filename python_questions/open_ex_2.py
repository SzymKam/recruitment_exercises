"""
context manager - jest to obiekt który możemy wywołać poprzez instrukcję 'with'. Umożliwia on zarządzanie zasobami
i posiada metody __exit__ oraz __enter__.

sys,argv - w pythonie jest to lista, która zawiera argumenty przekazywane do skryptu z linii poleceń.
Za pomocą sys.argv[0, 1, 2 ....] można pobrać agrumenty z linii poleceń. Arg o indeksie [0] to nazwa skryptu

pep-8 - jest to zbiór zasad, okreslających konwencję formatowania kodu pythona. Np. nazewnictwo, ukłdu kodu, znaków,
komentarzy - celem poprawy spójności i czytelności

DRY - dont repeat yourself - kod i informacje nie powinny być duplikowane - wprowadza to niespójność

KISS - keep it simple stupid - staramy się tworzyć kod prosty, jak najmniej skomplikowany

Pythonic Code - to kod napisane zgodnie z zasadami, konwencją języka python

magic methods - są specjalne metody w jezyku python. zaczynają się i kończą dwiema podkresleniami np. __init__.
Nazywa się je takze dunder methods - od double underscore. Pozwalają na definiowanie specjalnego zachowania dla
obiektów w pythonie np. konstruktora __init__, reprezentacji tekstowej __str__, __repr__ - tzw przeciążanie operatorów

linux komendy -
to 15 podstawowych poleceń systemu Linux, które mogą być przydatne dla programisty:

    ls - Wyświetla zawartość bieżącego katalogu.
    cd - Zmienia bieżący katalog. Na przykład, cd /home przeniesie Cię do katalogu /home.
    pwd - Wyświetla ścieżkę do bieżącego katalogu.
    touch - Tworzy nowy, pusty plik. Na przykład, touch example.txt utworzy plik o nazwie example.txt.
    cat - Wyświetla zawartość pliku. Na przykład, cat example.txt wyświetli zawartość pliku example.txt.
    rm - Usuwa plik. Na przykład, rm example.txt usunie plik example.txt.
    cp - Kopiuje plik. Na przykład, cp source.txt dest.txt skopiuje source.txt do dest.txt.
    mv - Przenosi lub zmienia nazwę pliku. Na przykład, mv old.txt new.txt zmieni nazwę old.txt na new.txt.
    mkdir - Tworzy nowy katalog. Na przykład, mkdir new_directory utworzy katalog o nazwie new_directory.
    rmdir - Usuwa katalog. Na przykład, rmdir directory usunie katalog o nazwie directory.
    man - Wyświetla podręcznik dla danego polecenia. Na przykład, man ls wyświetli podręcznik dla polecenia ls.
    grep - Wyszukuje tekst w pliku. Na przykład, grep "example" file.txt wyszuka example w file.txt.
    sudo - Pozwala na wykonanie polecenia jako inny użytkownik, zwykle jako użytkownik root.
    chmod - Zmienia uprawnienia do pliku. Na przykład, chmod 755 file.txt ustawi uprawnienia do file.txt na 755.
    chown - Zmienia właściciela pliku. Na przykład, chown user:group file.txt zmieni właściciela file.txt na user i grupę na group.

Pamiętaj, że możesz zawsze użyć polecenia man aby uzyskać więcej informacji na temat każdego z tych poleceń. Na przykład, man ls dostarczy Ci szczegółowe informacje na temat polecenia ls.

proces -




"""