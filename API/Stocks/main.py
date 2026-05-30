'''
STOCK_PRIZE API DOCUMENTATION : https://www.alphavantage.co/documentation/
NEWS_API DOC : https://newsapi.org/
'''

import requests

from main import STOCK_NAME

STOCK_APIKEY = "A6ZIPGN7JKSSHYH7"
NEWS_APIKEY = "ea0b75d4889a4b89b0928fb14d73c403"
STOCK_NAME = "IRFC.BSE"

parameters = {
    "function": "TIME_SERIES_MONTHLY",
    "apikey": STOCK_APIKEY,
    "symbol": STOCK_NAME,
}

response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
response.raise_for_status()
data = response.json()
print(data)

# data_list = [value for (key, value) in data.items()]
# print(data_list)
# print(data_list[0])
# last_refreshed = data_list[0]['3. Last Refreshed']
# print(data_list[0]['3. Last Refreshed'])
# print(data_list[1])


# Get the last refreshed date
last_refreshed = data["Meta Data"]["3. Last Refreshed"]

# Get all dates sorted (latest first)
dates = sorted(data["Monthly Time Series"].keys(), reverse=True)

# Latest and previous dates
latest_date = dates[0]
previous_date = dates[1]

# Closing prices
latest_close = float(data["Monthly Time Series"][latest_date]["4. close"])
previous_close = float(data["Monthly Time Series"][previous_date]["4. close"])

# Percentage change
percent_change = ((latest_close - previous_close) / previous_close) * 100

print(f"Latest Date: {latest_date}, Close Price: {latest_close}")
print(f"Previous Date: {previous_date}, Close Price: {previous_close}")
print(f"Percentage Change: {percent_change:.2f}%")

# date_list = data_list[1]
# list = [date_list]
# print(list)
# print(date_list)
# dates_list = [key for (key, value) in date_list.items()]
# print(dates_list)
# this_month_closing_price = data_list[0]["4. close"]
# # yesterday_day = day_list[0]
# print(this_month_closing_price)
# # print(yesterday_closing_price)
# last_month_closing_price = data_list[1]["4. close"]
# # day_before_yesterday = day_list[1]
# print(last_month_closing_price)
# print(day_before_yesterday_price)
# print(data["Time Series (Daily)"]["2026-05-14"]["4. close"])

# difference = float(yesterday_closing_price) - float(day_before_yesterday_price)
# # print(round(difference, 2))

up_down = None
if percent_change > 0:
    up_down = "📈"
    print("well,Got a bit compared to previous month")
else:
    up_down = "📉"
    print("Ufff!,lost a bit compared to previous month")

# if difference >= -20:
parameters = {
        "apiKey": NEWS_APIKEY,
        "q": "Indian Railway Finance Corporation",
    }
news_response = requests.get(url="https://newsapi.org/v2/everything",params=parameters)
news_response.raise_for_status()
news = news_response.json()["articles"]
top_articles = news[0:3]
top_news_title = top_articles[0]["title"]
print("Some of the reasons for stock price up & down👇")
formatted_articles = [f"{STOCK_NAME}:{up_down}{round(percent_change, 2)}INR\nHeadline: {article['title']}\nBrief: {article['description']}" for article in top_articles]
for article in formatted_articles:
    print(article)
