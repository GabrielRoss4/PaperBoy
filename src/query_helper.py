'''
Query object that acts as an intermediate between a user input
query and news api query format.
'''

import config as cfg

class NewsQueryHelper(object):
    def __init__(self, query_name=None, query=None, sources=None, 
    category=None, country=None, language=None, article_limit=10):


        if sources is not None and (country is not None or category is not None):
            raise ValueError("Sources cannot be selected with country or with category")

        self.query_name = query_name
        self.query = query
        self.sources = ",".join(sources) if sources else None
        self.category = category
        self.country = country
        self.language = language
        self.article_limit = article_limit

    def __repr__(self):
        return f'''NewsQueryHelper(query_name={self.query_name}, query={self.query}, sources={self.sources}, 
        category={self.category}, country={self.country}, language={self.language}, article_limit={self.article_limit}'''


class LocalQueryHelper(NewsQueryHelper):
    def __init__(self, city, state, zipcode, country, units=None):
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        self.units = units
        super().__init__(
            query_name=f"{self.city}, {self.state}",
            query=self.city,
            country=self.country,
            article_limit=3)

