import requests
from datetime import datetime
import os

api_id = '#'
api_key = '#'		


api_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'


header = {
    'x-app-id':api_id,
    'x-app-key':api_key,
    'x-remote-user-id': '0'
}

usr_input = input("What you did today: ")


excercise_params = {
    'query': usr_input,
    "gender":"male",
    "weight_kg":'75',
    "height_cm":'176',
    "age":'21'
}

response1 = requests.post(url=api_endpoint,json=excercise_params,headers=header)
response1.raise_for_status()
results = response1.json()
results = results['exercises']


sheety_endpoint = 'https://api.sheety.co/a4b00f3bb955df1e12d3c478bbda6c81/myWorkouts/workouts'

header1 = {
   'Authorization': 'Bearer sheetymakessheetawesome101',
   "Content-Type":"application/json"
}

today = datetime.now()
date = today.strftime(f"{'%d'}/{'%m'}/{'%Y'}")
time = today.strftime(f"{'%X'}")
for i in range(len(results)):
    sheety_params ={
        'workout':{
            'date':date,
            'time':time,
            'exercise':results[i]["user_input"].title(),
            'duration':results[i]["duration_min"],
            'calories':results[i]["nf_calories"]
        }
    }

    response2 = requests.post(url=sheety_endpoint,json=sheety_params,headers=header1)
    response2.raise_for_status()
    print(response2.text)