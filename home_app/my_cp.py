from plant_app.models import Category, Plant, ANIMAL_INFLUENCE, AIR_PURIFYING, WindowSide, HomeRoom, RoomPart


ROOM_DESCRIPTION = (
    (1, 'Jeśli do tej pory nawet nie myślałeś ustawieniu roślin na kuchennym blacie z obawy o niekorzystne warunki tam panujące, mamy dla ciebie dobre wieści. Istnieje całkiem pokaźna lista roślin, którym bardzo odpowiada gorąca para, podwyższona wilgotność'),
    (2, 'Żywe kwiaty w łazience? Tak, to możliwe. Wbrew pozorom rośliny dobrze się czują w łazience, szczególnie te pochodzące z ciepłych i wilgotnych regionów. Wilgotny, ciepły i często zaciemniony klimat panujący w łazience to idealne warunki wzrostu dla wielu roślin doniczkowych. Czasem nawet zdecydowanie lepsze niż te panujące w pokojach, gdzie zbyt dużo światła i suche powietrze nie są korzystne dla wielu gatunków.'),
    (3, 'Pokój dzienny to na ogół miejsce tętniące życiem. Rośliny powinny więc być jak najbardziej zróżnicowane, ciekawe i kolorowe. Pokój dzienny, a także nasze sypialnie są jednak z reguły pomieszczeniami nieco bardziej suchymi niz pozostałe części naszego mieszkania. Jakie rośliny pasują do nich najlepiej?'),
)

WINDOWSIDE_DESCRIPTION = (
    (1, 'Parapety okien wychodzących na wschód, podobnie jak tych zachodnich, zaledwie przez kilka godzin w ciągu dnia są w pełni nasłonecznione, przez resztę dnia oferując światło rozproszone. Sprawdzą się tu odmiany, które nie wymagają długotrwałego naświetlania do prawidłowego wzrostu.'),
    (2, 'Okno kwiatowe od zachodniej strony, podobnie jak wschodnie, nasłonecznione jest przez mniejszą część dnia. W tym przypadku promienie słoneczne padają bezpośrednio na rośliny po południu i wczesnym wieczorem. Czas ekspozycji na światło słoneczne jest więc podobny, przy czym okno zachodnie jest zdecydowanie cieplejsze niż wschodnie. Wiosną i latem promienie są dodatkowo dosyć silne, przez co mogą sparzyć liście delikatnych odmian. Które rośliny doniczkowe wybrać zatem na okno zachodnie? Którym niestraszne jest chwilowe zacienienie? Na parapecie zachodnim dobrze czuć się będą rośliny preferujące półcień lub lekkie nasłonecznienie.'),
    (3, 'Parapet okna skierowanego na północ to miejsce, w którym najtrudniej uprawiać rośliny domowe. Dlaczego? Przez większość dnia stojące na nim kwiaty nie mają bezpośredniego kontaktu z promieniami słonecznymi, otrzymując jedynie rozproszone, bardzo delikatne światło. Warunki takie są nieodpowiednie dla odmian o kolorowych liściach, które do rozwoju potrzebują większej ilości chlorofilu produkowanego w wyniku fotosyntezy. Nie sprawdzi się tu również większość doniczkowych roślin kwitnące, które zawiązują pączki kwiatowe wyłącznie przy dobrym nasłonecznieniu. Jakie więc rośliny uprawiać przy zachodnim oknie? Zasada jest prosta – sprawdzą się tu przede wszystkim odporne odmiany o ciemnozielonych liściach.'),
    (4, 'Okna południowe są najbardziej nasłonecznione, a przez to niemal równie wymagające przy uprawie roślin jak zacienione okna północne. Dlaczego? Większość roślin domowych nie akceptuje bezpośredniego silnego nasłonecznienia, które oferuje okno z wystawą południową. Efektem postawienia na parapecie południowym zbyt delikatnej rośliny może być jej zwiędnięcie z przesuszenia lub sparzenie liści. Warunki panujące na parapecie okna południowego można porównać do klimatu pustynnego, gdzie jest sucho i bardzo słonecznie. Jakie zatem kwiaty doniczkowe wybrać na południowe okno?')
)


ROOMPART_DESCRIPTION = (
    (1, 'Zacieniony kąt to warunki nieodpowiednie dla odmian o kolorowych liściach, które do rozwoju potrzebują większej ilości chlorofilu produkowanego w wyniku fotosyntezy. MNie kążda roślina znosi więc silne promieniowanie'),
    (2, 'Ustawiając kwiaty doniczkowe na parapecie okiennym trzeba uwzględnić to, że podczas wietrzenia – zwłaszcza zimą – chłodne powietrze może zagrażać roślinom, natomiast latem trzeba uważać, aby silnie operujące w dzień promienie słoneczne nie spowodowały poparzeń liści.'),
)

ANIMAL_INFLUENCE_DESCRIPTION = (
    (1, 'Nie masz zwierząt? Negatywny wpływ roślin nie stanowi dla Ciebie problemu? Wybierz roślinę która zauroczy cię pięknym wyglądem, bez konieczności zwracania uwagi na inne czynniki.'),
    (2, 'Boisz się, że rośliny będą szkodliwe dla Twojego ukochanego zwierzaka. Wybierz rośliny doniczkowe bezpieczne dla kota i psa. Nie zawierają one trujących związków więc nawet jak Twój pupil potraktuje je jako przekąskę, nadal będzie czuł się dobrze i zachowa zdrowie. Stwórz miejską dżunglę bez obawy o ich zdrowie zwierząt.')
)

AIRPURIFYING_DESCRIPTION = (
    (1, 'Rośliny oczyszczające powietrze to niesłabnący trend ostatnich lat. Przełomowe w tym kierunku okazały się być badania instytutu NASA, które zwieńczono raportem przedstawiającym ranking roślin najlepiej oczyszczających powietrze. Agencja kosmiczna nie bez powodu zainteresowała się tym tematem. Szukano bowiem sposobu na łatwe, skuteczne i nie wymagające energii elektrycznej oczyszczanie powietrza w promach i na stacjach kosmicznych. Finalnie rośliny ze względu na swoje specyficzne wymagania nie zagościły w kosmosie. Jednak wyniki przeprowadzonych badań wiralowo rozeszły się po świecie skłaniając coraz to większe rzesze ludzi do zainteresowania się tematem i kupna roślin oczyszczających powietrze.'),
    (2, 'Nie zależy Ci na właściwościach oczyszających powietrze przez rośliny? Spokojnie możesz przejżeć wszystkie poniższe pozycje.')
)

# Global access to objects and descriptions in html files
def global_vars(request):
    return {
        'categories': Category.objects.all(),
        'homeroom': HomeRoom.objects.all(),
        'windowside': WindowSide.objects.all(),
        'roompart': RoomPart.objects.all(),
        'influence': ANIMAL_INFLUENCE,
        'purifying': AIR_PURIFYING,
        'plants': Plant.objects.all(),
        'room_description': ROOM_DESCRIPTION,
        'windowside_description': WINDOWSIDE_DESCRIPTION,
        'roompart_description': ROOM_DESCRIPTION,
        'animalinfluence_description': AIRPURIFYING_DESCRIPTION,
        'airpurifying_description': AIRPURIFYING_DESCRIPTION
    }
