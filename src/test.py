

""" from newsapi import NewsApiClient

client = NewsApiClient(api_key="fef7664a05d2466fad9808d03af93d11")

print(client.get_top_headlines(
    q="bitcoin",
    sources=None,
    category=None,
    language="en",
    country="us",
    page_size=10)) """

import requests

raw_response = requests.get("http://api.openweathermap.org/data/2.5/weather?&appid=227d84013f347b542827501bd6929b4d&zip=02460,us&units=imperial")
print("Connected to weather API")
response = raw_response.json()
print(response)