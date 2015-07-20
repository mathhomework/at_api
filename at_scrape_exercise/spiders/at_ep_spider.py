from scrapy import Spider, Selector

from at_api.models import Episode, Character
import django
import re
from datetime import date
django.setup()


def convert_to_utc(_str):
        months = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        print "++++++++++++++++"
        print _str
        date_list = _str.replace(",", "").split(" ")
        return date(int(date_list[2]), months[date_list[0]], int(re.findall(r'\d+', date_list[1])[0]))


class AT_Episode_Spider(Spider):
    name = "ep"
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
        "http://adventuretime.wikia.com/wiki/List_of_episodes"
    ]

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath("//table[@class='wikitable']/tr[position()>1]/td[2]/a/@href").extract()
        with open('episodes.txt', 'a') as f:
            for link in links:
                f.write("http://adventuretime.wikia.com{}\n".format(link))
            f.close()


class AT_Episode_Detail_Spider(Spider):
    name = "ep_detail"
    episodes = open("episodes.txt")
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
    #     "http://adventuretime.wikia.com/wiki/Animated_short",
    #     "http://adventuretime.wikia.com/wiki/Slumber_Party_Panic",
    #     "http://adventuretime.wikia.com/wiki/Jermaine_(episode)",
    #     "http://adventuretime.wikia.com/wiki/Loyalty_to_the_King",
    #     "http://adventuretime.wikia.com/wiki/James_(episode)",
    #     "http://adventuretime.wikia.com/wiki/Another_Five_More_Short_Graybles",
    #     "http://adventuretime.wikia.com/wiki/It_Came_from_the_Nightosphere",
    #     "http://adventuretime.wikia.com/wiki/Wizards_Only,_Fools",
        "http://adventuretime.wikia.com/wiki/Hot_Diggity_Doom",
    ]
    # start_urls = [url.strip() for url in episodes.readlines()]

    def parse(self, response):
        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        title = sel.xpath("//header[@id='WikiaPageHeader']//h1/text()").extract()[0].strip()
        print "===================NAME======================"
        title = title.replace(" (episode)", "")
        print title

        season_episode_str = data.xpath("normalize-space(tr[2]/td[1]/text())").extract()[0]
        season_id = season_episode_str.split("Season ", 1)[1].rpartition(",")[0]
        episode_id = season_episode_str.split("episode ", 1)[1]
        # this title_card is too small.
        title_card = data.xpath("tr[2]/td/div/div/a/@href").extract()[0]
        # this doesn't work for some things. Scraping for this has moved to ep_detail_2
        # production_code = data.xpath("normalize-space(tr[3]/td/text())").extract()[0]
        e, e_created = Episode.objects.get_or_create(title=title)
        e.season_id = season_id
        e.episode_id = episode_id
        # e.production_code = production_code
        e.save()

        # Note for characters. Towards the end, there is /a[1].The [1] is there because I only want the first link.
        # Sometimes something like Hunson Abadeer (name not revealed until "Return to the Nightosphere") will appear.
        # Both Hunson Abadeer and Return ... will be a tags, but Return is obviously not a character.
        characters = sel.xpath("//div[@id='mw-content-text']/*[self::h3 or self::h2][span[@id='Major_characters' or @id='Minor_characters']]/following-sibling::*[1]/li/a[1]/text() | "
                               "//div[@id='mw-content-text']/*[self::h3 or self::h2][span[@id='Major_characters' or @id='Minor_characters']]/following-sibling::*[1]/li/ul/li/a[1]/text()").extract()
        for char in characters:
            c, c_created = Character.objects.get_or_create(name=char)
            e.characters.add(c)
        print title_card
        print characters


class AT_Episode_Detail_Spider_2(Spider):
    # this scraper has better title card images, viewer information, and descriptions for Episodes.
    name = "ep_detail_2"
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
        "http://adventuretime.wikia.com/wiki/List_of_episodes"
    ]

    def parse(self, response):
        sel = Selector(response)
        title_cards = sel.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[1]/a[@class='image image-thumbnail']/@href").extract()
        titles = sel.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[2]/a/text()").extract()
        viewers = sel.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[3]/text()").extract()
        viewers = [el.strip() for el in viewers if el != "\n"]
        production_codes = sel.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[4]/text()").extract()
        production_codes = [el.strip() for el in production_codes if el != "\n"]

        air_dates = []
        air_dates_raw = sel.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[5]/text()").extract()
        # air_dates_raw = [x for x in air_dates_raw if x.strip()]
        for el in air_dates_raw:
            if el.strip():
                el = el.strip()
                if el.startswith("Official"):
                    el = el.replace("Official: ", "")
                if el.endswith("(US)"):
                    el = el.replace(" (US)", "")
                if el.startswith("Sneak") or el == "\n" or el.endswith("(Canada)"):
                    pass
                else:
                    air_dates.append(el)
        print air_dates
        air_dates_utc = [convert_to_utc(d) for d in air_dates]
        links = sel.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[2]/a/@href").extract()
        links = ["http://adventuretime.wikia.com"+link for link in links]
        print air_dates_utc
        zipped_data = zip(titles, title_cards, viewers, links, air_dates, air_dates_utc, production_codes)

        for ep in zipped_data:
            print ep[0]
            print ep[2]
            e, e_created = Episode.objects.get_or_create(title=ep[0])
            e.title_card = ep[1]
            e.viewers = ep[2]
            e.link = ep[3]
            e.air_date = ep[4]
            e.air_date_utc = ep[5]
            e.production_code = ep[6]
            e.save()

        # Pre SO
        # description = sel.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[@colspan='5']//text()").extract()
        # print description

        # GOOD
        # description = [" ".join(row.xpath(".//text()").extract())
        #                for row in response.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[@colspan]")]
        # print description

        # Messing around
        # for row in response.xpath("//table[@class='wikitable'][position()>2]/tr[position()>1]/td[@colspan]"):
        #     print row.xpath(".//text()").extract()