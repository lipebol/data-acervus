#!/usr/bin/python3

import os
import json

def tempTwo():
    directory = os.path.expanduser('~/config_Conky/Scripts/weather')
    file = open(f'{directory}/weather.json')
    item = json.load(file)
    print(item["chuva"])
    print(item["umidade"])
    print(item["vento"])

tempTwo()