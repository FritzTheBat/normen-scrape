import scrapy, re 

class NormSpider(scrapy.Spider):
    name = 'GesetzblattBayern'
    start_urls = ['https://www.verkuendung-bayern.de/gvbl/?offset=0']

    def parse(self, response):
        for item in response.css('#search-results-table tbody tr'):

            id = item.css("td:nth-child(4) ::text").get()
            if id:
                yield {
                    'ID': re.sub("\s+"," ",id.strip()),
                    'Titel': item.css("td:nth-child(3) ::text").get().strip(),
                    'Link': response.urljoin(item.css('td:nth-child(1) a::attr(href)').get()),
                    'Datum': item.css("td:nth-child(2) ::text").get().strip(),
                    'Seiten': re.sub("^\d{4} ","",item.css("td:nth-child(1) ::text").get().strip())+" ff.",
                }


        m = re.search("offset=(\d+)",response.request.url)
        if m and int(m.group(1)) < 5 * 16:

            nextUrl = re.sub("offset=(\d+)",lambda m: "offset="+str(int(m.group(1))+16),response.request.url)
            request = scrapy.Request(url=nextUrl)
            yield request