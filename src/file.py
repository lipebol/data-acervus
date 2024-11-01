from inspect import currentframe
from json import dump, load
from os import getenv, path, remove
from PIL import Image
from shutil import copyfile
from system import System


class File:

    def __init__(self) -> None:
        self._dir = path.dirname(__file__)
        self._System = System()


    def read(self, file: str) -> object:
        try:
            if ".json" in getenv(file):
                return load(open(self._dir + getenv(file)))
            return open(self._dir + getenv(file)).read().strip()
        except Exception as error:
            self._System.notify(f"{error} in: @{currentframe().f_code.co_name}")
            return False
    

    def write(self, file: str, content: str or dict or bytes) -> str:
        try:
            self.type_write = 'wb' if type(content) == bytes else 'w'
            if ".json" in getenv(file):
                dump(content, open(self._dir + getenv(file), 'r+'), indent=5)
            else:
                open(self._dir + getenv(file), self.type_write).write(content)
            return getenv(file)
        except Exception as error:
            self._System.notify(f"{error} in: @{currentframe().f_code.co_name}")
            return False


    def exists(self, file: str) -> bool:
        try:
            if not path.isfile(self._dir + getenv(file)):
                self.write(file, 'VOID')
            return True
        except Exception as error:
            self._System.notify(f"{error} in: @{currentframe().f_code.co_name}")
            return False

    
    def new(self, source: str, destination: str) -> str:
        try:
            if ".jpeg" in source:
                Image.open(self._dir + source).save(self._dir + getenv(destination))
                remove(self._dir + getenv('ORIGINAL_IMAGE'))
                return getenv(destination)
            return copyfile(self._dir + source, self._dir + getenv(destination))
        except Exception as error:
            self._System.notify(f"{error} in: @{currentframe().f_code.co_name}")
            return False