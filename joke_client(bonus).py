import requests
from typing import Dict

URL = "https://official-joke-api.appspot.com/random_joke"

def get_joke(joke_type: str) -> Dict:
    res = requests.get(URL, params={'type': joke_type})
    return res.json()

def main():
    joke_data = get_joke("random_joke")
    print("Joke details:")
    for key in joke_data.keys():
        print(f"{key}: {joke_data[key]}")

if __name__ == '__main__':
    main()
