#!/usr/bin/python3

from ast import literal_eval
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from file import File
from inspect import currentframe
from os import getenv, path, remove
from scrape import Scrape
from system import System

class SpotifEx:
    
    load_dotenv(find_dotenv('.env'))
    def __init__(self) -> None:
        self.today = str(datetime.now().date())
        self._dir = path.dirname(__file__)
        self._metadata = System().dbus()
        self._File = File(self._dir)
        self._json = self._File.read(getenv('JSON_FILE'), 'json')
        self._trackid = self._File.read(getenv('TRACKID')) if self._File.exists(
            getenv('TRACKID')) else False


    def trackFind(self) -> None or dict:
        if self.today not in self._json['spotifEx'].keys():
            self._json['spotifEx'].update({self.today: []})
        else:
            for idx, item in enumerate(self._json['spotifEx'][self.today]):
                if self._metadata['trackid'] == item['track']['trackid']:
                    return item


    def nextTrack(self) -> None or str:
        if self._metadata:
            if self._metadata['trackid'] != self._trackid:
                return str(
                    self._File.write(
                        getenv('TRACKID'), 
                        self._metadata['trackid']
                    )
                )
        

    def run(self):
        if self.nextTrack():
            self.find = self.trackFind()
            if not self.find:
                self._metadata = Scrape(self._metadata).info()
                if self._metadata:
                    self._json['spotifEx'][self.today].append(self._metadata)
            else:
                self.find['listen'] += 1
            return self._File.write(getenv('JSON_FILE'), self._json, 'json')
        else:
            print("Neeem veeem")
        #else:
        #    if self._write(getenv('TRACKID'), getenv('VOID')):
        #        return self._new(
        #            getenv('VOID_IMAGE'), getenv('CURRENT_IMAGE')
        #        )
        #except Exception as error:
             #print(f"{error} in: @{currentframe().f_code.co_name}")
        #    return False

if __name__ == '__main__':
    app = SpotifEx()
    app.run()


#def Spotify():
    #directory = os.path.expanduser('spotify')
    #file_trackid = os.listdir("./utils/others/")
    #if 'trackid' not in file_trackid:
    #    with open('./utils/others/trackid', 'w') as file:
    #        file.write("")
    #bus = dbus.SessionBus()
    #file = open('./utils/others/trackid').read().strip()
    #try:
    #    spotify = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    #    iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
    #    props = iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
    #except dbus.exceptions.DBusException:
    #    if file != "":
    #        with open('./utils/others/trackid', 'w') as file:
    #            file.write("")
    #        source = './image/transparent.png'
    #        destination = './image/current/current.png'
    #        shutil.copyfile(source, destination)
    #    print("")
    #    print("")
    #else:
    #    strs = ("mpris:", "xesam:")
    #    toJSON = json.dumps(props).replace(strs[0], "").replace(strs[1], "")
    #    metadata = json.loads(toJSON)
    #    if file !=  metadata['trackid']:
    #        with open('./utils/others/trackid', 'w') as file:
    #            file.write(metadata['trackid'])
    #        imgurl = metadata['artUrl']
    #        scrapeImage(imgurl, directory)
    #    print(metadata['title'])
    #    print(metadata['artist'][0])
