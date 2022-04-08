import scrapy
from ..items import ScrapyJungleBoogieItem
from ..items import ScrapyZielonyParapetItem
from ..items import ScrapyFloraPointItem, ScrapyCocafloraItem


# Class for scrapying JungleBoogie wepsite - passing item objects to pipeline and saving items to database
class JungleBoogieSpider(scrapy.Spider):
    name = 'jungleboogie-plantscraper'
    #allowed_domains = ['https://www.jungleboogie.pl']
    start_urls = ['https://www.jungleboogie.pl/kategoria-produktu/rosliny/']


# Other way to start scrapy cralwer by manage commands in plant_app
   # def start_requests(self):
       # yield scrapy.Request('https://www.jungleboogie.pl/kategoria-produktu/rosliny/')

    # def parse(self, response):
    #     for plant in response.css('li.wcpa_has_options, product, type-product'):
    #         name = plant.css('a.woocommerce-LoopProduct-link, woocommerce-loop-product__link').attrib['aria-label']
    #         price_data = plant.css('span.woocommerce-Price-amount bdi::text').get()
    #         price = float(price_data[0:-3].replace(',', '.').replace(' ', '')) #float(price[0:-3].replace(',','.'))
    #         picture = plant.css('img.attachment-woocommerce_thumbnail, size-woocemmerce_thumbnail').attrib['src']
    #         link = plant.css('a.woocommerce-LoopProduct-link, woocommerce-loop-product__link').attrib['href']
    #         if ScrapyJungleBoogie.objects.filter(name=name).filter(link=link).first():
    #             plant = ScrapyJungleBoogie.objects.filter(name=name).first()
    #             plant.price = price
    #             plant.picture = picture
    #             plant.link = link
    #             plant.save()
    #         else:
    #             ScrapyJungleBoogie.objects.create(name=name, price=price, picture=picture, link=link)
    #     for element in ScrapyJungleBoogie.objects.all():
    #         latest_date = ScrapyJungleBoogie.objects.latest("updated")
    #         if element.updated!=latest_date:
    #             plant.price = None
    #             plant.picture = ""
    #             plant.link = ""
    #             plant.save()
    #
    #     #for element in ScrapyJungleBoogie.objects.all():
    #
    #         yield {
    #              'name': name,
    #              'price': price,
    #              'picture': picture
    #          }
    #
    #     next_page = response.css('a.next').attrib['href']
    #     if next_page is not None:
    #         yield response.follow(next_page, callback=self.parse)  # parse wraca do fukncji i przechodzi ja od nowa


    # Scrapying website
    def parse(self, response):
        for plant in response.css('li.wcpa_has_options, product, type-product'):
            item = ScrapyJungleBoogieItem()
            #item = ItemLoader(item=ScrapyJungleBoogieItem(), selector=plant)
            #item.add_css('name', 'a.woocommerce-LoopProduct-link, woocommerce-loop-product__link')
            item['name'] = plant.css('a.woocommerce-LoopProduct-link, woocommerce-loop-product__link').attrib['aria-label']
            #item.add_css('price', 'span.woocommerce-Price-amount bdi::text')
            item['price'] = float((plant.css('span.woocommerce-Price-amount bdi::text').get())[0:-3].replace(',', '.').replace(' ', ''))  #float(price[0:-3].replace(',','.'))
            #item.add_css('picture', 'img.attachment-woocommerce_thumbnail, size-woocemmerce_thumbnail')
            #item['picture'] = (plant.css('img.attachment-woocommerce_thumbnail, size-woocemmerce_thumbnail data-src').attrib['src'])[26:]
            item['picture'] = plant.css('img.attachment-woocommerce_thumbnail, size-woocemmerce_thumbnail data-src').attrib['src']
            #item.add_css('link', 'a.woocommerce-LoopProduct-link, woocommerce-loop-product__link')
            item['link'] = plant.css('a.woocommerce-LoopProduct-link, woocommerce-loop-product__link').attrib['href']

            yield item
        # for link in response.css('a.woocommerce-LoopProduct-link').attrib['href']:
        #     yield response.follow(link.get(), callback=self.parse_plants)

    # def parse_plants(self, response):
    #     item = ScrapyJungleBoogieItem()
    #     item['name'] = response.css('h1.product_title::text')
    #     item['price'] = float(
    #         (response.css('span.woocommerce-Price-amount bdi::text').get())[0:-3].replace(',', '.').replace(' ', ''))
    #     item['picture'] = response.css('img.attachment-woocommerce_thumbnail, size-woocemmerce_thumbnail data-src').attrib['src']
    #     yield item

    # Getting the to next available searched page
        next_page = response.css('a.next, page-numbers').attrib['href']
        if next_page:
            yield response.follow(next_page, callback=self.parse)  # parse wraca do fukncji i przechodzi ja od nowa


# Class for scrapying ZielonyParapet wepsite - passing item objects to pipeline and saving items to database
class ZielonyParapetSpider(scrapy.Spider):
    name = 'zielonyparapet-plantscraper'
   #allowed_domains = ['https://www.jungleboogie.pl']
    start_urls = ['https://zielony-parapet.pl/38-kwiaty-domowe#']

    # Scrapying website
    def parse(self, response):
        for plant in response.css('li.ajax_block_product, col-xs-12, col-md-4'):
            item = ScrapyZielonyParapetItem()
            item['name'] = plant.css('a.product-name').attrib['title']
            item['price'] = float((plant.css('span.price::text').get())[0:-3].replace(',', '.').replace(' ', ''))  #float(price[0:-3].replace(',','.'))
            item['picture'] = plant.css('img.replace-2x, img-responsive').attrib['src']
            item['link'] = plant.css('a.product-name').attrib['href']
            yield item


        # Getting the to next available searched page
        next_page = response.css('li.pagination_next a').attrib['href']
        if next_page:
            yield response.follow(next_page, callback=self.parse)  # parse wraca do fukncji i przechodzi ja od nowa


# Class for scrapying  FloraPoint wepsite - passing item objects to pipeline and saving items to database
class FloraPointSpider(scrapy.Spider):
    name = 'florapoint-plantscraper'
   #allowed_domains = ['https://www.jungleboogie.pl']
    start_urls = ['https://www.florapoint.pl/kategoria-produktu/rosliny/']

    # Scrapying website
    def parse(self, response):
        for plant in response.css('div.product-small, col, has-hover'):
            item = ScrapyFloraPointItem()
            item['name'] = plant.css('a.woocommerce-LoopProduct-link::text').get()
            item['price'] = float((plant.css('span.woocommerce-Price-amount bdi::text').get())[0:-3].replace(',', '.').replace(' ', ''))  #float(price[0:-3].replace(',','.'))
            item['picture'] = plant.css('img.attachment-woocommerce_thumbnail, size woocommerce_thumbnail').attrib['src']
            item['link'] = plant.css('a.woocommerce-LoopProduct-link, woocommerce-loop-product__link').attrib['href']
            yield item


        # Getting the to next available searched page
        next_page = response.css('a.next, page-number').attrib['href']
        if next_page:
            yield response.follow(next_page, callback=self.parse)  # parse wraca do fukncji i przechodzi ja od nowa


# Class for scrapying  FloraPoint wepsite - passing item objects to pipeline and saving items to database
class CocafloraSpider(scrapy.Spider):
    name = 'cocaflora-plantscraper'
   #allowed_domains = ['https://www.jungleboogie.pl']
    start_urls = ['https://www.cocaflora.com/pl/c/ROSLINY-ZIELONE/20']

    # Scrapying website
    def parse(self, response):
        for plant in response.css('div.product'):
            item = ScrapyCocafloraItem()
            item['name'] = plant.css('span.productname::text').get()
            item['price'] = float((plant.css('div.price em::text').get())[0:-3].replace(',', '.').replace(' ', '').replace('\xa0', ''))  #float(price[0:-3].replace(',','.'))
            item['picture'] = 'https://www.cocaflora.com' + plant.css('span.f-grid-12 img').attrib['data-src']
            item['link'] = 'https://www.cocaflora.com' + plant.css("a.prodname, f-row").attrib["href"]
            yield item

        # Getting the to next available searched page
        for x in range(2, 33):
            yield(scrapy.Request(f'https://www.cocaflora.com/pl/c/ROSLINY-ZIELONE/20/{x}', callback=self.parse))
