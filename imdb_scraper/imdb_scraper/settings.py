# -*- coding: utf-8 -*-

BOT_NAME = 'imdb_scraper'

SPIDER_MODULES = ['imdb_scraper.spiders']
NEWSPIDER_MODULE = 'imdb_scraper.spiders'

# Saving the output in json format
# FEED_URI = 'data/%(name)s.json'
# FEED_FORMAT = 'json'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Pipeline activation
# Syntax: '<relative location>.<Pipeline name>': <Order of execution from 0-1000>
ITEM_PIPELINES = {
    'imdb_scraper.pipelines.ImdbScraperPipeline': 100,
    'imdb_scraper.pipelines.ElasticSearchPipeline': 200,
}
