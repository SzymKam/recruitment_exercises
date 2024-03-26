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

proces i watek - W kontekście programowania, "proces" i "wątek" są dwoma ważnymi koncepcjami, szczególnie w systemach operacyjnych. Oto krótkie wyjaśnienie obu terminów:

    Proces:
        Proces jest instancją działającej aplikacji w systemie operacyjnym. Może to być program uruchomiony przez użytkownika, który wykonuje określone zadania.
        Proces ma swoją przestrzeń adresową, w której przechowywane są instrukcje programu, dane, stos i inne struktury potrzebne do jego działania.
        Każdy proces działa niezależnie od innych procesów, co oznacza, że ​​nie ma dostępu do pamięci ani zasobów innych procesów bez odpowiednich mechanizmów synchronizacji.
        Procesy mogą komunikować się ze sobą za pomocą mechanizmów takich jak potoki, gniazda sieciowe, pliki lub pamięć współdzielona.

    Wątek:
        Wątek jest mniejszą jednostką wykonawczą niż proces. W jednym procesie może być wiele wątków.
        Wątki w ramach jednego procesu mają wspólną przestrzeń adresową i zasoby, co oznacza, że ​​mogą bezpośrednio współdzielić dane i zasoby między sobą.
        Wątki w ramach jednego procesu wykonują się równolegle, co może zwiększyć wydajność aplikacji poprzez wykorzystanie wielordzeniowych procesorów.
        Wątki mogą komunikować się między sobą za pomocą mechanizmów synchronizacji takich jak semafory, mutexy, zmienne warunkowe, itp.

Podsumowując, proces jest instancją działającej aplikacji, podczas gdy wątek jest mniejszą jednostką wykonawczą w ramach procesu, która może wykonywać zadania równolegle z innymi wątkami w tym samym procesie.




    Behave:
        Behave to biblioteka do testowania oparta na języku Python, która wykorzystuje podejście BDD (Behavior-Driven Development).
        Umożliwia tworzenie testów w formie naturalnej, czytelnej dla wszystkich zainteresowanych stron (biznes, deweloperzy, testerzy).
        Testy Behave są definiowane w formie scenariuszy, z krokami opartymi na języku Gherkin, który jest czytelny dla osób niebędących programistami.

    Selenium:
        Selenium to zestaw narzędzi do automatyzacji testów dla aplikacji webowych.
        Pozwala na interakcję z przeglądarką internetową w sposób programatyczny, symulując zachowanie użytkownika.
        Jest obsługiwane w wielu językach programowania, ale najczęściej używane jest w połączeniu z językiem Python.

    Pytest:
        Pytest to framework do testowania w języku Python, który oferuje prostą składnię i bogatą funkcjonalność.
        Umożliwia łatwe pisanie testów, zarządzanie nimi i generowanie raportów.
        Pytest automatycznie znajduje i wykonuje testy w oparciu o zdefiniowane kryteria.

    Allure:
        Allure to otwarty framework do generowania raportów z testów.
        Zapewnia przejrzyste, interaktywne i estetyczne raporty z wynikami testów.
        Może być używany z różnymi narzędziami do testowania, w tym z pytest, Behave, Selenium i innymi.


Locust to narzędzie do testowania wydajności aplikacji internetowych, które umożliwia symulowanie dużego obciążenia na serwerze poprzez generowanie wielu równoległych użytkowników (wątków). Oto kilka kluczowych cech i funkcji narzędzia Locust:

    Python-based: Locust jest napisany w języku Python, co czyni go łatwym w użyciu dla osób znajomych z tym językiem programowania.

    Skalowalność: Narzędzie jest zaprojektowane w taki sposób, aby obsługiwać duże obciążenia, pozwalając na łatwe skalowanie liczby równoległych użytkowników.

    Declarative approach: Locust korzysta z deklaratywnego podejścia do definiowania testów wydajnościowych. Użytkownik definiuje zestaw zadań, które mają zostać wykonane przez symulowanych użytkowników, wraz z logiką, która ma być wykonywana w tych zadaniach.

    Obsługa protokołu HTTP: Locust umożliwia testowanie aplikacji internetowych poprzez protokół HTTP, co czyni go idealnym narzędziem do testowania wydajności API oraz aplikacji webowych.

    Dynamiczna konfiguracja: Użytkownicy mogą dynamicznie konfigurować testy, modyfikując scenariusze testowe, obciążenie lub inne parametry w trakcie działania testu.

    Interaktywny interfejs użytkownika: Locust oferuje interaktywny interfejs webowy, który umożliwia monitorowanie postępu testów, analizę wyników oraz śledzenie metryk wydajnościowych w czasie rzeczywistym.

    Raporty i wyniki: Po zakończeniu testu Locust generuje raporty zawierające szczegółowe informacje na temat wyników testów, takie jak średni czas odpowiedzi, liczba żądań na sekundę, czas odpowiedzi procentylny itp.

Dzięki tym funkcjom Locust jest używany przez zespoły deweloperskie i QA do przeprowadzania testów obciążeniowych i testów wydajnościowych, pomagając w identyfikacji i eliminacji ewentualnych wąskich gardeł w aplikacjach internetowych przed wdrożeniem na produkcję.


"""