import requests
from datetime import datetime,timedelta
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "JYSLQ05DF3PQ5M11"
NEWS_API_KEY = "pub_379371b386c658d2699f1e136ea60bab47ac"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsdata.io/api/1/news"

tsla_params={
"function":"TIME_SERIES_DAILY",
"symbol":STOCK_NAME,
"outputsize":"compact",
"apikey":STOCK_API_KEY
}

news_params={
"apikey":NEWS_API_KEY,
"q":STOCK_NAME
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

TSLA_response=requests.get(url="https://www.alphavantage.co/query",params=tsla_params)
TSLA_response.raise_for_status()
#print("API Return Status Code:" + str (TSLA_response.status_code))
TSLA_json=TSLA_response.json()
#print(TSLA_json)

Yesterday_date = datetime.today() - timedelta(days=1)
Yesterday_date_str=(str(Yesterday_date))[0:10]
Day_Before_Yesterday_date = datetime.today() - timedelta(days=2)
Day_Before_Yesterday_date_str=(str(Day_Before_Yesterday_date))[0:10]

stock_price_yesterday=TSLA_json["Time Series (Daily)"][Yesterday_date_str]['4. close']
stock_price_day_before=TSLA_json["Time Series (Daily)"][Day_Before_Yesterday_date_str]['4. close']

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

##print(stock_price_yesterday)

#TODO 2. - Get the day before yesterday's closing stock price

##print(stock_price_day_before)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

positive_difference=round(abs(float(stock_price_yesterday)-float(stock_price_day_before)),2)


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference=round((positive_difference/round(float(stock_price_yesterday),2))*100,2)
##print(percentage_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

def get_news():
  NEWS_list=[]
  #print("Get News")
  NEWS_response=requests.get(url="https://newsdata.io/api/1/news",params=news_params)
  NEWS_response.raise_for_status()
  #print("API Return Status Code:" + str (NEWS_response.status_code))
  NEWS_json=NEWS_response.json()
  NEWS_list.append(NEWS_json["results"])
  i=0

  for item in NEWS_list:
    #get the top 1 news in a separate list
    if i==0:
      NEWS_list_1=item[i]
      i=i+1
  
  NEWS_Headline=NEWS_list_1["title"]
  NEWS_Brief=NEWS_list_1["full_description"]
  NEWS=NEWS_Headline+"||"+NEWS_Brief
  return(NEWS) 

if percentage_difference > 1.00:
  NEWS=get_news()

NEWS_LIST=NEWS.split("||")
NEWS_Headline=NEWS_LIST[0]
NEWS_Brief=NEWS_LIST[1]
#print(NEWS_Headline)
#print(NEWS_Brief)
if float(stock_price_yesterday)-float(stock_price_day_before)>0.00:
  symbol="🔺"
else:
  symbol="🔻"

Message=f"""
TSLA: {percentage_difference} {symbol}
Headline : {NEWS_Headline}
Brief: {NEWS_Brief}"""

Truncate_Message=Message[0:1300]
#print(len(Truncate_Message))


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=Truncate_Message,
                     from_='+16018085467',
                     to='+610449075793'
                 )

print(message.sid)
print(message.status)

print(Message)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
