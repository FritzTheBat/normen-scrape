import scrapy, re

class NormSpider(scrapy.Spider):
    name = 'GesetzblattNRW'
    start_urls = ['https://recht.nrw.de/lmi/owa/br_vbl_liste']

    def parse(self, response):

        #single issue
        for item in response.css('#main1 .standard tr'):
            href = response.urljoin(item.css('td:nth-child(4) a::attr(href)').get()) # 
            id = item.css("td:nth-child(1)::text").get()
            if "detail_text" in href and id:
                yield {
                    'ID': id,
                    'Titel': item.css("td:nth-child(4) a::text").get().strip(),
                    'Link': href,
                    'Datum': item.css("td:nth-child(2)::text").get(),
                    "Seiten": item.css("td:nth-child(5)::text").get()
                }


        #issue list
        for item in response.css('.untergliederung tr'):
            id = item.css("td:nth-child(4) a ::text").get()
            if id: id = id.replace(".html","")
            if id:
                href = response.urljoin(item.css('td:nth-child(4) a ::attr(href)').get())
                request = scrapy.Request(url=href)
                print(request)
                yield request


        # todo: add more years like https://recht.nrw.de/lmi/owa/br_vbl_liste?jahr=2018