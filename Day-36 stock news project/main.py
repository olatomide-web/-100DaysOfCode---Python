import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsdata.io/api/1/news"

STOCK_API_KEY = "MA7DNTG68J4YZ5VF"
NEWS_API_KEY = "pub_1718964480ce05e2acbf57136d6fb022a0a3a"

stock_params = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)
print(response.json())
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#positive difference
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#percentage difference
difference_percent = (difference / float(yesterday_closing_price)) * 100
print(difference_percent)

if difference_percent > 1:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    results = news_response.json()["results"]
    print(results)