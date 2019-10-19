import scrapy, re 
import datetime
now = datetime.datetime.now()
import urllib3
http = urllib3.PoolManager()

class NormSpider(scrapy.Spider):
    name = 'GesetzblattSaarland'
    start_urls = ['http://www.amtsblatt.saarland.de/jportal/portal/page/fpverksl.psml']

    def parse(self, response):
        for item in response.css('.newsInhalt'):


            self.titel = item.css('a ::text').get().replace("Zum ","")
            self.date = item.re_first('(?<=vom )\d+\. [A-ZÖÄÜ][a-zöäüß]+ \d{4}')
            self.id = item.re_first('(?<=Nr\. )\d+')

            nextUrl = response.urljoin(item.css('a::attr(href)').get())
            request = scrapy.Request(url=nextUrl)
            yield request

        pdfIframe = response.css("#externIframe::attr(src)").get()
        if pdfIframe:
            yield {
                'ID': self.id,
                'Titel': self.titel,
                'Link': response.urljoin(pdfIframe),
                'Datum': self.date
            }

       