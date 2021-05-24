

import config as cfg
from news_api_interface import NewsApiInterface
from weather_api_interface import WeatherApiInterface


def make_local_query(cfg, NewsApiInterface, WeatherApiInterface):
    for query in cfg.LOCAL_QUERIES:
        weather = WeatherApiInterface().get_weather(query)
        news = NewsApiInterface().get_top_headlines(query)
        print(f'''
        Local news and weather for {query.city}, {query.state}:
        It is currently {weather["weather"]}.
        The high for the day is {weather["temp_high"]}, the low for the day is {weather["temp_low"]}.
        It is currently {weather["temp_cur"]} and it feels like {weather["temp_feels_like"]}. All in Fahrenheit
        
        Top news stories:''')
        for article in news:
            print(article)

def make_national_query(cfg, NewsApiInterface):
    # Instead of formatting the articles here I can have a method
    # in the api interface class that formats it how I want it here.
    for query in cfg.NEWS_QUERIES:
        news = NewsApiInterface().get_top_headlines(query)
        print("\nTop national news stories:")
        for article in news:
            print(f'''
            Title: {article["title"]}
            Source: {article["source"]}
            Author: {article["author"]}
            Description: {article["description"]}
            URL: {article["url"]}
            ''')

def main(cfg, NewsApiInterface, WeatherApiInterface):
    make_local_query(cfg, NewsApiInterface, WeatherApiInterface)
    make_national_query(cfg, NewsApiInterface)

if __name__ == "__main__":
    main(cfg, NewsApiInterface, WeatherApiInterface)

