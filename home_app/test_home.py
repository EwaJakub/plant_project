import pytest

from .models import UserProfile

@pytest.mark.django_db
def test_user_profiles(user_profiles):
  profile_1 = UserProfile.objects.filter(phone="345432348").first()
  assert len(UserProfile.objects.all()) == 3
  assert profile_1.phone == "345432348"

@pytest.mark.django_db
def test_homepage(anonymous_client, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('')
  response1 = logged_clients.get('')
  response2 = logged_clients_with_profile.get('')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert "O nas" in response.content.decode('utf-8'), 'Brak informacji na stronie głównej'


@pytest.mark.django_db
def test_add_user(anonymous_client, logged_clients, logged_clients_with_profile):
  user_data = {'username': 'user', 'first_name': 'name', 'last_name': 'surename', 'email': 'user@email.pl', 'password1': 'alamakota10', 'password2': 'alamakota10'}
  response = anonymous_client.get('/add-user/')
  response1 = logged_clients.get('/add-user/')
  response2 = logged_clients_with_profile.get('/add-user/')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  response4 = anonymous_client.post('/add-user/', user_data)
  response5 = logged_clients.post('/add-user/', user_data)
  response6 = logged_clients_with_profile.post('/add-user/', user_data)
  assert response4.status_code == 302  # niezalogowany
  assert response5.status_code == 200  # zalogowany użytkownik
  assert response6.status_code == 200  # zalogowany użytkownik
  assert user_data['username'] in anonymous_client.get('/add-user/').content.decode('utf-8'), 'anonymus_client może dodać user_profile'
  assert "Użytkownik:" in response.content.decode('utf-8'), 'Brak informacji'
  assert "Hasło:" in response.content.decode('utf-8'), 'Brak informacji'

@pytest.mark.django_db
def test_login(anonymous_client, logged_clients, logged_clients_with_profile):
  user_data = {'username': 'username1', 'password': 'password1'}
  response = anonymous_client.get('/login/')
  response1 = logged_clients.get('/login/')
  response2 = logged_clients_with_profile.get('/login/')
  response4 = anonymous_client.post('/login/', user_data)
  response5 = logged_clients.post('/login/', user_data)
  response6 = logged_clients_with_profile.post('/login/', user_data)
  assert user_data['username'] not in anonymous_client.get('/login/').content.decode('utf-8')
  assert user_data['username'] not in logged_clients.get('/login/').content.decode('utf-8')
  assert user_data['username'] not in logged_clients_with_profile.get('/login/').content.decode('utf-8')
  assert response.status_code == 200
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert response4.status_code == 200
  assert response5.status_code == 200  # zalogowany użytkownik
  assert response6.status_code == 200  # zalogowany użytkownik
  assert "Użytkownik:" in response.content.decode('utf-8'), 'Brak informacji'


@pytest.mark.django_db
def test_reset_password(anonymous_client, logged_clients, logged_clients_with_profile):
  user_data = {'username': 'username1', 'password': 'password1'}
  response = anonymous_client.get('/change-password/')
  response1 = logged_clients.get('/change-password/')
  response2 = logged_clients_with_profile.get('/change-password/')
  response4 = anonymous_client.post('/change-password/', user_data)
  response5 = logged_clients.post('/change-password/', user_data)
  response6 = logged_clients_with_profile.post('/login/', user_data)
  assert response.status_code == 302  # jeśli użytkownik niezalogowany, zwraca odpowiedz 302
  assert response1.status_code == 200
  assert response2.status_code == 200
  assert response4.status_code == 302
  assert response5.status_code == 200  # zalogowany użytkownik
  assert response6.status_code == 200  # zalogowany użytkownik


@pytest.mark.django_db
def test_user_profile(anonymous_client, logged_clients,  logged_clients_with_profile):
  response = anonymous_client.get('/my-profile/')
  response1 = logged_clients.get('/my-profile/')
  response2 = logged_clients_with_profile.get('/change-password/')
  assert response.status_code == 302
  assert response1.status_code == 200
  assert response2.status_code == 200

@pytest.mark.django_db
def test_user_profile_edit(anonymous_client, logged_clients, logged_clients_with_profile):
  user_data = {'username': 'user', 'first_name': 'name', 'last_name': 'surename', 'email': 'user@email.pl',
               'password1': 'alamakota10', 'password2': 'alamakota10'}
  response = anonymous_client.get('/edit-my-profile/')
  response1 = logged_clients.get('/edit-my-profile/')
  response2 = logged_clients_with_profile.get('/edit-my-profile/')
  assert response.status_code == 302
  assert response1.status_code == 403
  assert response2.status_code == 200
  response4 = anonymous_client.post('/edit-my-profile/', user_data)
  response5 = logged_clients.post('/edit-my-profile/', user_data)
  response6 = logged_clients_with_profile.post('/edit-my-profile/', user_data)
  assert response4.status_code == 302
  assert response5.status_code == 403
  assert response6.status_code == 302


@pytest.mark.django_db
def test_userprofile_form(anonymous_client, logged_clients, logged_clients_with_profile):
  response = anonymous_client.get('/create-my-profile/')
  response1 = logged_clients.get('/create-my-profile/')
  response2 = logged_clients_with_profile.get('/create-my-profile/')
  assert response.status_code == 302
  assert response1.status_code == 200
  assert response2.status_code == 200
