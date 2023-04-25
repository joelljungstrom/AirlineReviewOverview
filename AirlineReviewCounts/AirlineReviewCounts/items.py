# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirlinereviewcountsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    AirlineName = scrapy.Field()
    Reviews = scrapy.Field()
    Slug = scrapy.Field()
    pass
