import scrapy, re
from scrapy.http import Request
import datetime
now = datetime.datetime.now()

class NormSpider(scrapy.Spider):
    name = 'BundesGbl'
    year = str(now.year)
    issue = 1
    start_urls = ["https://media.offenegesetze.de/bgbl1/"+year+"/bgbl1_"+year+"_"+str(issue)+".pdf"]

    def parse(self, response):
        yield {
            'ID': "bgbl1_"+self.year+"_"+str(self.issue),
            # 'Titel': item.css('h2 ::text').get(),
            'Link': response.request.url,
         #    'Datum': re.sub("\/",".",item.re_first(r'\d{2}\/\d{2}\/\d{4}'))
        }
            
        self.issue+=1
        nextUrl = "https://media.offenegesetze.de/bgbl1/"+self.year+"/bgbl1_"+self.year+"_"+str(self.issue)+".pdf"
        yield scrapy.Request(url=nextUrl)
