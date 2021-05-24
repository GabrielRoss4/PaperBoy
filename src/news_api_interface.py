'''
Interfaces with the news api and returns formatted results
'''

from newsapi import NewsApiClient
from traceback import print_exc
import config as cfg


class NewsApiInterface(object):
    def __init__(self, api_key=cfg.NEWS_API_KEY):
        self.api_key = api_key
        self.api_client = NewsApiClient(api_key=self.api_key)

    def get_top_headlines(self, query):
        try:
            response = self.api_client.get_top_headlines(
                q=query.query,
                sources=query.sources,
                category=query.category,
                language=query.language,
                country=query.country,
                page_size=query.article_limit)
            print("Connected to news API.\nQuery status: "+response["status"])
            return self.format_headlines(response)

        except:
            print("Failed to connect to news API")
            print_exc()
            return -1

    def format_headlines(self, raw_api_response):
        formatted_response = []
        for article in raw_api_response["articles"]:
            formatted_response.append({
                "source":article["source"]["name"],
                "author":article["author"],
                "title":article["title"],
                "description":article["description"],
                "url":article["url"]})
        return formatted_response

#   TEST THE API TO SEE WHAT HAPPENS IF I GIVE IT A FIELD WHOSE VALUE IS NONE