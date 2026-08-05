import requests
import sys

API_KEY = "your_api_key_here"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(f"{city}: {data['weather'][0]['description']}, {data['main']['temp']}K")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)
    get_weather(sys.argv[1])
