import config as cfg
from news_api_interface import NewsApiInterface
from weather_api_interface import WeatherApiInterface


def make_local_query(cfg, NewsApiInterface, WeatherApiInterface):
    local_json_obj = dict()
    for query in cfg.LOCAL_QUERIES:
        weather = WeatherApiInterface().get_weather(query)
        news = NewsApiInterface().get_top_headlines(query)

        locale = f"{query.city}, {query.state}"
        local_json_obj[locale] = {
            "weather":weather,
            "news":news}
        print(f'''
        Local news and weather for {query.city}, {query.state}:
        It is currently {weather["weather"]}.
        The high for the day is {weather["temp_high"]}, the low for the day is {weather["temp_low"]}.
        It is currently {weather["temp_cur"]} and it feels like {weather["temp_feels_like"]}. All in Fahrenheit
        
        Top news stories:''')
        for article in news:
            print(article)
    return local_json_obj


def make_national_query(cfg, NewsApiInterface):
    # Instead of formatting the articles here I can have a method
    # in the api interface class that formats it how I want it here.
    national_json_obj = dict()
    for query in cfg.NEWS_QUERIES:
        news = NewsApiInterface().get_top_headlines(query)
        national_json_obj[query.query_name] = news
        print("\nTop national news stories:")
        for article in news:
            print(f'''
            Title: {article["title"]}
            Source: {article["source"]}
            Author: {article["author"]}
            Description: {article["description"]}
            URL: {article["url"]}
            ''')
    return national_json_obj

def main(cfg, NewsApiInterface, WeatherApiInterface):
    local = make_local_query(cfg, NewsApiInterface, WeatherApiInterface)
    national = make_national_query(cfg, NewsApiInterface)

    if cfg.EXPORT_TO_JSON:
        import json
        data = dict()
        data["local"] = local
        data["national"] = national
        with open("all_news.txt", "w") as outfile:
            json.dump(data, outfile)

if __name__ == "__main__":
    main(cfg, NewsApiInterface, WeatherApiInterface)

