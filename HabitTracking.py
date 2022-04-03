import requests
from datetime import datetime

pixela_endpoint="https://pixe.la/v1/users"
username="deepak123"

user_params = {
  "token":"xderf1234tfsaq1234d",
  "username":username,
  "agreeTermsOfService":"Yes",
  "notMinor":"Yes",
  "thanksCode":"ThisIsThanksCode"
  }

#1.Setting up a user account in pixela 
#Post Method 
response=requests.post(url=pixela_endpoint,json=user_params)
#response.raise_for_status()
#print(response.text)

#2.Create a new pixelation graph definition.
#Post Method

pixela_graph_endpoint=f"https://pixe.la/v1/{username}/a-know/graphs"

graph_config={
  "id":"graph1",
  "name":"Cycle Graph",
  "unit":"Km",
  "type":"float",
  "color":"ajisai"
}

header ={
"X-USER-TOKEN":"xderf1234tfsaq1234d"
}

pixela_graph_response=requests.post(url=pixela_graph_endpoint,json=graph_config,headers=header)
#pixela_graph_response.raise_for_status()
#print(pixela_graph_response.text)

#3.Viewing a pixel created
#This is done by checking in the browser
#go to https://pixe.la/v1/users/deepak123/graphs/graph1.html

#Get the current day using datetime module
dt=datetime.now()
date_str=str(str(dt))[0:4]+str(str(dt))[5:7]+str(str(dt))[8:10]
#print(date_str)

#4.Post value to the graph
#Post Method

post_value_pixela_endpoint=f"https://pixe.la/v1/users/{username}/graphs/graph1"

post_value_params={
 "date":date_str,
 "quantity":"5" 
}

post_value_response=requests.post(url=post_value_pixela_endpoint,json=post_value_params,headers=header)
#post_value_response.raise_for_status()
#print(post_value_response.text)

#5.Update the Pixel for the graph
#Put Method

put_pixel_endpoint=f"https://pixe.la/v1/users/{username}/graphs/graph1/{date_str}"

put_value_params={
 "quantity":8
}

put_pixel_response=requests.put(url=put_pixel_endpoint,json=put_value_params,headers=header)
#put_pixel_response.raise_for_status()
#print(put_pixel_response.text)

#Delete a Pixel for the graph
#Refer Delete Method here : https://docs.pixe.la/entry/delete-pixel

