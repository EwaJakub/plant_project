from .models import UserProfile
import pytest

from django.test import Client
from django.contrib.auth.models import User, Permission

@pytest.fixture
def user_profiles():
    admin = User.objects.create_superuser('admin', password='Alamakota1!')
    user_1 = User.objects.create_user('user_1', password='Alamakota1!')
    user_2 = User.objects.create_user('user_2', password='Alamakota1!')
    user_3 = User.objects.create_user('user_3', password='Alamakota1!')
    return (
        UserProfile.objects.create(user=user_1, phone="567654478", picture='images/image1.jpg'),
        UserProfile.objects.create(user=user_2, phone="345432348", picture='images/image2.jpg'),
        UserProfile.objects.create(user=user_3, phone="567432356", picture='images/image3.jpg')
    )

@pytest.fixture
def anonymous_client():
    c = Client()
    return c

@pytest.fixture
def logged_clients():
    # creating user
    user_1 = User.objects.create_user('user_1', password='Alamakota1!')

    # creating customer
    client_user_1 = Client()

    # user login
    client_user_1.force_login(user_1)

    return client_user_1 #client_user_2, client_user_3

@pytest.fixture
def logged_clients_with_profile():
    # downloading permissions
    change_userprofile = Permission.objects.get(codename='change_userprofile')
    view_userprofile = Permission.objects.get(codename='view_userprofile')

    # creating users
    user_2 = User.objects.create_user('user_2', password='Alamakota1!')

    # adding perissions
    user_2.user_permissions.add(change_userprofile)
    user_2.user_permissions.add(view_userprofile)
    user_2.save()

    UserProfile.objects.create(user=user_2, phone="345432348", picture='images/image2.jpg')
    # creating a clients for users
    client_user_2 = Client()

    # login users
    client_user_2.force_login(user_2)

    return client_user_2
