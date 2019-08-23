import scrapy, re 

class NormSpider(scrapy.Spider):
    name = 'MinisterialblattBayern'
    start_urls = ['https://www.verkuendung-bayern.de/baymbl/'] #,'https://www.verkuendung-bayern.de/amtsblatt/ausgabe/allmbl-2019-1/'

    def parse(self, response):


        for item in response.css('#search-results-table tbody tr'):

            id = item.css("td:nth-child(1) ::text").get()
            if id:
                yield {
                    'ID': re.sub("\s+"," ",id.strip()),
                    'Titel': item.css("td:nth-child(3) ::text").get().strip(),
                    'Link': response.urljoin(item.css('td:nth-child(1) a::attr(href)').get()),
                    'Datum': item.css("td:nth-child(5) ::text").get(),
                    # "Seiten" : item.css("td:nth-child(4) ::text").get().strip()+" ff.",
                }

        nextUrl = response.urljoin(response.xpath('//a[contains(@title, "Weiterblättern")]/@href').get())
        request = scrapy.Request(url=nextUrl)
        yield request