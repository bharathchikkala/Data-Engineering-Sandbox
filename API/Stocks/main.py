'''
STOCK_PRIZE API DOCUMENTATION : https://www.alphavantage.co/documentation/
NEWS_API DOC : https://newsapi.org/
'''

import requests

from main import STOCK_NAME

STOCK_APIKEY = "A6ZIPGN7JKSSHYH7"
NEWS_APIKEY = "ea0b75d4889a4b89b0928fb14d73c403"
STOCK_NAME = "TCS.BSE"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "apikey": STOCK_APIKEY,
    "symbol": STOCK_NAME,
}

response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
# print(data)
data_list = [value for (key, value) in data.items()]
# print(data_list)
day_list = [key for (key, value) in data.items()]

yesterday_closing_price = data_list[0]["4. close"]
yesterday_day = day_list[0]
print(yesterday_day)
print(yesterday_closing_price)
day_before_yesterday_price = data_list[1]["4. close"]
day_before_yesterday = day_list[1]
print(day_before_yesterday)
print(day_before_yesterday_price)
# print(data["Time Series (Daily)"]["2026-05-14"]["4. close"])

difference = float(yesterday_closing_price) - float(day_before_yesterday_price)
# print(round(difference, 2))
up_down = None
if difference > 0:
    up_down = "📈"
    print("well,Got today a bit")
else:
    up_down = "📉"
    print("stocks are worst")

# if difference >= -20:
parameters = {
        "apiKey": NEWS_APIKEY,
        "q": "Tata Consultancy Services",
    }
news_response = requests.get(url="https://newsapi.org/v2/everything",params=parameters)
news_response.raise_for_status()
news = news_response.json()["articles"]
top_articles = news[0:3]
top_news_title = top_articles[0]["title"]
print("Some of the reasons for stock price up & down👇")
formatted_articles = [f"{STOCK_NAME}:{up_down}{round(difference, 2)}INR\nHeadline: {article['title']}\nBrief: {article['description']}" for article in top_articles]
for article in formatted_articles:
    print(article)
