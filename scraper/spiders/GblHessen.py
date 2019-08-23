import scrapy, re
import datetime
now = datetime.datetime.now()
import requests



class NormSpider(scrapy.Spider):
    name = 'GesetzblattHessen'
    year = str(now.year)


    start_urls = ['http://starweb.hessen.de']

    def parse(self, response):

        for i in range(1,300):

            url = "http://starweb.hessen.de/cache/GVBL/2019/"+"{:05d}".format(i)+".pdf"
            print("try: ",url)
            try:
                request = requests.get(url) #Here is where im getting the error
                if request.status_code == 200:
            


                   yield {
                    'ID': i,
                    'Link': url
                    }

                else:
                    break
            
            except:
                print('Web site does not exist')
                break