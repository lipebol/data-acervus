from utils.files import Files
from utils.scrape import scrapeWeather
from utils.verify import Verify
import json

def Weather():
    
    directory, region = Files()
    weather = scrapeWeather(region)

    item = {
        "condição": weather[0],
        "chuva": weather[2],
        "umidade": weather[3],
        "vento": weather[4]
    }

    item = json.dumps(item, ensure_ascii=False, indent=5)
    with open(f'{directory}/utils/others/weather.json', 'w') as file:
        file.write(item)

    Verify(directory, weather[0])

    print(weather[1])

