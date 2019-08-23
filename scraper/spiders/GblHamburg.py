import scrapy, re
import datetime
now = datetime.datetime.now()

class NormSpider(scrapy.Spider):
    name = 'GesetzblattHamburg'
    year = str(now.year)
    start_urls = ['https://www.luewu.de/gvbl/']

    def parse(self, response):

        #issue list
        for item in response.xpath("//a[contains(.,'Ausgabe') and contains(.,'.2019')]"):
            href = response.urljoin(item.css('a::attr(href)').get())
            yield {
                'ID': re.search("(\d+)",item.css("::text").get()).group(1),
                'Titel': item.css("::text").get(), 
                'Link': href, # a ::href
                'Datum': re.search("(\d{2}\.\d{2}\.\d{4})",item.css("::text").get()).group(1).replace("&nbsp;"," "),
                "Seiten": re.search(r"Seiten (\d+\D+\d+)", item.css("::text").get()).group(1).replace("&nbsp;"," ")
            }
