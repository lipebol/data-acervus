#!/usr/bin/python3

from utils.files import Files
import json

def weatherTwo():
    directory, off = Files()
    weather = json.load(open(f'{directory}/utils/others/weather.json'))
    print(weather["chuva"])
    print(weather["umidade"])
    print(weather["vento"])

weatherTwo()