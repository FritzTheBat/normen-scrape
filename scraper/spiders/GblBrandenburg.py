import scrapy, re 
import datetime
now = datetime.datetime.now()
class NormSpider(scrapy.Spider):
    name = 'GesetzblattBrandenburg'
    year = str(now.year)
    start_urls = ['http://bravors.brandenburg.de/de/veroeffentlichungsblaetter_chronologisch/'+year]

    def parse(self, response):
        resList = list(response.xpath("descendant-or-self::a[@href and contains(@href, 'GVBl') and not(contains(@href, '-Anlage'))]"))
        resList.reverse()
        for item in resList: #.css("a[href*=GVBl]")
            yield {
                'ID': re.sub(" \([^\)]+KB\)","",item.attrib.get('title')).replace("Gesetz- und Verordnungsblatt ",""), 
                # 'Titel': item.css("td:nth-child(3) ::text").get().strip(),
                'Link': response.urljoin(item.attrib.get('href')),
                # 'Datum': item.css("td:nth-child(2) ::text").get().strip(),
            }

        # nextUrl = re.sub("chronologisch/(\d+)",lambda m: "chronologisch/"+str(int(m.group(1))+-1),response.request.url)
        # request = scrapy.Request(url=nextUrl)
        # yield request