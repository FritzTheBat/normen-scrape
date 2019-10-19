import scrapy, re 
import datetime
now = datetime.datetime.now()
import urllib3
http = urllib3.PoolManager()

class NormSpider(scrapy.Spider):
    name = 'GesetzblattSaarland'
    year = str(now.year)
    start_urls = ['http://www.amtsblatt.saarland.de/jportal/docs/news_anlage/sl/pdf/VerkBl/ABl/ads_39-2019_teil_I_signed.pdf'+year+'/GBl'+year+'01.pdf']

    def parse(self, response):
        
        for i in range(1,50):
            nextUrl = re.sub("\d\d\.pdf","{:02d}".format(i)+".pdf",self.start_urls[0])
            r = http.request('GET', nextUrl, preload_content=False)
            if r.status==200:

                yield {
                    'ID': nextUrl.split("/")[-1].replace(".pdf",""),
                    'Link': nextUrl
                }
            else:
                break

