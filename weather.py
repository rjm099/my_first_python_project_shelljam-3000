# Install the dependency from a terminal:
# pip install python-dotenv
import requests

LATITUDE = 40.7128
LONGITUDE = -74.0060

# We added &current=weather_code to get condition descriptions
URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current=temperature_2m,weather_code&temperature_unit=fahrenheit"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()
        
        temp = data["current"]["temperature_2m"]
        code = data["current"]["weather_code"]
        
        # Translate the numerical weather code into plain English
        condition = "Clear sky"
        if code in [1, 2, 3]:
            condition = "Partly cloudy"
        elif code in [45, 48]:
            condition = "Foggy"
        elif code in [51, 53, 55, 61, 63, 65]:
            condition = "Rainy"
        elif code in [71, 73, 75]:
            condition = "Snowy"
        elif code >= 95:
            condition = "Thunderstorm"

        print(f"COMPOWDER WEATHER: {temp}°F and {condition} in New York City.")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    get_weather()