import requests
from PIL import Image
import os


def scrapeImage(imgurl, directory):
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    r = requests.get(url=imgurl, headers=headers, stream=True)
    if r.status_code == 200:
        with open(f'{directory}/image/current/current.jpeg', 'wb') as image:
            image.write(r.content)
        image = Image.open(f'{directory}/image/current/current.jpeg')
        image.save(f'{directory}/image/current/current.png')
        os.remove(f'{directory}/image/current/current.jpeg')