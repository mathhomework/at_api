from scrapy.selector import Selector
from scrapy.spider import Spider
from at_scrape_exercise.items import AT_Char_Item, AT_Char_Detail_Item
import re

from at_api.models import Character, Occupation, Episode, Species


class AT_Char_Spider(Spider):
    name = "char"
    allowed_domains = ["adventuretime.wikia.com"]
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
    start_urls = [
        # "http://adventuretime.wikia.com/wiki/Doctor_Princess",
        # "http://adventuretime.wikia.com/wiki/Finn",
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
    ]
    start_urls = [url.strip() for url in characters.readlines()]


    def parse(self, response):

        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        # categories = data.xpath("tr[position()>2]/td/b/text()").extract()
        name = sel.xpath("//header[@id='WikiaPageHeader']/h1/text()").extract()[0]
        c, c_created = Character.objects.get_or_create(name=name)
        try:
            full_name = data.xpath("normalize-space(tr[td/b/text()='Name']/td[position()>1]/text())").extract()[0]
            c.full_name = full_name
        except IndexError:
            pass

        species_list = data.xpath("tr/td/a[../../td/b/text()='Species']/text()|tr[td/b/text()='Species']/td/text()[normalize-space()]").extract()
        species = [x.strip() for x in species_list]
        for name in species:
            s, s_created = Species.objects.get_or_create(name=name)
            c.species.add(s)

        # returns [u'Vampire', u'Demon']
        print "*************SPECIES**********"
        print species
        # the occupation below does not take into account a tags... so Marceline's Henchmen would just be something like 's henchmen
        # occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]/text()").extract()
        # occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]/descendant::text()").extract()
        # this is more specific than the below because it does not matter where the extra space after occupation is
        # occupation = data.xpath("tr[td/b/text()='Occupation ']/td[position()>1]/text()").extract()
        try:
            occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]").extract()[0]

            print "***********OCCUPATION******************"
            for x in str(occupation).split("<br>"):
                title = re.sub('<[^>]*>', '', re.sub('\(.*?\)', '', x)).strip().rstrip(",")
                job, job_created = Occupation.objects.get_or_create(title=title, character=c)

            print "**********END OCCUPATION**************"
        except IndexError:
            pass
        try:
            sex = data.xpath("normalize-space(tr[td/b/text()='Sex']/td[position()>1]/text())").extract()[0]
            c.sex = sex
        except IndexError:
            pass

        # print "************relatives**************"
        # relatives = data.xpath("tr[td/b/text()='Relatives']/td[position()>1]/a/text()").extract()
        relatives = data.xpath("tr[td/b/text()='Relatives']/td[position()>1]/descendant::a/text()[not(ancestor::small)]").extract()
        for relative in relatives:
            r, r_created = Character.objects.get_or_create(name=relative)
            c.relatives_many.add(r)

        link = response.request.url
        print link
        c.link = link
        # print "*************appearances*********"
        # This version makes sure that if a minor character is being scraped, it will return an empty list if there's no Episodes appearances section
        body_appearances = sel.xpath("//div[@id='mw-content-text']/*[self::h3 or self::h2][span[@id='Major_appearances' or @id='Minor_appearances' or @id='Episode_appearances']]/following-sibling::*[1]/li/a/text()").extract()
        sidebar_introduced = data.xpath("normalize-space(tr[td/b/text()='Introduced in']/td[position()>1]/a/text())").extract()
        appearances = body_appearances or sidebar_introduced
        print appearances

        for title in appearances:
            e, e_created = Episode.objects.get_or_create(title=title)
            c.appearance.add(e)
        try:
            image = data.xpath("tr/td/a[@class='image image-thumbnail']/@href").extract()[0]
            # print "***********IMAGE********"
            c.image = image
        except IndexError:
            pass
        c.save()

