import requests
import re

def get_city_coordinates(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    response = requests.get(url)
    data = response.json()

    if "results" in data and len(data["results"]) > 0:
        city_data = data["results"][0]
        return {"name": city_data["name"], "lat": city_data["latitude"], "lon": city_data["longitude"]}
    else:
        return None

def get_weather(city):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true&timezone=Europe/Berlin"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "current_weather" in data:
            weather = data["current_weather"]
            temp = weather["temperature"]
            wind = weather["windspeed"]
            
            return f"Das aktuelle Wetter in {city['name']}: {temp}°C, Windgeschwindigkeit {wind} km/h."
        else:
            return "Ich konnte das Wetter nicht abrufen."
    
    except Exception as e:
        return f"Fehler beim Abrufen des Wetters: {e}"

def extract_city_from_text(text):
    """ Sucht nach einer Stadt in der Frage des Nutzers """
    match = re.search(r"wetter in ([\w\s]+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None