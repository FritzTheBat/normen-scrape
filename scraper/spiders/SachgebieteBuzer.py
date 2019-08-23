import scrapy, re 
import datetime, time
from urllib.parse import urlparse
now = datetime.datetime.now()




class BuzerSpider(scrapy.Spider):
    name = 'BuzerSpider'
    start_urls = ["https://de.wikipedia.org/w/index.php?title=Kategorie:Rechtsquelle_(Deutschland)&pageuntil=Bundesleistungsgesetz#mw-pages"]

    def parse(self, response): 

        infoBox = response.css('.infobox').get()
        if infoBox:
            yield {
                'FNA': [l.xpath("string()").get().strip() for l in response.xpath("//*[contains(@class,'infobox')] //td[contains(.,'Rechtsmaterie:')] //following-sibling::td //a")],
                'Titel': response.css('h1::text').get(),
                'Wiki': response.request.url,
                'Link': response.xpath("//a[contains(@href,'www.gesetze-im-internet.de')]").css('::attr(href)').get()
            }

        for item in response.css("#mw-pages .mw-content-ltr a"):
            request = scrapy.Request(url=response.urljoin(item.css("::attr(href)").get())) # meta={'municipalityName':  response.meta.get("municipalityName"),'depth': int(response.meta.get("depth",0))+1}
            yield request


        for item in response.xpath("//a[contains(.,'nächste Seite')]"):
            request = scrapy.Request(url=response.urljoin(item.css("::attr(href)").get())) # meta={'municipalityName':  response.meta.get("municipalityName"),'depth': int(response.meta.get("depth",0))+1}
            yield request
                        
                            