import requests
from datetime import datetime
import os

APP_ID=os.environ['Nutritionix_APP_ID']
API_KEY=os.environ['Nutritionix_API_KEY']
API_URL="https://trackapi.nutritionix.com/v2/natural/exercise"

Header={"x-app-id":APP_ID,"x-app-key":API_KEY,"Content-Type":"application/json"}
Exercise=input("Tell me which exercies you did : ")

Params={
  "query":Exercise,
  "gender":"Male",
  "weight_kg":80,
  "height_cm":170,
  "age":33
  }

#Call the Nutritionix API endpoint

response_text={}
response=requests.post(API_URL,json=Params,headers=Header)
response.raise_for_status()
status_code=response.status_code
response_text=response.text
result_text=response.json()

print("API Reponse Code:" + str(status_code))
print("API Response Text: " +  str(response_text))

#Get today's date and time and format it using strftime 
dt=datetime.now()
datee=dt.strftime("%d/%m/%Y")
timee=dt.strftime("%X")

#Call the Sheety API endpoint 

Sheety_URL="https://api.sheety.co/926a64abed2af1bb25e75be56f3c0bef/workouts/workouts"

number_exercise=len(result_text["exercises"])
i=0

#Build json for the next API Call
#Call the API in a loop for the number of exercises done in a day


Bearer_Authentication=os.environ['Sheety_Bearer_Authentication']

bearer_header={
  "Authorization": Bearer_Authentication

}

for exercise in result_text["exercises"]:
   if i<=number_exercise:
     name=exercise["user_input"]
     duration_min=exercise["duration_min"]
     calories=exercise["nf_calories"]
     let_body={
       "workout":
        {"date": datee,
        "time":timee,
        "exercise":name,
        "duration":duration_min,
        "calories":calories
        }
      }
     
     sheety_response=requests.post(url=Sheety_URL,json=let_body,headers=bearer_header)
     print(sheety_response.text)
     i=i+1
     let_body={}
    







