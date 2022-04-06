from django.db import models
from django.contrib.auth.models import User

from plant_app.models import Plant


# Class Model for creating UserProfile objects
class UserProfile(models.Model):  # profil użytkownika
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")  #pip install pillow
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    wishlist = models.ManyToManyField(Plant, related_name='wish_list_profile')
    plants = models.ManyToManyField(Plant, related_name='my_plants_profile')
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.username
