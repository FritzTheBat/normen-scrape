import scrapy, re 

class BlogSpider(scrapy.Spider):
    name = 'MinisterialblattBayern'
    start_urls = ['https://www.verkuendung-bayern.de/amtsblatt/ausgabe/allmbl-2019-1/']

    def parse(self, response):


        def is404():
            res = "<h2>AllMBl." not in response.body_as_unicode()
            if res:
                print("404!",response.request.url)
            return res

        if not is404():
            for item in response.css('#search-results-table tbody tr'):

                id = item.css("td:nth-child(1) ::text").get()
                if id:
                    yield {
                        'ID': re.sub("\s+"," ",id.strip()),
                        'Titel': item.css("td:nth-child(3) ::text").get().strip(),
                        'Link': response.urljoin(item.css('td:nth-child(5) a::attr(href)').get()),
                        'Datum': item.css("td:nth-child(2) ::text").get().strip(),
                        "Seiten" : item.css("td:nth-child(4) ::text").get().strip()+" ff.",
                    }


        def guessNextPage(urlMatch):
            if is404(): return "allmbl-" + str(int(urlMatch.group(1))-1)+ "-1"
            else: return "allmbl-" + urlMatch.group(1)+ "-" + str(int(urlMatch.group(2))+1)

        nextUrl = re.sub("allmbl-(\d{4})-(\d+)",guessNextPage,response.request.url)
        request = scrapy.Request(url=nextUrl)
        yield request