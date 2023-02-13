import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "0d3490fd12d2dd9d82be2909d40c7fad"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

# make a request
response = requests.get(URL)

# check if request worked
if response.status_code == 200:
   # load JSON data from the response
   recipe_data = response.json()
   # print the keys in the JSON object
   print("Keys in the JSON object:")
   for key in recipe_data.keys():
       print(key)
else:
   # if the request unsuccessful, print an error message
   print("error", response.status_code)

def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    main()