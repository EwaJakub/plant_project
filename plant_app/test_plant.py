import pytest
from home_app.models import User
from .models import Category, HomeRoom, Plant, RoomPart, ScrapyCocaflora, ScrapyFloraPoint, ScrapyJungleBoogie, ScrapyZielonyParapet, WindowSide

@pytest.mark.django_db
def test_categories(categories):
  category_1 = Category.objects.filter(name='name_1').first()
  assert len(Category.objects.all()) == 3
  assert category_1.name == 'name_1'


@pytest.mark.django_db
def test_plants(plants, categories):
  plant_1 = Plant.objects.filter(name='name_1').first()
  assert len(Plant.objects.all()) == 3
  assert plant_1.name == 'name_1'


@pytest.mark.django_db
def test_windowsides(windowsides):
  windowside_1 = WindowSide.objects.filter(direction=1).first()
  assert len(WindowSide.objects.all()) == 3
  assert windowside_1.direction == 1


@pytest.mark.django_db
def test_homerooms(homerooms):
  homeroom_1 = HomeRoom.objects.filter(room=1).first()
  assert len(HomeRoom.objects.all()) == 3
  assert homeroom_1.room == 1


@pytest.mark.django_db
def test_roomparts(roomparts):
  roompart_1 = RoomPart.objects.filter(roompart=1).first()
  assert len(RoomPart.objects.all()) == 3
  assert roompart_1.roompart == 1

@pytest.mark.django_db
def test_scrapy_jungle_boogies(scrapy_jungle_boogie):
  scrapy_1 = ScrapyJungleBoogie.objects.filter(name='name 1').first()
  assert len(ScrapyJungleBoogie.objects.all()) == 3
  assert scrapy_1.name == 'name 1'


@pytest.mark.django_db
def test_scrapy_zielony_parapets(scrapy_zielony_parapet):
  scrapy_1 = ScrapyZielonyParapet.objects.filter(name='name 1').first()
  assert len(ScrapyZielonyParapet.objects.all()) == 3
  assert scrapy_1.name == 'name 1'


@pytest.mark.django_db
def test_scrapy_flora_points(scrapy_flora_point):
  scrapy_1 = ScrapyFloraPoint.objects.filter(name='name 1').first()
  assert len(ScrapyFloraPoint.objects.all()) == 3
  assert scrapy_1.name == 'name 1'


@pytest.mark.django_db
def test_scrapy_cocafloras(scrapy_cocaflora):
  scrapy_1 = ScrapyCocaflora.objects.filter(name='name 1').first()
  assert len(ScrapyCocaflora.objects.all()) == 3
  assert scrapy_1.name == 'name 1'


@pytest.mark.django_db
def test_all_categories(anonymous_client, categories, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('/categories/')
  response1 = logged_clients.get('/categories/')
  response2 = logged_clients_with_profile.get('/categories/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert len(response.context['categories']) == 3

@pytest.mark.django_db
def test_all_plants(anonymous_client, plants, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('/plants/')
  response1 = logged_clients.get('/plants/')
  response2 = logged_clients_with_profile.get('/plants/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert len(response.context['plants']) == 3

@pytest.mark.django_db
def test_categories(anonymous_client, categories,  logged_clients, logged_clients_with_profile):
  category = categories[0]
  response = anonymous_client.get('/category/' + category.slug + '/')
  response1 = logged_clients.get('/category/' + category.slug + '/')
  response2 = logged_clients_with_profile.get('/category/' + category.slug + '/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200

@pytest.mark.django_db
def test_delete_plant_plants(anonymous_client, plants, logged_clients, logged_clients_with_profile):
  plant = plants[0]
  response = anonymous_client.get('/my-view-plants/delete-plants/' + plant.slug + '/')
  response1 = logged_clients.get('/my-view-plants/delete-plants/' + plant.slug + '/')
  response2 = logged_clients_with_profile.get('/my-view-plants/delete-plants/' + plant.slug + '/')
  assert response.status_code == 302
  assert response1.status_code == 403  # brak uprawnień
  assert response2.status_code == 200
  response4 = anonymous_client.post('/my-view-plants/delete-plants/' + plant.slug + '/')
  response5 = logged_clients.post('/my-view-plants/delete-plants/' + plant.slug + '/')
  response6 = logged_clients_with_profile.post('/my-view-plants/delete-plants/' + plant.slug + '/')
  assert response4.status_code == 302
  assert response5.status_code == 403
  assert response6.status_code == 302


@pytest.mark.django_db
def test_delete_plant_whishlists(anonymous_client, plants, logged_clients, logged_clients_with_profile):
  plant = plants[0]
  response = anonymous_client.get('/my-view-plants/delete-wishlist/' + plant.slug + '/')
  response1 = logged_clients.get('/my-view-plants/delete-wishlist/' + plant.slug + '/')
  response2 = logged_clients_with_profile.get('/my-view-plants/delete-wishlist/' + plant.slug + '/')
  assert response.status_code == 302
  assert response1.status_code == 403  # brak uprawnień
  assert response2.status_code == 200
  response4 = anonymous_client.post('/my-view-plants/delete-wishlist/' + plant.slug + '/')
  response5 = logged_clients.post('/my-view-plants/delete-wishlist/' + plant.slug + '/')
  response6 = logged_clients_with_profile.post('/my-view-plants/delete-wishlist/' + plant.slug + '/')
  assert response4.status_code == 302
  assert response5.status_code == 403
  assert response6.status_code == 302

@pytest.mark.django_db
def test_window_sides(anonymous_client, windowsides, logged_clients, logged_clients_with_profile):
  windowside = windowsides[0]
  number_windowside = len(WindowSide.objects.all())
  response = anonymous_client.get('/window-side/' + windowside.slug + '/')
  response1 = logged_clients.get('/window-side/' + windowside.slug + '/')
  response2 = logged_clients_with_profile.get('/window-side/' + windowside.slug + '/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert len(WindowSide.objects.all()) == number_windowside
  assert "Kategoria:" in response.content.decode('utf-8'), 'Brak informacji'

@pytest.mark.django_db
def test_my_plants(anonymous_client, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('/my-plants/')
  response1 = logged_clients.get('/my-plants/')
  response2 = logged_clients_with_profile.get('/my-plants/')
  assert response.status_code == 302 # widok dla zalogowanych
  assert response1.status_code == 302  # brak uprawnień
  assert response2.status_code == 200

@pytest.mark.django_db
def test_my_whishlists(anonymous_client, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('/my-wishlist/')
  response1 = logged_clients.get('/my-wishlist/')
  response2 = logged_clients_with_profile.get('/my-wishlist/')
  assert response.status_code == 302 # widok dla zalogowanych
  assert response1.status_code == 302  # brak uprawnień
  assert response2.status_code == 200

@pytest.mark.django_db
def test_plant_description(anonymous_client, plants, logged_clients, logged_clients_with_profile):
  plant = plants[0]
  category = plant.category
  response = anonymous_client.get('/plant-description/' + category.slug + '/' + plant.slug + '/')
  response1 = logged_clients.get('/plant-description/' + category.slug + '/' + plant.slug + '/')
  response2 = logged_clients_with_profile.get('/plant-description/' + category.slug + '/' + plant.slug + '/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert "Opis rośliny" in response.content.decode('utf-8'), 'Brak informacji'
  response5 = logged_clients.post('/plant-description/' + category.slug + '/' + plant.slug + '/')
  response6 = logged_clients_with_profile.post('/plant-description/' + category.slug + '/' + plant.slug + '/')
  assert response5.status_code == 302
  assert response6.status_code == 200


@pytest.mark.django_db
def test_plant_filter(anonymous_client, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('/plant-filter/')
  response1 = logged_clients.get('/plant-filter/')
  response2 = logged_clients_with_profile.get('/plant-filter/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  response4 = anonymous_client.post('/plant-filter/')
  response5 = logged_clients.post('/plant-filter/')
  response6 = logged_clients_with_profile.post('/plant-filter/')
  assert response4.status_code == 200
  assert response5.status_code == 200
  assert response6.status_code == 200
  assert "Wybierz czego szukasz:" in response.content.decode('utf-8'), 'Brak informacji'


@pytest.mark.django_db
def test_plant_influence(anonymous_client, logged_clients, logged_clients_with_profile):
  data = 'przyjazna-dla-zwierzat'
  number_influence = len(Plant.objects.filter(influence=1))
  #data = 'oczyszczajace-powietrze'
  response = anonymous_client.get('/influence/' + data + '/')
  response1 = logged_clients.get('/influence/' + data + '/')
  response2 = logged_clients_with_profile.get('/influence/' + data + '/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert len(Plant.objects.filter(influence=1)) == number_influence
  assert "Kategoria:" in response.content.decode('utf-8'), 'Brak informacji'


@pytest.mark.django_db
def test_price_compare(anonymous_client, plants,  logged_clients, logged_clients_with_profile, scrapy_jungle_boogie, scrapy_cocaflora, scrapy_flora_point, scrapy_zielony_parapet):
  plant = plants[0]
  number_scrapy_jungleboogie = len(ScrapyJungleBoogie.objects.all())
  number_srapy_florapoint = len(ScrapyFloraPoint.objects.all())
  number_scrapy_zielonyparapet = len(ScrapyZielonyParapet.objects.all())
  number_scrapy_cocaflora = len(ScrapyCocaflora.objects.all())
  response = anonymous_client.get('/price-compare/' + plant.slug + '/')
  response1 = logged_clients.get('/price-compare/' + plant.slug + '/')
  response2 = logged_clients_with_profile.get('/price-compare/' + plant.slug + '/')
  assert response.status_code == 302  # widok dostępny tylko dla zalogowanego użytkownika z uprawnieniami
  assert response1.status_code == 403  # zalogowany ale brak uprawnień
  assert response2.status_code == 200  # zalogowany z uprawnieniami
  assert len(ScrapyJungleBoogie.objects.all()) == number_scrapy_jungleboogie
  assert len(ScrapyFloraPoint.objects.all()) == number_srapy_florapoint
  assert len(ScrapyZielonyParapet.objects.all()) == number_scrapy_zielonyparapet
  assert len(ScrapyCocaflora.objects.all()) == number_scrapy_cocaflora


# path('home-room/<slug>/', plant_views.ChosenHomeroomView.as_view(), name='chosen-homeroom'),
@pytest.mark.django_db
def test_room_part(anonymous_client, roomparts, logged_clients, logged_clients_with_profile):
  roompart = roomparts[0]
  roompart_number = len(RoomPart.objects.all())
  response = anonymous_client.get('/room-part/' + roompart.slug + '/')
  response1 = logged_clients.get('/room-part/' + roompart.slug + '/')
  response2 = logged_clients_with_profile.get('/room-part/' + roompart.slug + '/')
  assert len(RoomPart.objects.all()) == roompart_number
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert "Kategoria:" in response.content.decode('utf-8'), 'Brak informacji'

@pytest.mark.django_db
def test_search_result(anonymous_client, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('/search-result/')
  response1 = logged_clients.get('/search-result/')
  response2 = logged_clients_with_profile.get('/search-result/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  response4 = anonymous_client.post('/search-result/')
  response5 = logged_clients.post('/search-result/')
  response6 = logged_clients_with_profile.post('/search-result/')
  assert response4.status_code == 200
  assert response5.status_code == 200
  assert response6.status_code == 200

@pytest.mark.django_db
def test_home_rooms(anonymous_client, homerooms, logged_clients, logged_clients_with_profile):
  homeroom_number = len(HomeRoom.objects.all())
  homeroom = homerooms[0]
  response = anonymous_client.get('/home-room/' + homeroom.slug + '/')
  response1 = logged_clients.get('/home-room/' + homeroom.slug + '/')
  response2 = logged_clients_with_profile.get('/home-room/' + homeroom.slug + '/')
  assert len(HomeRoom.objects.all()) == homeroom_number
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert "Kategoria:" in response.content.decode('utf-8'), 'Brak informacji'