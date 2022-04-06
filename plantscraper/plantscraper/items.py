from plant_app.models import ScrapyJungleBoogie, ScrapyZielonyParapet, ScrapyFloraPoint, ScrapyCocaflora

from scrapy_djangoitem import DjangoItem



# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# Connecting ScrapyItem to DjangoModel
class ScrapyJungleBoogieItem(DjangoItem):
    django_model = ScrapyJungleBoogie


# Connecting ScrapyItem to DjangoModel
class ScrapyZielonyParapetItem(DjangoItem):
    django_model = ScrapyZielonyParapet


# Connecting ScrapyItem to DjangoModel
class ScrapyFloraPointItem(DjangoItem):
    django_model = ScrapyFloraPoint


# Connecting ScrapyItem to DjangoModel
class ScrapyCocafloraItem(DjangoItem):
    django_model = ScrapyCocaflora