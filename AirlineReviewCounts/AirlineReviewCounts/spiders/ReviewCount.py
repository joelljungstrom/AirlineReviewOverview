# Import library
import scrapy
import re
from AirlineReviewCounts.items import AirlinereviewcountsItem


# Create Spider class
class ReviewCountCrawler(scrapy.Spider):
    # Name of spider
    name = 'ReviewCountCrawler'
    # Website to scrape
    allowed_urls = ['https://www.airlinequality.com/']
    start_urls = [
        'https://www.airlinequality.com/review-pages/a-z-airline-reviews/airline-review-ratings/'
    ]

    # Parses the website
    def parse(self, response):
        counts = response.xpath('//*/div[@class="aggregateRow clearfix"]')
        for count in counts:
            # Airline Name
            try:
                name = count.xpath('.//div[@class="aggregateColumn aggregateColumn_two"]/a/text()').extract_first()
            except:
                name = ''

            # Slug
            try:
                link = count.xpath('.//div[@class="aggregateColumn aggregateColumn_two"]/a/@href')
                slug = re.search(r'/airline-reviews/(.+?)$', link.get()).group(1)
            except:
                slug = ''

            # Number of Reviews
            try:
                count = count.xpath('.//div[@class="aggregateColumn aggregateColumn_four"]/text()').extract_first()
            except:
                count = ''

            item = AirlinereviewcountsItem()
            item['AirlineName'] = name
            item['Slug'] = slug
            item['Reviews'] = count

            yield item
        pass