import datetime as td
import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

now = str(td.datetime.now())
today_date = now.split(" ")[0]
date = int(today_date[8:])
yesterday = str(date-1)
day_before_yesterday = str(date-2)
day_before_yesterday_date =  today_date.replace(today_date[8:],day_before_yesterday)
yesterday_date = today_date.replace(today_date[8:],yesterday)



params = {
    "symbol":STOCK,
    "apikey":"CPPVFLJ310MZMD34"
}

response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY", params=params)


# try : 
#  yesterday_stock = float(response.json()['Time Series (Daily)'][yesterday_date]['1. open'])
#  #day_before_yesterday_stock_open = float(response.json()['Time Series (Daily)'][day_before_yesterday_date]['1. open'])
#  yesterday_stock_open = float(response.json()['Time Series (Daily)'][yesterday_date]['1. open'])
#  yesterday_stock_close = float(response.json()['Time Series (Daily)'][yesterday_date]['4. close'])
# #  difference = yesterday_stock_close - day_before_yesterday_stock_open
#  print(f"stock difference : {(yesterday_stock_open)} ")
# except:
#  print("yesterday market was closed")
# try:
#  today_stock = response.json()['Time Series (Daily)'][today_date]
#  print(today_stock)
 
# except:
#  print("market closed today")

yesterday_stock = response.json()
 #day_before_yesterday_stock_open = float(response.json()['Time Series (Daily)'][day_before_yesterday_date]['1. open'])
# yesterday_stock_open = float(response.json()['Time Series (Daily)'][yesterday_date]['1. open'])
# yesterday_stock_close = float(response.json()['Time Series (Daily)'][yesterday_date]['4. close'])
#  difference = yesterday_stock_close - day_before_yesterday_stock_open
print(f"stock difference : {(yesterday_stock)} ")



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_params  = {
    "q":"tesla",
    "apikey":"605bf9d9bae04a52a95a96ae0508e47e",
    "from":yesterday_date,
    "to":today_date
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
top_3 = news_response.json()["articles"][:2]
#print(top_3[0]["title"])


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# account_sid = 'AC3d0d251daa480d5d088da4c08a7bac56'
# auth_token = '52ba17d39b4bc6e13cd69a01cdde7137'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+14243532012',
#   to='+917032229659',
#   body=f"{STOCK}:"
# )

# print(message.sid)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey=CPPVFLJ310MZMD34