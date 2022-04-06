from django.contrib import admin

from .models import Plant, Category, WindowSide, HomeRoom, RoomPart
# Register your models here.

admin.site.register(Plant)

admin.site.register(Category)

admin.site.register(WindowSide)

admin.site.register(HomeRoom)

admin.site.register(RoomPart)
