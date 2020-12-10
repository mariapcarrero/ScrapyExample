# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    summary = scrapy.Field()
    genre = scrapy.Field()
    movieRating = scrapy.Field()
    runtime = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    cast = scrapy.Field()

class CastItem(scrapy.Item):
    name = scrapy.Field()
    character = scrapy.Field()