import requests
import datetime as dt

now = str (dt.datetime.now())

split_now = now.split(' ')

response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()

data = response_iss.json()

latitude , longitude = data['iss_position']['latitude'] , data['iss_position']['longitude']

parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted":0

}



response = requests.get(url=f"https://api.sunrise-sunset.org/json?", params=parameters )
response.raise_for_status()

data = response.json()

sunset_split = data['results']['sunset'].split('T')

print(f"sunset time = {sunset_split[1]}\nTime Now = {split_now[1]}")



