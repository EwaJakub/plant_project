

# ScrumLab

## Czym jest ScrumLab?

ScrumLab to projekt, którego celem jest nauczenie Cię pracy w zespole programistów.  Symuluje on realne zadania
w projekcie aplikacji webowej. Podczas tego tygodnia będziesz uczestniczyć w codziennych spotkaniach, rozwiązywać
problemy, robić *code review* i integrować swój kod z kodem kolegów.

ScrumLab będzie prowadzony inaczej niż pozostałe zajęcia w CodersLab. Udział wykładowcy powinien być tu jak najmniejszy, idealnie byłoby, gdyby zjawiał się tylko aby sprawdzić postępy - na tych zajęciach szlifujemy umiejętności dzielenia się wiedzą między uczestnikami i jednoczesną pracę nad wspólnym kodem.
Dodatkowo praca z repozytorium ma przypominać prawdziwy projekt — dlatego będzie się różnić od tego, jak wyglądała praca na ćwiczeniach. 


## Ustawienie wirtualnego środowiska

1. Przygotuj wirtualne środowisko, wpisując `virtualenv <nazwa folderu np. venv>` (folder nie musi być wcześniej stworzony)
2. Aktywuj środowisko `. <nazwa folderu>/bin/activate` albo `source <nazwa folderu>/bin/activate`
3. Następnie używając `pip install -r requirements.txt` zainstaluj wymagane biblioteki i framework
4. Pozostało już tylko zobaczyć czy IDE ustawiło poprawne środowisko. Jak nie to trzeba to zrobić ręcznie (w PyCharmie Interpreter Settings)
5. Możesz też wyrazić zgodę, aby to PyCharm zainstalował wymagane biblioteki i framework (o ile wyskoczy ci odpowiednie okno przy uruchomieniu)

## Ustawienie bazy danych

Przez to, że .gitignore pomija local_settings.py.example, trzeba sobie ręcznie u siebie usunąć ".example" z rozszerzenia pliku "local_settings.py.example"

## Opis projektu

Pani Maria Iksińska napisała książkę kucharską, która stała się bestsellerem na rynku książek kucharskich w Polsce i zwróciła się do nas z prośba o przygotowanie dla jej czytelników aplikacji do planowania posiłków. Książka Pani Iksińskiej promuje zdrowe odżywianie i podkreśla jak ważną rolę odgrywa w nim planowanie posiłków. Chce zacząć przeprowadzać w całym kraju warsztaty, na których będzie uczyć uczestników planowania posiłków.

Pani Maria chce rozwijać swój biznes, a do zrealizowania swoich celów potrzebuje strony-wizytówki oraz prostej aplikacji do planowania posiłków.

## Plan tego repozytorium
* `scrumlab` – katalog z projektem Django. Znajdują się w nim pliki
  - `settings.py` – ustawienia projektu,
  - `urls.py` – dane URL-i,
  - `local_settings.py.example` – ustawienia lokalne; po szczegóły zajrzyj do rozdziału **Konfiguracja projektu**,
* `jedzonko` – katalog aplikacji Django, nad którą będziesz pracował.
* `static` – katalog z plikami statycznymi; po szczegóły zajrzyj do rozdziału **Konfiguracja projektu**

## Konfiguracja projektu

### Co skonfigurowaliśmy za Ciebie?
- szablony
  - umieszczaj je w aplikacji **jedzonko** w katalogu **templates**,
- pliki statyczne
  - pliki statyczne (czyli wszystkie pliki, które są serwowane przez aplikację: obrazki, pliki CSS, JS itp.)
  umieszczaj w katalogu **static**, który znajduje się w głównym katalogu projektu.

### Czego nie skonfigurowaliśmy?
- bazy danych (ze względów bezpieczeństwa)

**Pamiętaj:** nie należy trzymać danych wrażliwych pod kontrolą Gita! Takimi danymi wrażliwymi
są m. in. dane do połączenia z bazą danych. Te dane trzymamy w pliku **local_settings.py**,
którego nie znajdziesz w tym repozytorium (plik jest dodany do **.gitignore**)!

Zajrzyj do pliku **settings.py**, znajdziesz w nim następującą sekcję:

```python
try:
    from scrumlab.local_settings import DATABASES
except ModuleNotFoundError:
    print("Brak konfiguracji bazy danych w pliku local_settings.py!")
    print("Uzupełnij dane i spróbuj ponownie!")
    exit(0)
```

Oznacza to, że Django podczas każdego uruchomienia będzie próbowało zaimportować
stałą `DATABASES` z pliku **local_settings.py**. Tam trzymaj dane do połączenia.
Nie umieszczaj tego pliku pod kontrolą Gita. Aby ułatwić Ci pracę, przygotowaliśmy
plik **local_settings.py.example**, w którym znajdziesz przygotowane odpowiednie dane.
Wystarczy tylko, że zmienisz plikowi **local_settings.py.example** nazwę na  **local_settings.py**
i uzupełnisz go.

---

Jeśli wszystko skonfigurowałeś poprawnie, to pod adresem http://localhost:8000/index zobaczysz przykładową stronę.


import mimetypes

mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)




django-base64 field


Base64field !!!!1

'testserver' 

ALLOWED_HOSTS = ['testserver'] w settingsach

