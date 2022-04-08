

# Plant Project 

## Ustawienie wirtualnego środowiska

1. Przygotuj wirtualne środowisko, wpisując `virtualenv <nazwa folderu np. venv>` (folder nie musi być wcześniej stworzony)
2. Aktywuj środowisko `. <nazwa folderu>/bin/activate` albo `source <nazwa folderu>/bin/activate`
3. Następnie używając `pip install -r requirements.txt` zainstaluj wymagane biblioteki i framework
4. Pozostało już tylko zobaczyć czy IDE ustawiło poprawne środowisko. Jak nie to trzeba to zrobić ręcznie (w PyCharmie Interpreter Settings)
5. Możesz też wyrazić zgodę, aby to PyCharm zainstalował wymagane biblioteki i framework (o ile wyskoczy ci odpowiednie okno przy uruchomieniu)


## Opis projektu

Projekt jest aplikacją służącą do wyszukiwania roślin zgodnie z naszymi preferencjami. W przypadku zalogowanego użytkownika z utworzonym profilem dodatkowo pozwala na dodawanie roślin do my whishlist i my plants. Wishlist posiada dodatkowy widok - porównywarkę cen z 4 wybranych sklepów z roślinami.


## Plan tego repozytorium
* `plant_app` – katalog z projektem Django. Znajdują się w nim pliki związane z działaniem aplikacji
  - `settings.py` – ustawienia projektu,
  - `urls.py` – dane URL-i,
* `home_app` – katalog aplikacji Django, zawierający widoki związane ze stroną gółną i profilem użytkownika
 `static` – katalog z plikami statycznymi; 
 `media` – katalog z plikami statycznymi;
* `plantscraper` – katalog aplikacji scrapy, połączony z projektem Django, korzystający z modeli Django

---

## Migracje
Pamiętaj


## Plan uruchamianie aplikacji scrapy
aby uruchomić scrapy, w terminalu w folderze aplikacji powinniśmy wpisać komendę:
scrapy crawl cocaflora-plantscraper
scrapy crawl florapoint-plantscraper
scrapy crawl zielonyparapet-plantscraper
scrapy crawl jungleboogie-plantscraper


Jeśli wszystko skonfigurowałeś poprawnie, to pod adresem http://localhost:8000/index zobaczysz przykładową stronę.


