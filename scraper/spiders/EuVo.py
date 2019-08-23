import scrapy, re
from scrapy.http import Request

class NormSpider(scrapy.Spider):
    name = 'EUVerordnungen'
    # start_urls = ['https://eur-lex.europa.eu/search.html?page=1&DB_TYPE_OF_ACT=regulation&CASE_LAW_SUMMARY=false&DTS_DOM=ALL&typeOfActStatus=REGULATION&type=advanced&lang=de&SUBDOM_INIT=ALL_ALL&DTS_SUBDOM=ALL_ALL']
    start_urls = ["https://eur-lex.europa.eu/search.html?VV=true&DB_TYPE_OF_ACT=allRegulation&DTS_DOM=EU_LAW&typeOfActStatus=ALL_REGULATION&type=advanced&lang=de&SUBDOM_INIT=LEGISLATION&DTS_SUBDOM=LEGISLATION&page=1&sortOne=DD&sortOneOrder=desc&sortOneOrder=desc"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'clientlanguage':'de'}, callback=self.parse)

    def parse(self, response):
        for item in response.css('.SearchResult'):
            yield {
                'ID': "EU VO "+item.css("h2").re_first('\d{4}\/\d+'),
            	'Titel': item.css('h2 ::text').get(),
            	'Link': re.sub(r"&qid=\d+|&rid=\d+","",response.urljoin(item.css('h2 a::attr(href)').get()).replace("/AUTO/","/DE/TXT/")),
                'Datum': re.sub("\/",".",item.re_first(r'\d{2}\/\d{2}\/\d{4}'))
            }

        m = re.search("page=(\d+)",response.request.url)
        if m and int(m.group(1)) < 5:
            nextUrl = re.sub("page=(\d+)",lambda m: "page="+str(int(m.group(1))+1),response.request.url)
            request = scrapy.Request(url=nextUrl)
            yield request
