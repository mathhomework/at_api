from scrapy import Spider, Selector

from at_api.models import Episode
import django
django.setup()


class AT_Episode_Detail_Spider(Spider):
    name = "ep_detail"
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
        "http://adventuretime.wikia.com/wiki/Animated_short",
        "http://adventuretime.wikia.com/wiki/Slumber_Party_Panic",
        "http://adventuretime.wikia.com/wiki/Jermaine_(episode)",
    ]
    # start_urls = [url.strip() for url in characters.readlines()]


    def parse(self, response):
        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        name = sel.xpath("//header[@id='WikiaPageHeader']//h1/text()").extract()[0].strip()
        print "===================NAME======================"
        name = name.replace(" (episode)", "")
        print name

        season_episode_str = data.xpath("normalize-space(tr[2]/td[1]/text())").extract()[0]
        season_id = season_episode_str.split("Season ", 1)[1].rpartition(",")[0]
        episode_id = season_episode_str.split("episode ", 1)[1]
        
        try:
            pass
        except IndexError:
            pass
