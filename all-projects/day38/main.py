import requests
import os 
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

app_id = os.getenv("app_id")
app_key = os.getenv("app_key")
token = os.getenv("Authorization")
url_sheety = os.getenv("url_sheety")
url_nutri = os.getenv("url_nutri")

headers_nutri = {
    "x-app-id" : app_id,
    "x-app-key" : app_key,
    
    
}




def get_tags (query):
    json = {
    "query" : query
    }

    response_nutri = requests.post(
    url=url_nutri,
    headers= headers_nutri,
    json=json
    

    )
    result = response_nutri.json()
    return result

query = input("enter your query \n")
tags = get_tags(query=query)


exercise = str(tags['exercises'][0]['user_input'])
duration = str(tags['exercises'][0]['duration_min'])
calories = str(tags['exercises'][0]['nf_calories'])
date = str(dt.date.today())
time = str(dt.datetime.now())


sheeetinput = {
 "workout" : { 
      "date":     date,
      "time":     time,
      "exercise": exercise,
      "duration": duration,
      "calories": calories
}
}

headers_sheety = {'Authorization': token}


def update_sheet():
    
    response = requests.post(
        url = url_sheety,
        headers=headers_sheety,
        json= sheeetinput
    
        
        
    )
    
    print("sheet updated !")


update_sheet()











  