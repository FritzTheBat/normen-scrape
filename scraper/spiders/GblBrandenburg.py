import scrapy, re 

class NormSpider(scrapy.Spider):
    name = 'GesetzblattBrandenburg'
    start_urls = ['http://bravors.brandenburg.de/de/veroeffentlichungsblaetter_chronologisch/2019']

    def parse(self, response):
        for item in response.xpath("descendant-or-self::a[@href and contains(@href, 'GVBl') and not(contains(@href, '-Anlage'))]"): #.css("a[href*=GVBl]")
            yield {
                'ID': re.sub(" \([^\)]+KB\)","",item.attrib.get('title')).replace("Gesetz- und Verordnungsblatt ",""), 
                # 'Titel': item.css("td:nth-child(3) ::text").get().strip(),
                'Link': response.urljoin(item.attrib.get('href')),
                # 'Datum': item.css("td:nth-child(2) ::text").get().strip(),
            }

        nextUrl = re.sub("chronologisch/(\d+)",lambda m: "chronologisch/"+str(int(m.group(1))+-1),response.request.url)
        request = scrapy.Request(url=nextUrl)
        yield requestitem.css("::attr(href)").get()