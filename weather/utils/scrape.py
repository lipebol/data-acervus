import requests
from bs4 import BeautifulSoup

def scrapeWeather(region):

    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    }

    r = requests.get(
        "https://www.google.com/search", 
        headers = headers, 
        params = {
            "q": "tempo" + region
            }
    )
    soup = BeautifulSoup(r.text, "lxml")
    soup_weather = soup.find("div", {"class": "UQt4rd"})
    image = soup_weather.find("img")
    condition = image['alt']
    temperature = soup_weather.get_text()[:2] + "°C"
    rain = soup_weather.get_text().split("°F")[2].split("%")[0] + "%"
    air_humidity = soup_weather.get_text().split("°F")[2].split("%")[1] + "%"
    wind = soup_weather.get_text().split("°F")[2].split("%")[2].split("km/h")[0] + "km/h"

    weather = [condition, temperature, rain, air_humidity, wind]

    return weather