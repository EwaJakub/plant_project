from django import forms
from .models import WORLD_DIRECTIONS, HOME_ROOM, ROOM_PART, ANIMAL_INFLUENCE, AIR_PURIFYING, Category


# Function which extract tuple for choices field in FilterPlantForm
def category():
    category_list = []
    categories = Category.objects.all()
    for category in categories:
        category_list.append((category.name, category.name))
    return category_list


# Class Form for extracting filtered data from PLant table
class FilterPlantForm(forms.Form):
    category = forms.MultipleChoiceField(label='Gatunek', choices=category(), widget=forms.CheckboxSelectMultiple, required=False)
    window_direction = forms.MultipleChoiceField(label='Kierunek świata', choices=WORLD_DIRECTIONS, widget=forms.CheckboxSelectMultiple, required=False)
    home_room = forms.MultipleChoiceField(label='Rodaj pomieszczenia', choices=HOME_ROOM, widget=forms.CheckboxSelectMultiple, required=False)
    room_part = forms.MultipleChoiceField(label='Część pomieszczenia', choices=ROOM_PART, widget=forms.CheckboxSelectMultiple, required=False)
    animal_influence = forms.MultipleChoiceField(label='Wpływ na zwierzęta', choices=ANIMAL_INFLUENCE, widget=forms.CheckboxSelectMultiple, required=False)
    air_purifying = forms.MultipleChoiceField(label='Wpływ na powietrze', choices=AIR_PURIFYING, widget=forms.CheckboxSelectMultiple, required=False)


