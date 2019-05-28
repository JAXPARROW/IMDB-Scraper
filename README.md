# IMDB Scraper

![](https://img.shields.io/github/license/dojutsu-user/IMDB-Scraper.svg?style=for-the-badge)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg?style=for-the-badge)](https://GitHub.com/otto-torino/IMDB-Scraper/graphs/contributors/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/dojutsu-user/IMDB-Scraper/pulls)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Overview

> This is a fork of the original [IMDB Scraper](https://github.com/dojutsu-user/IMDB-Scraper) repo.

This is a [Scrapy](https://github.com/scrapy/scrapy) project which can be used to crawl [IMDB](https://www.imdb.com/) website to scrape movies' information and then store the data in `json` format or/and save them in an elasticsearch index.

## Configuration

### Search query

You can change the starting page of the crawler in the file `imdb_scraper/spiders/movie.py` by changing the `SEARCH_QUERY` variable. You can get your own query from here: [imdb.com/search/title](https://www.imdb.com/search/title). Copy the generated URL and paste it in place of default url. By default:
```python3
SEARCH_QUERY = (
    'https://www.imdb.com/search/title?'
    'title_type=feature&'
    'user_rating=1.0,10.0&'
    'countries=us&'
    'languages=en&'
    'count=250&'
    'view=simple'
)
```

### ElasticSearch

You can store scraped info in elasticsearch, just enable the pipeline in the `ITEM_PIPELINE` dict in `settings.py` (enabled by default) and set the following env vars:

```ES_HOST, ES_PORT, ES_USERNAME, ES_SECRET, ES_INDEX```

### JSON Output

If you enable the `FEED_URI` and `FEED_FORMAT` settings in `settings.py`, data will be stored in `json` file named `movie.json` located at `IMDB-Scraper/imdb-scraper/data/movie.json`.

## Getting started

1. Clone the repo and navigate into `IMDB-Scraper` folder.
```
$ git clone https://github.com/dojutsu-user/IMDB-Scraper.git
$ cd IMDB-Scraper/
```
2. Create and activate a virtual environment.
```
(IMDB-Scraper) $ pipenv shell
```
3. Install all dependencies.
```
(IMDB-Scraper) $ pipenv install
```
4. Navigate into `imdb_scraper` folder.
```
(IMDB-Scraper) $ cd imdb_scraper/
```
5. Start the crawler.
```
(IMDB-Scraper) $ scrapy crawl movie
```

## Disclaimer

The project and the obtained dataset is intended only for educational purpose. It is completely open source and has no value intentions to commercialise complete or any part of the same. The developer is on no part the owner of any resources used and does not claim to hold the permissions to use the project.
