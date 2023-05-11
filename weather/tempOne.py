#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import json
import shutil
import os
from datetime import datetime

def tempOne():
    currentHours = datetime.now()
    directory = os.path.expanduser('~/config_Conky/Scripts/weather')
    region = open(f'{directory}/region.txt').read()
    files = os.listdir(f'{directory}/current')
    destination = f'{directory}/current/weather.png'
    if 'weather.png' in files:
        os.remove(destination)
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
    if currentHours.hour == 6:
        if currentHours.minute >= 14 and currentHours.minute <= 40:
            if condition != "Tempestades isoladas com raios e trovões":
                if condition != "Chuvas com trovoadas":
                    condition = "Nascer do sol"
    if currentHours.hour == 17:
        if currentHours.minute >= 31:
            if condition != "Tempestades isoladas com raios e trovões":
                if condition != "Chuvas com trovoadas":
                    condition = "Pôr do sol"
    if currentHours.hour <= 5 or currentHours.hour >= 18:
        if condition != "Tempestades isoladas com raios e trovões":
            if condition != "Chuvas com trovoadas":
                condition = "Noite"
    source = f'{directory}/icons/{condition}.png'
    shutil.copyfile(source, destination)
    temperature = soup_weather.get_text()[:2] + "°C"
    rain = soup_weather.get_text().split("°F")[2].split("%")[0] + "%"
    air_humidity = soup_weather.get_text().split("°F")[2].split("%")[1] + "%"
    wind = soup_weather.get_text().split("°F")[2].split("%")[2].split("km/h")[0] + "km/h"
    item = {
        "condição": condition,
        "chuva": rain,
        "umidade": air_humidity,
        "vento": wind
    }

    item = json.dumps(item, ensure_ascii=False, indent=5)
    with open(f'{directory}/weather.json', 'w') as file:
        file.write(item)

    print(temperature)

tempOne()
