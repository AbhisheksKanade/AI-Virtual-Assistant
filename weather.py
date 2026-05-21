import requests

def get_weather(city="pune"):
    try:
        url = f"https://wttr.in/{city}?format=%t+%C"
        response = requests.get(url)

        if response.status_code == 200:
            return f"Weather in {city}: {response.text}"
        else:
            return "Weather not found"

    except:
        return "Error getting weather"