import scrapy, re 
import datetime, time
import html
import redis, json
from tqdm import tqdm
redisDb = redis.Redis(host='redis', port=6379, db=0)

from urllib.parse import urlparse
now = datetime.datetime.now()


# positive
probablyInKeyword = ["atzung","erordnung","ATZUNG","ERORDNUNG"]
maybeInKeyword = [".pdf","öffnen","herunterladen","ehr erfahren","PDF"]

# negative
definatelyOutSelector = [".linkliste.downloadliste ul li > ul li a"]
definatelyOutKeyword = ["atzungen","erordnungen"]

maxTimePerDomain = 180


titleRegex = r">(?P<title>[^<]{1,40}(ATZUNG|ORDNUNG|atzung|ordnung|[a-zöäüß]+V|[a-zöäüß]+S)[^<]*)"



def cleanTitle(title):
    try:
        title = title.strip()
        title = title.replace("_"," ")
        title = re.sub("(\.?pdf|PDF)$","",title).strip()
        title = re.sub("\/$","",title).strip()
        title = re.sub("\d+(,|\.)?\d+ ?(KB|MB)$","",title)
        title = re.sub("^\d+ +","",title)
        title = re.sub("^(\d+(\.|/))+\d+ +","",title)
        title = re.sub("^(.{10,})\n[\s\S]*",r"\1",title)
        title = re.sub("^(.{10,}) PDF[\s\S]*",r"\1",title)
        title = re.sub("^:","",title)
        title = re.sub("\d[\d\-]+( - )?","",title)
        title = re.sub("\([^\)]*(PDF|KB|MB)[^\)]*\)$","",title,flags=re.IGNORECASE)
        title = re.sub("^-","",title)
        title = re.sub("^&nbsp;","",title)
        title = html.unescape(title)
    except Exception:
        title = "???"
        warnings.warn(title)
        
    return title.strip()

class NormSpider(scrapy.Spider):
    name = 'Kommunen'
    forceSource = ""
    start_urls = ["https://app.draftr.de/sat-docs/kommunenStart.txt"]
    dupeDict = {}
    firstDomainVisit = {}
    noFollow = False
    redisDb.set("monitor:sat:status:kommunal:scapystartat",time.time())
    pbar = tqdm(total=1000)

    def __init__(self, *args, **kwargs):
        url = kwargs.pop('customStartUrl', "") 
        if url:
            self.start_urls = [url]
            self.noFollow = True
        self.logger.info(self.start_urls)
        super(NormSpider, self).__init__(*args, **kwargs)



    def parse(self, response): 

        uri = urlparse(response.request.url)
        if not self.firstDomainVisit.get(uri.netloc): self.firstDomainVisit[uri.netloc] = time.time()
        if time.time() - self.firstDomainVisit[uri.netloc] > maxTimePerDomain:
            print()#
            self.logger.info("time limit for %s exceeded",  uri.netloc)
            return

        
        pdfIframe = response.xpath("//iframe[contains(@src,'.PDF') or contains(@src,'.pdf')]")
        if pdfIframe:
            yield {
                'Link': response.urljoin(pdfIframe.css('::attr(src)').get()),
            }
            return

        if "kommunenStart.txt" in response.request.url:
            lines = response.body_as_unicode().split("\n")
            for i,lineTxt in enumerate(lines):
                
                m = re.search("^(?P<name>.*)[\t\s]+(?P<url>https?://.*)([\t\s]|$)",lineTxt)
                if m : #and "Kehl" in lineTxt
                    dynamicM = re.search("\[(?P<start>\d+)-(?P<stop>\d+)\]",lineTxt)
                    if dynamicM:
                        for i in range(int(dynamicM.group("start")),int(dynamicM.group("stop"))):
                            if not "wikipedia" in m.group("url"):
                                request = scrapy.Request(url=m.group("url").replace(dynamicM.group(0),str(i)),  meta={'municipalityName': m.group("name"),'progress':i/len(lines)})
                                yield request
                    elif not "wikipedia" in m.group("url"):
                        request = scrapy.Request(url=m.group("url"),  meta={'municipalityName': m.group("name"),'depth':0})
                        yield request

        else:

            negaItems = response.css(",".join(definatelyOutSelector)).getall()
            if not negaItems: negaItems = []

            for item in response.xpath("//a[contains(.,'"+("') or contains(., '".join(probablyInKeyword)+"')")+" or contains(@href,'"+("') or contains(@href, '".join(probablyInKeyword)+"')")+"]"):
                itemText = cleanTitle(item.xpath("string()").get().strip()) or re.sub("<.*?>","",item.get()).strip()
                if len(itemText) <= 12:
                    itemText = item.xpath("..").xpath("string()").get()
                itemLink = item.css('::attr(href)').get()
                if item.get() not in negaItems and not any([keyword in itemText for keyword in definatelyOutKeyword]) and any([keyword in itemText for keyword in probablyInKeyword]):
                    l = response.urljoin(itemLink)
                    if not self.dupeDict.get(l):
                        self.dupeDict[l] = True
                        yield {
                            'Quelle': (response.meta.get("municipalityName")  or self.forceSource).strip(),
                            'Titel': itemText,
                            'Link': l,
                        }

            for item in response.xpath("//a[contains(.,'"+("') or contains(., '".join(maybeInKeyword)+"')")+" or contains(@title,'"+("') or contains(@title, '".join(maybeInKeyword)+"')")+" or contains(@href,'"+("') or contains(@href, '".join(maybeInKeyword)+"')")+"]"):
                searchMarker = item.get()
                if not searchMarker in response.body_as_unicode():
                    searchMarker = item.css('::attr(href)').get()
                pos = response.body_as_unicode().index(searchMarker)
                searchIn = response.body_as_unicode()[pos-300:pos]
                titleMatch = list(re.finditer(titleRegex,searchIn))
                # print("***************\n",searchIn,"\n***************\n",titleMatch)
                if not len(titleMatch):
                    titleMatch = list(re.finditer(titleRegex,searchIn))
                if not len(titleMatch):
                    pos += len(searchMarker)
                    titleMatch = list(re.finditer(titleRegex,response.body_as_unicode()[pos:pos+300]))
                if not len(titleMatch):
                    titleMatch = list(re.finditer(titleRegex,response.body_as_unicode()[pos:pos+3000]))

                if item.get() not in negaItems:
                    if len(titleMatch):

                        titleMatch=titleMatch[-1]
                        # print(titleMatch)
                        l = response.urljoin(item.css('::attr(href)').get())
                        if not self.dupeDict.get(l):
                            self.dupeDict[l] = True
                            yield {
                                'Quelle': (response.meta.get("municipalityName") or self.forceSource).strip(),
                                'Titel': cleanTitle(titleMatch.group("title")),
                                'Link': l,
                            }

            # pagination
            if not self.noFollow:
                for item in response.xpath("//a[contains(.,'ächste Seite')  or contains(@title,'Weiter') or contains(@title,'weiter') or contains(.,'alphabetisch') or contains(@rel,'next') or contains(@class,'next')]"):
                    if int(response.meta.get("depth",0)) < 20:
                        nextUrl = response.urljoin(item.css('::attr(href)').get())
                        uri = urlparse(nextUrl)

                        if not self.firstDomainVisit.get(uri.netloc): self.firstDomainVisit[uri.netloc] = time.time()
                        if time.time() - self.firstDomainVisit[uri.netloc] > maxTimePerDomain:
                            self.logger.info("time limit for %s exceeded",  uri.netloc)
                            return

                        elif not "wikipedia" in nextUrl:

                            # print("time spent on ",uri.netloc,":",int(time.time() - self.firstDomainVisit[uri.netloc]),"sec")
                            

                            request = scrapy.Request(url=nextUrl,  meta={'municipalityName':  response.meta.get("municipalityName"),'depth': int(response.meta.get("depth",0))+1})
                            yield request
                            
            if response.meta.get("progress"):
                redisDb.set("monitor:sat:status:kommunal:scapyprogress",response.meta.get("progress"))
                pbar.update(response.meta.get("progress")*1000)
                if response.meta.get("progress") > .999:
                    redisDb.set("monitor:sat:status:kommunal:scapystopat",time.time())