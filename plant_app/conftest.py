from .models import Category, HomeRoom, Plant, RoomPart, ScrapyCocaflora, ScrapyFloraPoint, ScrapyJungleBoogie, ScrapyZielonyParapet, WindowSide
from home_app.models import UserProfile
import pytest

from django.test import Client
from django.contrib.auth.models import User, Permission


@pytest.fixture
def categories():
    return (
        Category.objects.create(name="name_1", description='description 1', picture='images/picture1'),
        Category.objects.create(name="name_2", description='description 2', picture='images/picture2'),
        Category.objects.create(name="name_3", description='description 3', picture='images/picture3')
    )

@pytest.fixture
def plants():
    Category.objects.create(name="name_1", description='description 1', picture='images/picture1'),
    Category.objects.create(name="name_2", description='description 2', picture='images/picture2'),
    Category.objects.create(name="name_3", description='description 3', picture='images/picture3')
    return (
        Plant.objects.create(name="name_1", category=Category.objects.get(pk=1), description='description_1', picture='images/picture_1', watering_description='description_1', solar_description='description_1', search_key='key_1'),
        Plant.objects.create(name="name_2", category=Category.objects.get(pk=2), description='description_2', picture='images/picture_2', watering_description='description_2', solar_description='description_2', search_key='key_2'),
        Plant.objects.create(name="name_3", category=Category.objects.get(pk=1), description='description_3', picture='images/picture_3', watering_description='description_3', solar_description='description_3', search_key='key_3')
    )

@pytest.fixture
def windowsides():
    Category.objects.create(name="name_1", description='description 1', picture='images/picture1')
    Plant.objects.create(name="name_1", category=Category.objects.get(pk=1), description='description_1',
                         picture='images/picture_1', watering_description='description_1',
                         solar_description='description_1', search_key='key_1'),
    Plant.objects.create(name="name_2", category=Category.objects.get(pk=1), description='description_2',
                         picture='images/picture_2', watering_description='description_2',
                         solar_description='description_2', search_key='key_2'),
    object_1 = WindowSide.objects.create(direction=1, description=1)
    object_2 = WindowSide.objects.create(direction=2, description=2)
    object_3 = WindowSide.objects.create(direction=3, description=3)
    object_1.plants.add(Plant.objects.get(pk=1))
    object_2.plants.add(Plant.objects.get(pk=1))
    object_3.plants.add(Plant.objects.get(pk=2))
    return (
        object_1,
        object_2,
        object_3
    )

@pytest.fixture
def homerooms():
    Category.objects.create(name="name_1", description='description 1', picture='images/picture1')
    Plant.objects.create(name="name_1", category=Category.objects.get(pk=1), description='description_1',
                         picture='images/picture_1', watering_description='description_1',
                         solar_description='description_1', search_key='key_1'),
    Plant.objects.create(name="name_2", category=Category.objects.get(pk=1), description='description_2',
                         picture='images/picture_2', watering_description='description_2',
                         solar_description='description_2', search_key='key_2'),
    object_1 = HomeRoom.objects.create(room=1, description=1)
    object_2 = HomeRoom.objects.create(room=2, description=2)
    object_3 = HomeRoom.objects.create(room=3, description=3)
    object_1.plants.add(Plant.objects.get(pk=1))
    object_2.plants.add(Plant.objects.get(pk=1))
    object_3.plants.add(Plant.objects.get(pk=2))
    return (
        object_1,
        object_2,
        object_3
    )

@pytest.fixture
def roomparts():
    Category.objects.create(name="name_1", description='description 1', picture='images/picture1')
    Plant.objects.create(name="name_1", category=Category.objects.get(pk=1), description='description_1',
                         picture='images/picture_1', watering_description='description_1',
                         solar_description='description_1', search_key='key_1'),
    Plant.objects.create(name="name_2", category=Category.objects.get(pk=1), description='description_2',
                         picture='images/picture_2', watering_description='description_2',
                         solar_description='description_2', search_key='key_2'),
    object_1 = RoomPart.objects.create(roompart=1, description=1)
    object_2 = RoomPart.objects.create(roompart=2, description=2)
    object_3 = RoomPart.objects.create(roompart=3, description=3)
    object_1.plants.add(Plant.objects.get(pk=1))
    object_2.plants.add(Plant.objects.get(pk=1))
    object_3.plants.add(Plant.objects.get(pk=2))
    return (
        object_1,
        object_2,
        object_3
    )

@pytest.fixture
def scrapy_jungle_boogie():
    return (
        ScrapyJungleBoogie.objects.create(name='name 1', link='https//:website...', price=10.4),
        ScrapyJungleBoogie.objects.create(name='name 2', link='https//:website...', price=10),
        ScrapyJungleBoogie.objects.create(name='name 3', link='https//:website...', price=12.98)
    )

@pytest.fixture
def scrapy_zielony_parapet():
    return (
        ScrapyZielonyParapet.objects.create(name='name 1', link='https//:website...', price=10.4),
        ScrapyZielonyParapet.objects.create(name='name 2', link='https//:website...', price=10),
        ScrapyZielonyParapet.objects.create(name='name 3', link='https//:website...', price=12.98)
    )

@pytest.fixture
def scrapy_flora_point():
    return (
        ScrapyFloraPoint.objects.create(name='name 1', link='https//:website...', price=10.4),
        ScrapyFloraPoint.objects.create(name='name 2', link='https//:website...', price=10),
        ScrapyFloraPoint.objects.create(name='name 3', link='https//:website...', price=12.98)
    )

@pytest.fixture
def scrapy_cocaflora():
    return (
        ScrapyCocaflora.objects.create(name='name 1', link='https//:website...', price=10.4),
        ScrapyCocaflora.objects.create(name='name 2', link='https//:website...', price=10),
        ScrapyCocaflora.objects.create(name='name 3', link='https//:website...', price=12.98)
    )

@pytest.fixture
def anonymous_client():
    c = Client()
    return c

@pytest.fixture
def logged_clients():
    # Tworzymy użytkowników
    user_1 = User.objects.create_user('user_1', password='Alamakota1!')

    # Tworzymy klentów dla użytkowników
    client_user_1 = Client()

    # Logujemy użytkowników
    client_user_1.force_login(user_1)

    return client_user_1 #client_user_2, client_user_3

@pytest.fixture
def logged_clients_with_profile():
    # Pobieramy uprawnienia
    change_userprofile = Permission.objects.get(codename='change_userprofile')
    view_userprofile = Permission.objects.get(codename='view_userprofile')

    # Tworzymy użytkowników
    user_2 = User.objects.create_user('user_2', password='Alamakota1!')

    # Dodajemy uprawnienia
    user_2.user_permissions.add(change_userprofile)
    user_2.user_permissions.add(view_userprofile)
    user_2.save()

    UserProfile.objects.create(user=user_2, phone="345432348", picture='images/image2.jpg')
    # Tworzymy klentów dla użytkowników
    client_user_2 = Client()

    # Logujemy użytkowników
    client_user_2.force_login(user_2)

    return client_user_2