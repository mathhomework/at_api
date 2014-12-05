# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class AtScrapeExerciseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AT_Char_Item(Item):
    name = Field()
    link = Field()

# exceptions to be aware of
# missing "Episodes featured" bio means you
# need to check "Introduced in" or "Latest appearance"
# Exclude "Mentioned In" for "Episodes featured"



class AT_Char_Detail_Item(Item):
    name = Field()
    sex = Field()
    species = Field()
    link = Field()
    appearances = Field()
    image = Field()
    relatives = Field()