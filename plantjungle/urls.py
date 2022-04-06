"""plantjungle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import home_app.views
from home_app.views import HomeView

from plant_app import views as plant_views
from home_app import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.HomeView.as_view(), name='home-view'),
    path('plant-description/<slug:category>/<slug:plant>/', plant_views.PlantView.as_view(), name='plant-view'),
    #path('check-price/', plant_views.check_price),
    path('categories/', plant_views.CategoryView.as_view(), name='all-categories-list'),
    #path('plant-add/', plant_views.PlantAddView.as_view()),
    path('plants/', plant_views.PlantListView.as_view(), name='all-plants-list'),
    path('search-result/', plant_views.SearchResultView.as_view(), name='search-result'),
    path('plant-filter/', plant_views.FilterPlantView.as_view(), name='plant-filter'),
    path('plant-filter/', plant_views.FilterPlantView.as_view(), name='plant-filter-result'),
    path('category/<slug>/', plant_views.ChosenCategoryView.as_view(), name='chosen-category'),
    path('room-part/<slug>/', plant_views.ChosenRoompartView.as_view(), name='chosen-roompart'),
    path('home-room/<slug>/', plant_views.ChosenHomeroomView.as_view(), name='chosen-homeroom'),
    path('window-side/<slug>/', plant_views.ChosenWindowsideView.as_view(), name='chosen-windowside'),
    path('influence/<str:data>/', plant_views.ChosenInfluenceView.as_view(), name='chosen-influence'),
    path('add-user/', home_views.AddUserView.as_view(), name='add-user'),
    path('login/', home_views.LoginView.as_view(), name='login'),
    path('logout/', home_views.log_out, name='logout'),
    path('create-my-profile/', home_views.CreateProfileView.as_view(), name='create-my-profile'),
    path('edit-my-profile/', home_views.EditProfileView.as_view(), name='edit-my-profile'),
    path('my-profile/', home_views.UserProfileView.as_view(), name='my-profile'),
    path('change-password/', home_views.ResetPasswordView.as_view(), name='change-password'),
    path('my-wishlist/', plant_views.AddToWishlistView.as_view(), name='my-wishlist'),
    path('my-plants/', plant_views.AddToMyplantsView.as_view(), name='my-plants'),
    path('my-view-plants/delete-wishlist/<slug>/', plant_views.DeletePlantWishlistView.as_view(), name='delete-plant-wishlist'),
    path('my-view-plants/delete-plants/<slug>/', plant_views.DeletePlantPlantsView.as_view(), name='delete-plant-plants'),
    path('price-compare/<slug>/', plant_views.PriceCompareView.as_view(), name='price-compare'),
    #path('logout/', home_views.ResetPasswordView.as_view(), name='logout'),
    #path('plant-filter-results/', plant_views.FilterPlantView.as_view(), name='plant-filter-results'),
    #path('plant-spider/', plant_views.PlantSpider),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
