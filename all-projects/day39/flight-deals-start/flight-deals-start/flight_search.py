class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass

import requests

header = {
    "apikey": "YXkwejnJDgdoOsBPCy6VzeG8okPZwbST"
}

query = {
    "fly_from": "FRA",
    "fly_to": "PRG",
    "date_from": "20/02/2024",
    "date_to": "21/02/2024"
}

response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=header, params=query)

print(response.json()["data"][0]["price"])

response.json()["data"][0]["price"]
