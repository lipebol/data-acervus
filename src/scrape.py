from ast import literal_eval
from bs4 import BeautifulSoup
from inspect import currentframe
from os import getenv
from requests import get


class Scrape:

    def __init__(self, metadata: dict) -> None:
        self.headers = literal_eval(getenv('HEADERS'))
        self.__metadata = metadata
    

    def info(self) -> dict or bool:
        try:
            if self.__metadata:
                if self.__metadata['title'] != getenv('AD'):
                    self._artist = "".join(self.__metadata['artist'])
                    if getenv('SINGLE_QUOTE') in self._artist: ### Example: Joseph O'Brien
                        self.idx = self._artist.find(getenv('SINGLE_QUOTE'))
                        ### 'r' (raw string) for 'escape' (Joseph O\'Brien)
                        self._artist = "".join(
                            fr"{self._artist[:self.idx]}\{self._artist[self.idx:]}"
                        )
                    self.__soup = BeautifulSoup(
                        self._res_text(
                            get(
                                getenv('EVERY_NOISE') + 'lookup.cgi', 
                                headers = self.headers, 
                                params = literal_eval(getenv('PARAMS') % self._artist) 
                            )
                        ), 'lxml').find_all('a')

                    return {
                        "listen": 1, 
                        "track": self._mergeInfo(
                            [
                                {
                                    (
                                        i.text if str(i.text) != "â\x93\x98" else ""
                                    ) : getenv('EVERY_NOISE') + self.__soup[idx]['href']
                                } for idx, i in enumerate(self.__soup)
                            ]
                        )
                    }
            return False
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False


    def _mergeInfo(self, info: list) -> dict:
        for dictio in info:
            if "".join(dictio.keys()) == "":
                self.__metadata['artist'] = {
                    "name": self._artist.replace(getenv('BACKSLASH'), getenv('VOID')),
                    "profile": "".join(dictio.values())
                }
        self.__metadata['genres'] = info[:-1]
        self.__metadata.pop('albumArtist')
        return self.__metadata


    def image(self) -> bytes or bool:
        try:
            return self._res_content(get(url=self.__metadata['artUrl'], headers=self.headers))
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False


    def _res_content(self, request: object) -> bytes or bool:
        return request.content if self._status(request) else False


    def _res_text(self, request: object) -> str or bool:
        return request.text if self._status(request) else False
    

    def _status(self, request: object) -> bool:
        return True if request.status_code == 200 else False

    