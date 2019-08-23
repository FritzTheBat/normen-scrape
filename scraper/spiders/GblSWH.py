import scrapy, re 
import datetime
now = datetime.datetime.now()
class NormSpider(scrapy.Spider):
    name = 'GesetzblattSWH'
    start_urls = ['https://www.schleswig-holstein.de/DE/Landesregierung/IV/Service/GVOBl/gvobl_node.html']

    def parse(self, response): 
        for item in response.css('.generictable.singleview tbody tr'):
            yield {
                'ID': item.css("td:nth-child(2) a ::text").get().split("/")[0].strip(), #
                # 'Titel': item.css("td:nth-child(2) a ::text").get().strip(),
                'Link': response.urljoin(item.css('td:nth-child(2) a ::attr(href)').get()),
                'Datum': item.css("td:nth-child(1) ::text").get().strip()
            }

        # nextUrl = re.sub("chronologisch/(\d+)",lambda m: "chronologisch/"+str(int(m.group(1))+-1),response.request.url)
        # request = scrapy.Request(url=nextUrl)
        # yield request