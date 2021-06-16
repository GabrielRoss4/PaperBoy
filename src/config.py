import os
from query_helper import NewsQueryHelper, LocalQueryHelper

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

UNITS = "imperial"
LANGUAGE = "en"

EXPORT_TO_JSON = True

LOCAL_QUERIES = [
    LocalQueryHelper(
        city="Boston",
        state="MA",
        zipcode="02101",
        country="us",
        units=UNITS),
    LocalQueryHelper(
        city="Seattle",
        state="WA",
        zipcode="98122",
        country="us",
        units=UNITS),
        ]

# All sources can be found programmatically using https://newsapi.org/docs/endpoints/sources
NEWS_SOURCES = [
"abc-news",
"al-jazeera-english",
"ars-technica",
"breitbart-news",
"business-insider",
"cbs-news",
"cnn",
"crypto-coins-news",
"fox-news",
"google-news",
"hacker-news",
"medical-news-today",
"msnbc",
"national-geographic",
"nbc-news",
"new-scientist",
"next-big-future",
"reuters",
"techcrunch",
"the-american-conservative",
"the-verge",
"the-wall-street-journal",
"usa-today"]

NEWS_QUERIES = [
    NewsQueryHelper(
        query_name="All",
        query=None,
        sources=NEWS_SOURCES,
        category=None,
        country=None,
        language=LANGUAGE,
        article_limit=20
    )
]