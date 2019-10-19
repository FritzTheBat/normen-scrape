import scrapy, re 
from scrapy.http import FormRequest

class NormSpider(scrapy.Spider):
    name = 'GesetzblattThueringen'
    start_urls = ["http://www.parldok.thueringen.de/ParlDok/formalkriterien"]

    def parse(self, response):
        # print(response.body)
        for item in response.css('#parldokresult tr'):

            id = item.css('[headers="result-titel"] a ::text').get()
            link = item.css('a::attr(href)').get()
            date = item.css('[headers="result-datum"] ::text').get()
            
            if id:
                self.currentId= re.sub("\s+"," ",id.strip())
                self.currentLink= link
            if date:
                yield {
                    'ID': self.currentId,
                    # 'Titel': item.css("td:nth-child(3) ::text").get().strip(),
                    'Link': response.urljoin(self.currentLink),
                    'Datum': date,
                    # 'Seiten': re.sub("^\d{4} ","",item.css("td:nth-child(1) ::text").get().strip())+" ff.",
                }



                # LegislaturperiodenNummer=7&UrheberPersonenId=&UrheberSonstigeId=&DokumententypId=14&BeratungsstandId=&Datum=&DatumVon=&DatumBis=
        frmdata = {"LegislaturperiodenNummer": "6", "DokumententypId":'9',"UrheberPersonenId":"","UrheberSonstigeId":"","BeratungsstandId":"","Datum":"","DatumVon":"","DatumBis":""}
        url = "http://www.parldok.thueringen.de/ParlDok/formalkriterien"
        yield FormRequest(url, callback=self.parse, formdata=frmdata)