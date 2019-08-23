import scrapy, re 

class NormSpider(scrapy.Spider):
    name = 'GesetzblattBerlin'
    start_urls = ['https://www.berlin.de/sen/justiz/service/gesetze-und-verordnungen/artikel.261829.php']

    def parse(self, response):
        for item in response.css('.body .modul-download'):

            id = item.css(".header strong ::text").get().strip()
            if id and not "Gesamtsachwortverzeichnis" in id:
                yield {
                    'ID': re.sub("\s+"," ",id),
                    'Titel': id,
                    'Link': response.urljoin(item.css('.download-btn a::attr(href)').get()),
                    'Datum': id.split("vom ")[-1].strip(),
                    'Seiten': id.split("/")[0].replace("Seiten","").strip()+" ff.",
                }



        for item in response.css('.html5-section.body .textile li'):

            nextUrl = response.urljoin(item.css("a::attr(href)").get())
            if not ".pdf" in nextUrl:
                request = scrapy.Request(url=nextUrl)
                yield request

