from django.views import View
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

from home_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin
)
from django.contrib import messages

import operator
from django.db.models import Q
from functools import reduce

from .models import Plant, Category, WindowSide, HomeRoom, RoomPart, ANIMAL_INFLUENCE, AIR_PURIFYING, ANIMAL_INFLUENCE_DESCRIPTION, AIRPURIFYING_DESCRIPTION, ScrapyJungleBoogie, ScrapyZielonyParapet, ScrapyCocaflora, ScrapyFloraPoint
from .form import FilterPlantForm

from bs4 import BeautifulSoup


# BeautufulSoup way of scrapping

# URL = 'https://www.jungleboogie.pl/tag-produktu/monstera/'

# page = get(URL)
# bs = BeautifulSoup(page.content, 'html.parser')

# def parse_price(price):
#     return float(price.replace(',', '.').replace(' ', ''))
#
# def check_price(request):
#     message = []
#     for offer in bs.find_all('div', class_='woocommerce-card__header'):
#         img = offer.previousSibling('img', class_='attachment-woocommerce_thumbnail size-woocommerce_thumbnail')
#         footer = offer.find('div', class_='woocommerce-loop-product__title')
#         name = footer.find('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
#         footer_2 = offer.find('span', class_='price')
#         price = parse_price((footer_2.find('span', class_='woocommerce-Price-amount amount').get_text())[0:-3])    #ucina /xa0zL
#         link = name['href']  # nasza nazwa rośliny będzie odnośnikiek linku, lub gdy mamy name.get_text() dodajemy oddzielnie link np po kliknięciu przycisku idz do sklepu
#         message.append(f'Nazwa rośliny: {name}'
#                        f'Link: {link}'
#                        f'Cena: {price}'
#                        f'Zdjęcie: {img}')
#     return HttpResponse(f'<a> {message} </a>')



# Plant View which extracts data from Plant models in connection to passed context and adding plant to my plants and whishlist
class PlantView(View):
    template_name = 'plant_app/plant-description.html'   # {category}/plant-description/{plant.pk}

    def get(self, request, plant, category):
        plant = Plant.objects.get(slug=plant)
        window_side = WindowSide.objects.filter(plants=plant.pk)
        home_room = HomeRoom.objects.filter(plants=plant.pk)
        room_part = RoomPart.objects.filter(plants=plant.pk)
        context = {'plant': plant,
                   'window_side': window_side,
                   'homeroom': home_room,
                   'roompart': room_part,
                   }
        return render(request, self.template_name, context)


    def post(self, request, plant, category):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        plant = Plant.objects.get(slug=plant)
        window_side = WindowSide.objects.filter(plants=plant.pk)
        home_room = HomeRoom.objects.filter(plants=plant.pk)
        room_part = RoomPart.objects.filter(plants=plant.pk)
        try:
            userprofile = UserProfile.objects.get(user=user.pk)  # if User have UserProfile plants can be added to User private lists
            if request.POST.get('wishlist'):
                userprofile.wishlist.add(plant)
                return redirect('my-wishlist')
            elif request.POST.get('my-plants'):
                user.userprofile.plants.add(plant)
                return redirect('my-plants')
            else:
                context = {'plant': plant,
                           'window_side': window_side,
                           'homeroom': home_room,
                           'roompart': room_part,
                           }
                return render(request, self.template_name, context)

        except UserProfile.DoesNotExist:  # if User don't have profile view redirects to create my profile website
            messages.error(request, "Żeby dodać roślinę musisz uzupełnić profil!")
            return redirect('create-my-profile')



# Class View which shows categories data
class CategoryView(View):
    template_name = 'plant_app/all_categories.html'

    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, self.template_name, context)


# View for adding new plants -> easier way by django.admin
# class PlantAddView(CreateView):
#     model = Plant
#     fields = ['name', 'category', 'description', 'picture', 'watering_description', 'solar_description', 'influence', 'purifying']
#     success_url = '/'


# Class View for viewing all plants in a list
class PlantListView(View):
    template_name = 'plant_app/all_plants.html'

    def get(self, request):
        return render(request, self.template_name)


# Class for search bar, shows results of plants that contains requested searched value
class SearchResultView(View):

    def get(self, request):
        return render(request, 'base.html')

    def post(self, request):
        try:
            searched_value = request.POST.get('searched')
            if searched_value and len(searched_value) == 0:
                return redirect('home-view')
            elif searched_value:
                searched_plants = Plant.objects.filter(name__contains=searched_value)
                return render(request, 'plant_app/search_result.html', {'searched_plants': searched_plants, 'searched_value': searched_value})
            else:
                return render(request, 'plant_app/search_result.html')
        except ObjectDoesNotExist:
            return render(request, 'plant_app/search_result.html')  # {% empty %} returns no searched data


# Class View for filtering all data on basis of plant_app models, contains all requested search values
class FilterPlantView(View):

    def get(self, request):
        form = FilterPlantForm()
        return render(request, 'plant_app/plant_filter.html', {'form': form})

    def post(self, request):
        form = FilterPlantForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            window_direction = form.cleaned_data['window_direction']
            home_room = form.cleaned_data['home_room']
            room_part = form.cleaned_data['room_part']
            animal_influence = form.cleaned_data['animal_influence']
            air_purifying = form.cleaned_data['air_purifying']

            category_filter = Category.objects.filter(name__in=category)  #1
            category_pk_list = []
            for category in category_filter:
                category_pk_list.append(category.pk)
            plants_by_category = Plant.objects.filter(category__in=category_pk_list)


            window_direction_filter = WindowSide.objects.filter(direction__in=window_direction) #2
            window_pk_list = []
            for direction in window_direction_filter:
                plants = direction.plants.all()
                for plant in plants:
                    window_pk_list.append(plant.pk)
            plants_by_windowside = Plant.objects.filter(pk__in=window_pk_list)

            homeroom_filter = HomeRoom.objects.filter(room__in=home_room)
            homeroom_pk_list = []
            for room in homeroom_filter:
                plants = room.plants.all()
                for plant in plants:
                    homeroom_pk_list.append(plant.pk)
            plants_by_homeroom = Plant.objects.filter(pk__in=homeroom_pk_list)

            roompart_filter = RoomPart.objects.filter(roompart__in=room_part)
            roompart_pk_list = []
            for part in roompart_filter:
                plants = part.plants.all()
                for plant in plants:
                    roompart_pk_list.append(plant.pk)
            plants_by_roompart = Plant.objects.filter(pk__in=roompart_pk_list)

            plants_by_animalinfluence = Plant.objects.filter(influence__in=animal_influence)

            plants_by_airpurifying = Plant.objects.filter(purifying__in=air_purifying)

            all_plants = plants_by_category | plants_by_windowside | plants_by_homeroom | plants_by_roompart | plants_by_animalinfluence | plants_by_airpurifying

            list = []
            for plant in all_plants:
                list.append(plant.name)

        return render(request, 'plant_app/plant_filter_result.html', {'all_plants': all_plants})


# Class Model view which shows all plants for the requested category
class ChosenCategoryView(View):

    def get(self, request, slug):
        choosen_category = Category.objects.get(slug=slug)
        chosen_plants = Plant.objects.filter(category=choosen_category)
        ctx = {
            'choosen_category': choosen_category,
            'choosen_plants': chosen_plants,
        }
        return render(request, 'plant_app/category.html', ctx)


# Class Model view which shows all plants for the requested roompart
class ChosenRoompartView(View):

    def get(self, request, slug):
        choosen_roompart = RoomPart.objects.get(slug=slug)
        chosen_plants = choosen_roompart.plants.all()
        ctx = {
            'choosen_plants': chosen_plants,
            'choosen_roompart': choosen_roompart,
        }
        return render(request, 'plant_app/room_part.html', ctx)


# Class Model view which shows all plants for the requested homeroom
class ChosenHomeroomView(View):

    def get(self, request, slug):
        choosen_homeroom = HomeRoom.objects.get(slug=slug)
        chosen_plants = choosen_homeroom.plants.all()
        ctx = {
            'choosen_plants': chosen_plants,
            'choosen_homeroom': choosen_homeroom,
        }
        return render(request, 'plant_app/home_room.html', ctx)


# Class Model view which shows all plants for the requested windowside
class ChosenWindowsideView(View):

        def get(self, request, slug):
            choosen_windowside = WindowSide.objects.get(slug=slug)
            chosen_plants = choosen_windowside.plants.all()
            ctx = {
                'choosen_plants': chosen_plants,
                'choosen_windowside': choosen_windowside,
            }
            return render(request, 'plant_app/window_side.html', ctx)


# Class Model view which shows all plants for the requested plant influence
class ChosenInfluenceView(View):

    def get(self, request, data):
        if data == slugify(ANIMAL_INFLUENCE[1][1]):  # searched value n the basis of slugify field
            plants = Plant.objects.filter(influence=slugify(ANIMAL_INFLUENCE[0][0]))
            influence = ANIMAL_INFLUENCE[1][1]
            description = ANIMAL_INFLUENCE_DESCRIPTION[1][1]
        elif data == slugify(AIR_PURIFYING[0][1]):
            plants = Plant.objects.filter(purifying=slugify(AIR_PURIFYING[0][0]))
            influence = AIR_PURIFYING[0][1]
            description = AIRPURIFYING_DESCRIPTION[0][1]
        chosen_plants = plants
        chosen_influence = influence
        chosen_description = description
        ctx = {
            'choosen_plants': chosen_plants,
            'chosen_influence': chosen_influence,
            'chosen_description': chosen_description
        }
        return render(request, 'plant_app/plant_influence.html', ctx)


# Adds Plant object to Userprofile, creates a wishlist of plants
class AddToWishlistView(LoginRequiredMixin, View):  # loginrequired ? permission required?

    template_name = "plant_app/my_wishlist.html"
    permission_required = "home_app.change_userprofile"

    def get(self, request):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        try:
            if user.userprofile.id:   # checking if user have Userprofile connected with account
                ctx = {
                    'wishlist': user.userprofile.wishlist.all(), # show list of plants in whishlist
                }
                return render(request, self.template_name, ctx)
        except UserProfile.DoesNotExist:  # if user don't have created userprofile
            messages.error(request, "Żeby dodać roślinę do wishlisty musisz uzupełnić profil!")
            return redirect('create-my-profile')


# Adds Plant object to Userprofile, creates a my plants list of plants
class AddToMyplantsView(LoginRequiredMixin, View):  # loginrequired ? permission required?

    template_name = "plant_app/my_plants.html"
    permission_required = "home_app.change_userprofile"

    def get(self, request):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        try:
            if user.userprofile.id:  # checking if user have Userprofile connected with account
                ctx = {
                    'my_plants': user.userprofile.plants.all()  # show list of plants in whishlist
                }
            return render(request, self.template_name, ctx)
        except UserProfile.DoesNotExist:  # if user don't have created userprofile
            messages.error(request, "Żeby dodać roślinę musisz uzupełnić profil!")
            return redirect('create-my-profile')


# Deletes Plant objects from Userprofile whishlist
class DeletePlantWishlistView(PermissionRequiredMixin, LoginRequiredMixin, View):  # page is forbidden withouth permission

    template_name = "plant_app/delete_plant_wishlist.html"
    permission_required = "home_app.change_userprofile"

    def get(self, request, slug):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        try:
            if user.userprofile.id:   # checking if user have Userprofile connected with account
                ctx = {
                    'plant': user.userprofile.wishlist.filter(slug=slug).first()
                }
                return render(request, self.template_name, ctx)
        except UserProfile.DoesNotExist:  # if user don't have created userprofile
            messages.error(request, "Żeby usunąć roślinę z wishlisty musisz uzupełnić profil!")
            return redirect('create-my-profile')

    def post(self, request, slug):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        try:
            if user.userprofile.id:  # checking if user have Userprofile connected with account
                if request.POST.get('delete') == 'Tak':
                    plant = user.userprofile.wishlist.filter(slug=slug).first()
                    user.userprofile.wishlist.remove(plant)  # removing a plant from whishlist
                    return redirect('my-wishlist')
                elif request.POST.get('delete') == 'Nie':
                    return redirect('my-wishlist')
                else:
                    return redirect('my-wishlist')
        except UserProfile.DoesNotExist:
            messages.error(request, "Żeby usunąć roślinę z wishlisty musisz uzupełnić profil!")
            return redirect('create-my-profile')


# Deletes Plant objects from Userprofile my plants
class DeletePlantPlantsView(PermissionRequiredMixin, LoginRequiredMixin, View):

    template_name = "plant_app/delete_plant_plants.html"
    permission_required = ("home_app.change_userprofile")

    def get(self, request, slug):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        try:
            if user.userprofile.id:  # checking if user have Userprofile connected with account
                ctx = {
                    'plant': user.userprofile.plants.filter(slug=slug).first()
                }
                return render(request, self.template_name, ctx)
            else:
                return redirect('my-plants')
        except UserProfile.DoesNotExist:   # if user don't have created userprofile
            messages.error(request, "Żeby dodać roślinę do moich roślin musisz uzupełnić profil!")
            return redirect('create-my-profile')

    def post(self, request, slug):
        logged_user = request.user.username
        user = User.objects.get(username=logged_user)
        try:
            if user.userprofile.id:  # checking if user have Userprofile connected with account
                if request.POST.get('delete') == 'Tak':
                    plant = user.userprofile.plants.filter(slug=slug).first()
                    user.userprofile.plants.remove(plant)   #  removing a plant from whishlist
                    return redirect('my-plants')
                elif request.POST.get('delete') == 'Nie':
                    return redirect('my-plants')
                else:
                    return redirect('my-plants')
        except UserProfile.DoesNotExist:
            messages.error(request, "Żeby dodać roślinę do moich roślin musisz uzupełnić profil!")
            return redirect('create-my-profile')


# Class View connested with Userprofile wishlist - shows data scrapped from choosen websites, saved in database
class PriceCompareView(PermissionRequiredMixin, LoginRequiredMixin, View):  # can't check prices withouth permission

     template_name = "plant_app/price_compare.html"
     permission_required = "home_app.change_userprofile"

     def get(self, request, slug):
         logged_user = request.user.username
         user = User.objects.get(username=logged_user)
         compared_plant = Plant.objects.filter(slug=slug).first()
         compared_names = compared_plant.search_key.split()
         query = reduce(operator.or_, (Q(name__contains=item) for item in compared_names))  # filter objects on the basis of search_key words list
         jungle_boogie_plants = ScrapyJungleBoogie.objects.filter(query)  # checkes plant's names connected with keywords from websites
         zielony_parapet_plants = ScrapyZielonyParapet.objects.filter(query)
         flora_point_plants = ScrapyFloraPoint.objects.filter(query)
         cocaflora_plants = ScrapyCocaflora.objects.filter(query)
         try:
             if user.userprofile.id:
                 ctx = {
                     'compared_plant': compared_plant,
                     'jungle_boogie_plants': jungle_boogie_plants,
                     'zielony_parapet_plants': zielony_parapet_plants,
                     'flora_point_plants': flora_point_plants,
                     'cocaflora_plants': cocaflora_plants,
                     'zielonyparapet': ScrapyZielonyParapet.objects.all(),
                     'florapoint': ScrapyFloraPoint.objects.all(),
                     'cocaflora': ScrapyCocaflora.objects.all(),
                 }
                 return render(request, self.template_name, ctx)
         except UserProfile.DoesNotExist:
             messages.error(request, "Żeby dodać roślinę do wishlisty musisz uzupełnić profil!")
             return redirect('create-my-profile')



# Plantscraper - CrawlerProcess to csv
# class PlantSpider(scrapy.Spider):
#     name = 'plant'
#     start_urls = ['https://www.jungleboogie.pl/kategoria-produktu/rosliny/']
#
#     def start_requests(self):
#         yield scrapy.Request('https://www.jungleboogie.pl/kategoria-produktu/rosliny/')
#
#     def parse(self, response):
#         for plant in response.css('li.wcpa_has_options, product, type-product'):
#             name = plant.css('a.woocommerce-LoopProduct-link, woocommerce-loop-product__link').attrib['aria-label']
#             price = plant.css('span.woocommerce-Price-amount bdi::text').get()  #float(price[0:-3].replace(',','.'))
#             picture = plant.css('img.attachment-woocommerce_thumbnail, size-woocemmerce_thumbnail').attrib['src']
#             yield {
#                 'name': name,
#                 'price': price,
#                 'picture': picture
#             }
#
#
#         next_page = response.css('a.next, page-numbers').attrib['href']
#         if next_page is not None:
#             yield response.follow(next_page, callback=self.parse)  # parse wraca do fukncji i przechodzi ja od nowa


# process = CrawlerProcess(settings={
#     'FEED_URI': 'plant.csv',
#     'FEED_FORMAT': 'csv'
#     })
#
#         #plant = response.css('li.product, type-product')
#
# process.crawl(PlantSpider)
# process.start()


