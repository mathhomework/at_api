from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import Spider
import re

from at_api.models import Character, Occupation, Episode, Species
import django
django.setup()


class AT_Char_Spider(Spider):
    name = "char"
    allowed_domains = ["adventuretime.wikia.com"]
    # Not necessary, but f you want this super automated in the future, and you need a scraper for these start_urls,
    # you could make another scraper that adds to a global variable that stores next page links coming out of each page
    # for something more complicated, try selenium?
    # http://stackoverflow.com/questions/17975471/selenium-with-scrapy-for-dynamic-page
    start_urls = [
        "http://adventuretime.wikia.com/wiki/Category:Characters",
        "http://adventuretime.wikia.com/wiki/Category:Characters?pagefrom=Donny+%28character%29#mw-pages",
        "http://adventuretime.wikia.com/wiki/Category:Characters?pagefrom=Jungle+Princess#mw-pages",
        "http://adventuretime.wikia.com/wiki/Category:Characters?pagefrom=Rock+Giant#mw-pages"

    ]

    def parse(self, response):
        sel = Selector(response)
        data = sel.xpath("(//div[@class='mw-content-ltr'])[3]/table/tr/td/ul/li/a")
        with open('characters.txt', 'a') as f:
            for datum in data:
                x = datum.xpath("text()").extract()
                if "User" not in x[0]:
                    f.write("http://adventuretime.wikia.com{}\n".format(datum.xpath("@href").extract()[0]))
            f.close()


class AT_Char_Spider_Detail(Spider):
    name = "char_detail"
    allowed_domains = ["adventuretime.wikia.com"]
    characters = open("characters.txt")
    # start_urls = [
        # "http://adventuretime.wikia.com/wiki/Doctor_Princess",
        # "http://adventuretime.wikia.com/wiki/Finn",
        # "http://adventuretime.wikia.com/wiki/T.V.",
        # "http://adventuretime.wikia.com/wiki/Jay_%26_Bonnie",
        # "http://adventuretime.wikia.com/wiki/Booger",
        # "http://adventuretime.wikia.com/wiki/Marceline",
        # "http://adventuretime.wikia.com/wiki/Breakfast_Princess",
        # "http://adventuretime.wikia.com/wiki/Abe_Lincoln",
        # "http://adventuretime.wikia.com/wiki/Ice_King",
        # "http://adventuretime.wikia.com/wiki/Ricardio",
        # "http://adventuretime.wikia.com/wiki/Mr._Pig",
        # "http://adventuretime.wikia.com/wiki/Earl_of_Lemongrab",
        # "http://adventuretime.wikia.com/wiki/Princess_Bubblegum",
        # "http://adventuretime.wikia.com/wiki/Lich_King",
        # "http://adventuretime.wikia.com/wiki/Greed_Lard",
        # "http://adventuretime.wikia.com/wiki/Jake_Jr.",
    # ]
    start_urls = [url.strip() for url in characters.readlines()]


    def parse(self, response):
        # Notes: Species should be updated to contain notes. body_appearances for Episode relation doesn't work properly
        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        # categories = data.xpath("tr[position()>2]/td/b/text()").extract()
        name = sel.xpath("//header[@id='WikiaPageHeader']//h1/text()").extract()[0]
        print(name)
        c, c_created = Character.objects.get_or_create(name=name)
        try:
            full_name = data.xpath("normalize-space(tr[td/b/text()='Name']/td[position()>1]/text())").extract()[0]
            print(full_name)
            c.full_name = full_name
        except IndexError:
            pass
        print("*************SPECIES************")
        # the species_ list below will split 1/4 Rainicorn (Rainicorn is <a>) into 1/4 and Rainicorn
        # species_list = data.xpath("tr/td/a[../../td/b/text()='Species']/text()|tr[td/b/text()='Species']/td/text()[normalize-space()]").extract()
        # species = [x.strip() for x in species_list]

        # The below will have to do for now... since it does combine 1/4 Rainicorn into one species for Jake. Jr.
        # However, Ice King's Human-turned-Wizard becomes Human -turned- Wizard.
        # Ultimately... I think it can be solved by writing better xpath, but I can't find a good solution right now.
        # The current parsing of the xpath generated list isn't too good either... much concatenation
        species_list = data.xpath("tr/td/a[../../td/b/text()='Species']/text()|tr[td/b/text()='Species']/td/text()|//br").extract()
        species = []
        holder = ""
        for thing in species_list:
            if thing == "<br>":
                if holder != "":
                    species.append(holder.strip())
                holder = ""
            else:
                space = " "
                if holder == "":
                    space = ""
                holder += thing + space
        print(species_list)
        for name in species:
            print(name)

            s, s_created = Species.objects.get_or_create(name=name)

            c.species.add(s)
            print(c.species.all())

        # returns [u'Vampire', u'Demon']
        print("*************END SPECIES**********")
        # the occupation below does not take into account a tags... so Marceline's Henchmen would just be something like 's henchmen
        # occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]/text()").extract()
        # occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]/descendant::text()").extract()
        # this is more specific than the below because it does not matter where the extra space after occupation is
        # occupation = data.xpath("tr[td/b/text()='Occupation ']/td[position()>1]/text()").extract()
        try:
            # BTW currently occupation does not take into account the episode in which character is associated
            occupation_html = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]").extract()[0]
            occu = occupation_html.split("<br>")
            print("***********OCCUPATION******************")
            for x in occu:
                # replace the re.sub below with just x if you want to include all the (formerly in "Henchman") etc.
                title = re.sub('<[^>]*>', '', re.sub('\(.*?\)', '', x)).strip()
                print(title)
                job, job_created = Occupation.objects.get_or_create(title=title)
                c.occupation.add(job)

            print("**********END OCCUPATION**************")
        except IndexError:
            pass
        try:
            sex = data.xpath("normalize-space(tr[td/b/text()='Sex']/td[position()>1]/text())").extract()[0]
            print(sex)
            c.sex = sex
        except IndexError:
            pass

        print("************relatives**************")
        # relatives = data.xpath("tr[td/b/text()='Relatives']/td[position()>1]/a/text()").extract()
        relatives = data.xpath("tr[td/b/text()='Relatives']/td[position()>1]/descendant::a/text()[not(ancestor::small)]").extract()
        for relative in relatives:
            r, r_created = Character.objects.get_or_create(name=relative)
            print(r)
            c.relatives_many.add(r)

        link = response.request.url
        print(relatives)
        print(link)
        c.link = link
        # print("*************appearances*********")
        # This version makes sure that if a minor character is being scraped, it will return an empty list if there's no Episodes appearances section
        body_appearances = sel.xpath("//div[@id='mw-content-text']/*[self::h3 or self::h2][span[@id='Major_appearances' or @id='Minor_appearances' or @id='Episode_appearances']]/following-sibling::*[1]/li/a/text()").extract()
        sidebar_introduced = data.xpath("normalize-space(tr[td/b/text()='Introduced in']/td[position()>1]/a/text())").extract()
        appearances = body_appearances or sidebar_introduced

        print("BODY_APPEAR")
        print(body_appearances)
        print("SIDEBAR APPEAR")
        print(sidebar_introduced)
        print("FINAL OUTPUT")
        print(appearances)

        for title in appearances:
            e, e_created = Episode.objects.get_or_create(title=title)
            c.episode.add(e)
        try:
            image = data.xpath("tr/td/a[@class='image image-thumbnail']/@href").extract()[0]
            # print("***********IMAGE********")
            c.image = image
        except IndexError:
            pass
        c.save()


def char_detail():
    process = CrawlerProcess()
    process.crawl(AT_Char_Spider_Detail)
    process.start()

