#!/usr/bin/python3

import dbus
import json
import requests
from PIL import Image
import os
import shutil


def ScrapeImage(imgurl, directory):
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    r = requests.get(url=imgurl, headers=headers, stream=True)
    if r.status_code == 200:
        with open(f'{directory}/image/current.jpeg', 'wb') as image:
            image.write(r.content)
        image = Image.open(f'{directory}/image/current.jpeg')
        image.save(f'{directory}/image/current.png')
        os.remove(f'{directory}/image/current.jpeg')

        
def App():
    directory = os.path.expanduser('~/config_Conky/Scripts/spotify')
    files = os.listdir(directory)
    if 'trackid' not in files:
        with open(f'{directory}/trackid', 'w') as file:
            file.write("")
    bus = dbus.SessionBus()
    file = open(f'{directory}/trackid').read().strip()
    try:
        spotify = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
        iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
        props = iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
    except dbus.exceptions.DBusException:
        if file != "":
            with open(f'{directory}/trackid', 'w') as file:
                file.write("")
            source = f'{directory}/transparent.png'
            destination = f'{directory}/image/current.png'
            shutil.copyfile(source, destination)
        print("")
        print("")
    else:
        strs = ("mpris:", "xesam:")
        toJSON = json.dumps(props).replace(strs[0], "").replace(strs[1], "")
        metadata = json.loads(toJSON)
        if file !=  metadata['trackid']:
            with open(f'{directory}/trackid', 'w') as file:
                file.write(metadata['trackid'])
            imgurl = metadata['artUrl']
            ScrapeImage(imgurl, directory)
        print(metadata['title'])
        print(metadata['artist'][0])

App()