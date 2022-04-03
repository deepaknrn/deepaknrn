import requests
from datetime import datetime

#Sydney latitude and longitude
parameters ={
"lat":33.8688,
"lng":1.2093,
"formatted":0
}

#ISS latitude and longitude
response=requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data=response.json()
Iss_lat=data["iss_position"]["latitude"]
Iss_lng=data["iss_position"]["longitude"]

print(Iss_lat,Iss_lng)

#Get the duration of the day
response1=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response1.raise_for_status()
sunrise=response1.json()["results"]["sunrise"]
sunset=response1.json()["results"]["sunset"]

print(sunrise,sunset)

sunrise_split=sunrise.split("T")
sunrise_hour_split=sunrise_split[1].split(":")
sunrise_hour=sunrise_hour_split[0]

sunset_split=sunset.split("T")
sunset_hour_split=sunset_split[1].split(":")
sunset_hour=sunset_hour_split[0]

print(sunrise_hour,sunset_hour)

time_now=datetime.now()
time_now_str=str(time_now)
time_hour=int(time_now_str[12:13])


#Compare the Sydney latitude and longitude Vs ISS Latitude and Longitude

if float(Iss_lat) >= round(parameters["lat"]-10,0) and  float(Iss_lat) <= round(parameters["lat"]+10,0):
  if float(Iss_lng) >= round(parameters["lng"]-10,0) and float(Iss_lng) <= round(parameters["lng"]+10,0):
    #if it is dark
    if time_hour <= sunrise_hour and time_hour>=sunset_hour:
      print("ISS at Sydney and Look at Sky")
