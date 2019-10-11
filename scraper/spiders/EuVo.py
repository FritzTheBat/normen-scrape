import scrapy, re
from scrapy.http import Request

class NormSpider(scrapy.Spider):
    name = 'EUVerordnungen'
    # start_urls = ['https://eur-lex.europa.eu/search.html?page=1&DB_TYPE_OF_ACT=regulation&CASE_LAW_SUMMARY=false&DTS_DOM=ALL&typeOfActStatus=REGULATION&type=advanced&lang=de&SUBDOM_INIT=ALL_ALL&DTS_SUBDOM=ALL_ALL']
    start_urls = [ 

                    #Verordnungen:
                    "https://eur-lex.europa.eu/search.html?VV=true&DB_TYPE_OF_ACT=allRegulation&DTS_DOM=EU_LAW&typeOfActStatus=ALL_REGULATION&type=advanced&lang=de&SUBDOM_INIT=LEGISLATION&DTS_SUBDOM=LEGISLATION&page=1&sortOne=DD&sortOneOrder=desc&sortOneOrder=desc",
                    #Beschlüsse:
                    "https://eur-lex.europa.eu/search.html?CASE_LAW_JURE_SUMMARY=false&lang=en&SUBDOM_INIT=ALL_ALL&DTS_DOM=ALL&CASE_LAW_SUMMARY=false&type=advanced&DTS_SUBDOM=ALL_ALL&qid=1570808050808&typeOfActStatus=OTHER&DTC=false&orFM_CODEDGroup=FM_CODED%3DREG_IMPL%2CFM_CODED%3DDEC_IMPL&sortOne=DD&sortOneOrder=desc&sortOneOrder=desc&page=1"
                    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'clientlanguage':'de'}, callback=self.parse)

    def parse(self, response):
        for item in response.css('.SearchResult'):
            print("### ID:",item.css("h2 ::text").get())
            if "Regulation" in item.css("h2 ::text").get():
                id = "EU VO "+item.css("h2").re_first('\d{4}\/\d+')
            else:
                try:
                    id = "EU Decision "+item.css("h2").re_first('\d{4}\/\d+')
                except Exception:
                    try:
                        id = "EU Decision of "+item.css("h2").re_first('\d+\/\d+\/\d{4}')
                    except Exception:
                        continue

            yield {
                'ID': id,
            	'Titel': item.css('h2 ::text').get(),
            	'Link': re.sub(r"&qid=\d+|&rid=\d+","",response.urljoin(item.css('h2 a::attr(href)').get()).replace("/AUTO/","/DE/TXT/")),
                'Datum': re.sub("\/",".",item.re_first(r'\d{2}\/\d{2}\/\d{4}'))
            }

        m = re.search("page=(\d+)",response.request.url)
        if m and int(m.group(1)) < 40:
            nextUrl = re.sub("page=(\d+)",lambda m: "page="+str(int(m.group(1))+1),response.request.url)
            request = scrapy.Request(url=nextUrl)
            yield request
