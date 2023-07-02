from utils.scrape import scrapeImage
import dbus
import json
import shutil
import os


def Spotify():
    directory = os.path.expanduser('~/config_Conky/Scripts/spotify')
    file_trackid = os.listdir(f'{directory}/utils/others/')
    if 'trackid' not in file_trackid:
        with open(f'{directory}/utils/others/trackid', 'w') as file:
            file.write("")
    bus = dbus.SessionBus()
    file = open(f'{directory}/utils/others/trackid').read().strip()
    try:
        spotify = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
        iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
        props = iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
    except dbus.exceptions.DBusException:
        if file != "":
            with open(f'{directory}/utils/others/trackid', 'w') as file:
                file.write("")
            source = f'{directory}/image/transparent.png'
            destination = f'{directory}/image/current/current.png'
            shutil.copyfile(source, destination)
        print("")
        print("")
    else:
        strs = ("mpris:", "xesam:")
        toJSON = json.dumps(props).replace(strs[0], "").replace(strs[1], "")
        metadata = json.loads(toJSON)
        if file !=  metadata['trackid']:
            with open(f'{directory}/utils/others/trackid', 'w') as file:
                file.write(metadata['trackid'])
            imgurl = metadata['artUrl']
            scrapeImage(imgurl, directory)
        print(metadata['title'])
        print(metadata['artist'][0])