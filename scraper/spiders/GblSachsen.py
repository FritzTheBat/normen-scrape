import scrapy, re
import datetime
now = datetime.datetime.now()

class NormSpider(scrapy.Spider):
    name = 'GesetzblattSachsen'
    year = str(now.year)


    start_urls = ['https://www.recht-sachsen.de/veroffentlichungen/sgvl.html?p=1','https://www.recht-sachsen.de/veroffentlichungen/sgvl.html?p=2']
    def parse(self, response):

        #single issue
        for item in response.css(".lr-product-description"):
            yield {
                'ID': item.re_first("\d{2}/20\d{2,}"),
                'Titel': item.css("h2::text").get(), 
                'Link': response.urljoin(item.css("u>a::attr(href)").get()), # a ::href
                # 'Datum': re.search("Vollzitat:.{5,300}?(\d+\..{2,40}?\d{4})",response.body_as_unicode()).group(1).replace("&nbsp;"," "),
                # "Seiten": re.search(r"\(.{2,40}?(S\..*?)\)",response.body_as_unicode()).group(1).replace("&nbsp;"," ")
            }

    # start_urls = ['https://www.recht.sachsen.de/suche?search_request=%7B%22edition_abbr%22%3A%22S%C3%A4chsGVBl.%22%2C%22valid_day%22%3A%222019-04-09%22%2C%22categories%22%3A%5B%22G%22%2C%22VO%22%2C%22VwV%22%2C%22FRL%22%2C%22StV%22%2C%22ZuG%22%5D%2C%22include_envelopes%22%3A%221%22%2C%22is_government%22%3A%220%22%2C%22mode%22%3A%22fullsearch%22%2C%22title_search%22%3A%221%22%2C%22origin_year%22%3A'+year+'%7D']

    # def parse(self, response):

    #     #single issue
    #     if response.css("h1.mbottom_s_i"):
    #         yield {
    #             'ID': re.search("\d{4,}-.*$",response.request.url).group(0), # item.re_first('<h3>Fundstelle und systematische Gliederungsnummer</h3>.*?(?=<br>)')
    #             'Titel': response.css("h1::text").get(), 
    #             'Link': response.urljoin(response.css("#print_save_box a::attr(href)").get()), # a ::href
    #             'Datum': re.search("Vollzitat:.{5,300}?(\d+\..{2,40}?\d{4})",response.body_as_unicode()).group(1).replace("&nbsp;"," "),
    #             "Seiten": re.search(r"\(.{2,40}?(S\..*?)\)",response.body_as_unicode()).group(1).replace("&nbsp;"," ")
    #         }


    #     #issue list
    #     for item in response.css('.result_hit'):
    #         href = response.urljoin(item.css('a::attr(href)').get())
    #         request = scrapy.Request(url=href)
    #         yield request


    #     # next search res page
    #     for item in response.css('.forward>a:first-child'):
    #         href = response.urljoin(item.css('::attr(href)').get())
    #         print("next res page",href)
    #         request = scrapy.Request(url=href)
    #         yield request