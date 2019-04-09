import scrapy, re
import datetime
now = datetime.datetime.now()

class NormSpider(scrapy.Spider):
    name = 'MinisterialblattNiedersachsen'
    start_urls = ['https://niedersachsen.de/politik_staat/gesetze_verordnungen/download-verkuendungsblaetter-108794.html']

    def parse(self, response):
        for item in response.css('.downloadliste li .download'):

            id = item.css("::text").get()
            if "MBl." in id:
                yield {
                    'ID': item.re_first(r'Nr\. \d+/\d{4}'),
                    'Titel': id.split(",")[0],
                    'Link': item.css("::attr(href)").get(),
                    'Datum': item.re_first(r'\d{2}\.\d{2}\.\d{4}'),
                    "Seiten": item.re_first(r'S\. \d+\s?-\d+')
                }




        # todo: where to find older years?