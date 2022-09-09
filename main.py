from urllib import response
import requests
import json
import config

'''
# How to get the API response

API_KEY = config.API_KEY

LAT = config.LAT
LON = config.LON

response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&appid={API_KEY}")

print(response.status_code)
print(response.content)

# Putting it into a file to explore without calling API repeatedly

with open('outputfile2.json', 'wb') as outf:
    outf.write(response.content)

'''

def parse(response):
    daily = response["daily"]
    week = [x["weather"][0]["main"] for x in daily][:7]
    
    for day, weather in enumerate(week):
        if weather == "Rain":
            # check response weather
            print(f"In {day+1} days -- Rain likely! Grab your brolly!")
        else:
            print(f"In {day+1} days -- Rain NOT likely!")
    return week

if __name__ == "__main__":
    # To test with a template response

    with open("outputfile2.json", "r") as f:
        data = json.load(f)

    # To get actual new data by calling the api

    # API_KEY = config.API_KEY
    # LAT = config.LAT
    # LON = config.LON

    # url = f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&appid={API_KEY}"

    # response = requests.get(url)
    # data = response.json()

    parse(data)