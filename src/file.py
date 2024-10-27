
from inspect import currentframe
from json import dump, load
from os import getenv, path
from PIL import Image
from shutil import copyfile


class File:

    def __init__(self, dir: str) -> None:
        self._dir = dir

    def read(self, file: str, typefile=None) -> object:
        try:
            if typefile == "json":
                return load(open(self._dir + file))
            return open(self._dir + file).read().strip()
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False
    

    def write(self, file: str, content: str or dict or bytes, typefile=None) -> int:
        try:
            self.type_write = 'wb' if type(content) == bytes else 'w'
            if typefile == "json":
                return dump(content, open(self._dir + file, 'r+'), indent=5)
            return open(self._dir + file, self.type_write).write(content)
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False

    def exists(self, file: str) -> bool:
        try:
            if not path.isfile(self._dir + file):
                return self.write(file, getenv('VOID'))
            return True
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False

    
    def new(self, source: str, destination: str) -> str:
        try:
            if "jpeg" in source:
                Image.open(source).save(destination)
                return remove(getenv('ORIGINAL_IMAGE'))
            return copyfile(source, destination)
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False