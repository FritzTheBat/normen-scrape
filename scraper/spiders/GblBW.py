import scrapy, re
import datetime
now = datetime.datetime.now()

class NormSpider(scrapy.Spider):
    name = 'GesetzblattBW'
    year = str(now.year)
    start_urls = ['http://www.landesrecht-bw.de/jportal/portal/t/dnn/page/bsbawueprod.psml/media-type/html?action=portlets.jw.ControlElementsAction&selectedcontrolelement=Verkuendungsblaetter']

    def parse(self, response):

   


        # main page link to 
        gblLink = response.xpath("//a[@class='HauptResultList'  and contains(.,'Gesetzblatt')]")
        if gblLink:
            href = response.urljoin(gblLink.css('::attr(href)').get())
            print("link is",href)
            request = scrapy.Request(url=href)
            yield request
        
        else:
            print("response.text:",response.text)


        #issue list
        for item in response.xpath("//a[@class='TrefferlisteHervorheben' and contains(.,'Gesamtausgabe')]"):
            href = response.urljoin(item.css('a::attr(href)').get())
            request = scrapy.Request(url=href)
            yield request



        # #single issue
        # if response.css("h1.mbottom_s_i"):
        #     yield {
        #         'ID': re.search("\d{4,}-.*$",response.request.url).group(0), # item.re_first('<h3>Fundstelle und systematische Gliederungsnummer</h3>.*?(?=<br>)')
        #         'Titel': response.css("h1::text").get(), 
        #         'Link': response.urljoin(response.css("#print_save_box a::attr(href)").get()), # a ::href
        #         'Datum': re.search("Vollzitat:.{5,300}?(\d+\..{2,40}?\d{4})",response.body_as_unicode()).group(1).replace("&nbsp;"," "),
        #         "Seiten": re.search(r"\(.{2,40}?(S\..*?)\)",response.body_as_unicode()).group(1).replace("&nbsp;"," ")
        #     }


        # # next search res page
        # for item in response.css('.forward>a:first-child'):
        #     href = response.urljoin(item.css('::attr(href)').get())
        #     print("next res page",href)
        #     request = scrapy.Request(url=href)
        #     yield request