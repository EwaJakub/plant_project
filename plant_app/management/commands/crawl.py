from django.core.management.base import BaseCommand
from plantscraper.plantscraper.spiders.plantspider import JungleBoogieSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


# Commands that starts CrawlerProcess in scrapy application, one of ways to start crawling procces
# class Command(BaseCommand):
#     help = "Release the spiders"
#
#     def handle(self, *args, **options):
#         process = CrawlerProcess(get_project_settings())
#
#         process.crawl(JungleBoogieSpider)
#         process.start()