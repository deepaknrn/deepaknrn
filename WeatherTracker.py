import requests

API_KEY="70905cb41a9ba2acd2fd1ce269bdb5df"
LOCATION="SYDNEY"
END_POINT="https://api.openweathermap.org/data/2.5/weather"

weather_params={
"lat":-33.868820,
"lon":151.209290,
"exclude":"current,minutely,hourly",
"appid":API_KEY  
}

response=requests.get(url=END_POINT,params=weather_params)
response.raise_for_status()
print("Response Code : " + str(response.status_code))
weather_data=response.json()
print(weather_data)
weather_id=weather_data["weather"][0]["id"]
print(weather_id)

if weather_id <=700:
  print("Bring an Umbrella")
else:
  print("It is not Raining currently")



