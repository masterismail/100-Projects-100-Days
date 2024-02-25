class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass

import requests
import json

response = requests.get(url="https://api.sheety.co/0171d80dbce85e9c31010c00153c2f78/flightDeals/prices")

json_data = response.json()


for i in range(2,len(json_data["prices"])):

 print(response.json()["prices"][i]["city"])
 print(response.json()["prices"][i]["iataCode"])
 print(response.json()["prices"][i]["lowestPrice"])


print(response.json()["prices"])
