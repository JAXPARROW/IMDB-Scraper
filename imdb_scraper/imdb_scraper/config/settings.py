import os

from dotenv import load_dotenv

load_dotenv()

# Sources
SOURCES_PATH = os.path.join(os.path.dirname(__file__), 'queries.json')

# Elastic Search
ES_HOST = os.getenv('ES_HOST', '127.0.0.1')
ES_PORT = os.getenv('ES_PORT', 9200)
ES_INDEX = os.getenv('ES_INDEX', 'imdb')
ES_USERNAME = os.getenv('ES_USERNAME', 'root')
ES_SECRET = os.getenv('ES_SECRET', 'password')

ES_MAPPING = {
    "properties": {
        "url": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "title": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "rating": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "year": {
            "type": "integer",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "user_rating": {
            "type": "float",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "votes": {
            "type": "long"
        },
        "metascore": {
            "type": "long",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "img_url": {
            "type": "text"
        },
        "countries": {
            "type": "nested",
            "properties": {
                "name": {"type": "keyword"}
            }
        },
        "languages": {
            "type": "nested",
            "properties": {
                "name": {"type": "keyword"}
            }
        },
        "actors": {
            "type": "nested",
            "properties": {
                "name": {"type": "keyword"}
            }
        },
        "genre": {
            "type": "nested",
            "properties": {
                "name": {"type": "keyword"}
            }
        },
        "tagline": {
            "type": "text"
        },
        "description": {
            "type": "text"
        },
        "storyline": {
            "type": "text"
        },
        "directors": {
            "type": "nested",
            "properties": {
                "name": {"type": "keyword"}
            }
        },
        "runtime": {
            "type": "text"
        },
        "date_download": {
            "type": "date",
            "format": "yyyy-MM-dd HH:mm:ss"
        }
    }
}
