from plant_app.models import ScrapyJungleBoogie, ScrapyZielonyParapet, ScrapyCocaflora, ScrapyFloraPoint
from datetime import datetime


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
# import django
# django.setup()


# Scrapy pipeline which is processing the given by spider items and changing them /saving in database
class ScrapyPlantsPipeline(object):

    def process_item(self, item, spider):
       #ScrapyJungleBoogie.objects.all().delete()
        if ScrapyJungleBoogie.objects.filter(name=item['name']).filter(link=item['link']).first():
            plant = ScrapyJungleBoogie.objects.filter(name=item['name']).filter(link=item['link']).first()
            plant.price = item['price']
            plant.picture = item['picture']
            plant.link = item['link']
            plant.save()
        elif ScrapyZielonyParapet.objects.filter(name=item['name']).filter(link=item['link']).first():
            plant = ScrapyZielonyParapet.objects.filter(name=item['name']).filter(link=item['link']).first()
            plant.price = item['price']
            plant.picture = item['picture']
            plant.link = item['link']
            plant.save()
        elif ScrapyFloraPoint.objects.filter(name=item['name']).filter(link=item['link']).first():
            plant = ScrapyFloraPoint.objects.filter(name=item['name']).filter(link=item['link']).first()
            plant.price = item['price']
            plant.picture = item['picture']
            plant.link = item['link']
            plant.save()
        elif ScrapyCocaflora.objects.filter(name=item['name']).filter(link=item['link']).first():
            plant = ScrapyCocaflora.objects.filter(name=item['name']).filter(link=item['link']).first()
            plant.price = item['price']
            plant.picture = item['picture']
            plant.link = item['link']
            plant.save()
        else:
            item.save()
        return item



 #    def process_item(self, item, spider):
 #        if ScrapyJungleBoogie.objects.filter(name=item.name).filter(link=item.link).first():
 #            plant = ScrapyJungleBoogie.objects.filter(name=item.name).first()
 #            plant.price = item.price
 #            plant.picture = item.picture
 #            plant.link = item.link
 #            plant.save()
 #        else:
 #            ScrapyJungleBoogie.objects.create(name=item.name, price=item.price, picture=item.picture, link=item.link)
 # #       self.con.commit()
 #        return item


# class PlantscraperPipeline(object):
#     def __init__(self):
#         self.con = sqlite3.connect('mój projekt/db.sqlite3')
#         self.cur = self.con.cursor("""CREATE TABLE IF NOT EXISXT""")
#
#     def creat_table(self):
#         self.cur.ececute
#
#     def process_item(self, item, spider):
#         item.save()
#         return item

# class ScrapyZielonyParapetPipeline(object):
#
#     def process_item(self, item, spider):
#         if ScrapyZielonyParapet.objects.filter(name=item['name']).filter(link=item['link']).first():
#             plant = ScrapyZielonyParapet.objects.filter(name=item['name']).filter(link=item['link']).first()
#             plant.price = item['price']
#             plant.picture = item['picture']
#             plant.link = item['link']
#             plant.save()
#         else:
#             item.save()
#         return item
#
#  class ScrapyFloraPointPipeline(object):
#
#     def process_item(self, item, spider):
#         if ScrapyFloraPoint.objects.filter(name=item['name']).filter(link=item['link']).first():
#             plant = ScrapyFloraPoint.objects.filter(name=item['name']).filter(link=item['link']).first()
#             plant.price = item['price']
#             plant.picture = item['picture']
#             plant.link = item['link']
#             plant.save()
#         else:
#             item.save()
#         return item
#
#
# class ScrapyCocafloraPipeline(object):
#
#     def process_item(self, item, spider):
#         if ScrapyCocaflora.objects.filter(name=item['name']).filter(link=item['link']).first():
#             plant = ScrapyCocaflora.objects.filter(name=item['name']).filter(link=item['link']).first()
#             plant.price = item['price']
#             plant.picture = item['picture']
#             plant.link = item['link']
#             plant.save()
#         else:
#             item.save()
#         return item