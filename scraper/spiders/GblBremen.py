import scrapy, re 

class NormSpider(scrapy.Spider):
    name = 'GesetzblattBremen'
    start_urls = ['https://www.gesetzblatt.bremen.de/?skip=0&max=-1']

    def parse(self, response):
        for item in response.css('.main_article li'):

            title = item.re_first('<strong>Hinweistext:</strong>.*?(?=<br>)')
            if not title: title ="??"
            id = item.css('h2 a::text').get()
            if id:
                yield {
                    'ID': id,
                    'Titel': title.replace("<strong>Hinweistext:</strong>",""),
                    'Link': response.urljoin(item.css('h2 a::attr(href)').get()),
                    'Datum': item.re_first(r'\d{2}\.\d{2}\.\d{4}'),
                    "Seiten": item.re_first(r'(?<=\()S\. [^\)]+(?=\))')
                }

        # no next page