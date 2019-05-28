# -*- coding: utf-8 -*-
import logging

from elasticsearch import Elasticsearch

from .config import (ES_HOST, ES_INDEX, ES_MAPPING, ES_PORT, ES_SECRET,
                     ES_USERNAME)


class ImdbScraperPipeline(object):
    """ Do nothing for the moment """

    def process_item(self, item, spider):
        return item


class ElasticSearchPipeline(object):
    """ Save all the stuff to elasticsearch, babe """
    log = None
    es = None
    index = None
    mapping = None

    def __init__(self):
        self.log = logging.getLogger('elasticsearch.trace')
        self.log.addHandler(logging.NullHandler())
        self.es = Elasticsearch(
            [ES_HOST],
            http_auth=(str(ES_USERNAME), str(ES_SECRET)),
            port=ES_PORT,
        )
        self.index = ES_INDEX
        self.mapping = ES_MAPPING

        try:
            # check if server is available
            self.es.ping()

            # raise logging level due to indices.exists() habit of
            # logging a warning if an index doesn't exist.
            es_log = logging.getLogger('elasticsearch')
            es_level = es_log.getEffectiveLevel()
            es_log.setLevel('ERROR')

            # check if the necessary indices exist and create them if needed
            if not self.es.indices.exists(self.index):
                self.es.indices.create(index=self.index, ignore=[400, 404])
                self.es.indices.put_mapping(
                    index=self.index, doc_type='article', body=self.mapping)
            self.running = True

            # restore previous logging level
            es_log.setLevel(es_level)

        except Exception as error:
            self.running = False
            self.log.error("Failed to connect to Elasticsearch, this module "
                           "will be deactivated. "
                           "Please check if the database is running and "
                           "the config is correct: %s" % error)

    def extract_data(self, key, value):
        if key == 'votes':
            return int(value.replace(',', ''))
        elif key in ['countries', 'languages', 'genre', 'actors', 'directors']:
            return [{'name': v} for v in value]
        return value

    def process_item(self, item, spider):
        if self.running:
            # check if existing
            request = self.es.search(
                index=self.index,
                body={'query': {
                    'match': {
                        'url': item['url']
                    }
                }})
            if request['hits']['total'] == 0:
                self.log.info("Saving to Elasticsearch: %s" % item['url'])
                data = {k: self.extract_data(k, v) for k, v in item.items()}
                self.es.index(index=self.index, doc_type='article', body=data)

        return item
