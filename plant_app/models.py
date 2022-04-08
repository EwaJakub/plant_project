from django.db import models
from django.utils.text import slugify
from scrapy_djangoitem import DjangoItem


WORLD_DIRECTIONS = (
    (1, 'okno w kierunku wschodnim'),
    (2, 'okno w kierunku zachodnim'),
    (3, 'okno w kierunku północnym'),
    (4, 'okno w kierunku południowym')
)

HOME_ROOM = (
    (1, 'kuchnia'),
    (2, 'łazienka'),
    (3, 'pokój dzienny/ sypialnia'),
)

ROOM_PART = (
    (1, 'zacieniony kąt'),
    (2, 'słoneczny parapet'),
)

ANIMAL_INFLUENCE = (
    (1, 'szkodliwa dla zwierząt'),
    (2, 'przyjazna dla zwierząt'),
)

AIR_PURIFYING = (
    (1, 'oczyszczające powietrze'),
    (2, 'brak wpływu na oczyszczanie powietrza'),
)

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
    (1, 'Zacieniony kąt to warunki nieodpowiednie dla odmian o kolorowych liściach, które do rozwoju potrzebują większej ilości chlorofilu produkowanego w wyniku fotosyntezy. Nie każda roślina znosi więc silne promieniowanie.'),
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


# Class Model for creating Category objects table
class Category(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")  # dwa opcjonalne argument - height_field i width_field
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    # function that return slug on basis of self.name of creating object
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# Class Model for creating Plant objects talbe
class Plant(models.Model):
    name = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    description = models.TextField()
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    watering_description = models.TextField()
    solar_description = models.TextField()
    influence = models.IntegerField(choices=ANIMAL_INFLUENCE, default=1, null=True)
    purifying = models.IntegerField(choices=AIR_PURIFYING, default=1, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    search_key = models.CharField(max_length=25, blank=True)


    def __str__(self):
        return self.name

    # function that return slug on basis of self.name of creating object
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# Class Model for creating WindowSide objects table
class WindowSide(models.Model):
    direction = models.IntegerField(choices=WORLD_DIRECTIONS)
    plants = models.ManyToManyField(Plant, related_name='window_sides')
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = models.IntegerField(choices=WINDOWSIDE_DESCRIPTION, null=True)

    def __str__(self):
        return self.get_direction_display()

    # function that return slug on basis of self.name of creating object
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.get_direction_display())
        super().save(*args, **kwargs)


# Class Model for creating HomeRoom objects table
class HomeRoom(models.Model):
    room = models.IntegerField(choices=HOME_ROOM)
    plants = models.ManyToManyField(Plant, related_name='home_room')
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = models.IntegerField(choices=ROOM_DESCRIPTION, null=True)

    def __str__(self):
        return self.get_room_display()

    # function that return slug on basis of self.name of creating object
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.get_room_display())
        super().save(*args, **kwargs)


# Class Model for creating RoomPart objects table
class RoomPart(models.Model):
    roompart = models.IntegerField(choices=ROOM_PART)
    plants = models.ManyToManyField(Plant, related_name='room_part')
    slug = models.SlugField(max_length=50, blank=True, null=True)
    description = models.IntegerField(choices=ROOMPART_DESCRIPTION, null=True)

    def __str__(self):
        return self.get_roompart_display()

    # function that return slug on basis of self.name of creating object
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.get_roompart_display())
        super().save(*args, **kwargs)


#Class Model for creating ScrapyJungleBoogie objects table
class ScrapyJungleBoogie(models.Model):
    name = models.CharField(max_length=225)
    link = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    picture = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
#
#     # import base64
#     # base64_message = 'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1NzYiIGhlaWdodD0iNzY4IiB2aWV3Qm94PSIwIDAgNTc2IDc2OCI+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0iI2ZmZmZmZiIvPjwvc3ZnPg=='
#     # base64_bytes = base64_message.encode('ascii')
#     # message_bytes = base64.b64decode(base64_bytes)
#     # message = message_bytes.decode('ascii')
#     # print(message)
#
    class Meta:
        verbose_name = 'Scrapped jungleboogie plants'

#ScrapyJungleBoogie DjangoItem model
class ScrapyJungleBoogieItem(DjangoItem):
    django_model = ScrapyJungleBoogie


# Class Model for creating ScrapyZielonyParapet objects table
class ScrapyZielonyParapet(models.Model):
    name = models.CharField(max_length=225)
    link = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    picture = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Scrapped zielonyparapet plants'

# ScrapyZielonyParapet DjangoItem model
class ScrapyZielonyParapetItem(DjangoItem):
    django_model = ScrapyZielonyParapet


# Class Model for creating ScrapyFloraPoint objects table
class ScrapyFloraPoint(models.Model):
    name = models.CharField(max_length=225)
    link = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    picture = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Scrapped florapoint plants'

# ScrapyFloraPoint DjangoItem model
class ScrapyFloraPointItem(DjangoItem):
    django_model = ScrapyFloraPoint


# Class Model for creating ScrapyCocaflora objects table
class ScrapyCocaflora(models.Model):
    name = models.CharField(max_length=225)
    link = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    picture = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Scrapped cocaflora plants'


# ScrapyCocaflora DjangoItem model
class ScrapyCocafloraItem(DjangoItem):
    django_model = ScrapyCocaflora