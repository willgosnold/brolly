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
    hourly = response["hourly"]
    pop = [x["pop"] for x in hourly][:16]
    
    for i, j in enumerate(pop):
        if j >= 0.75:
            # check response weather
            if hourly[i]["weather"][0]["main"] == "Rain":
                print(f"In {i+1} hours -- Rain likely! Grab your brolly!")
            else:
                print(f"In {i+1} hours -- Looks like it MIGHT rain, but I'm not sure.")
        else:
            print(f"In {i+1} hours -- Rain NOT likely!")
    return pop

if __name__ == "__main__":
    with open("outputfile2.json", "r") as f:
        response = json.load(f)

    parse(response)