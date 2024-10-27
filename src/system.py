from ast import literal_eval
from dbus import SessionBus, Interface
from inspect import currentframe
from json import dumps
from os import getenv


class System:

    def __init__(self):
        pass


    def dbus(self) -> dict or bool:
        try:
            return dict(
                (key.split(':')[1], value) for key, value in literal_eval(
                    dumps(
                        Interface(
                            SessionBus().get_object(
                                getenv('NAME'), getenv('OBJECT_PATH')
                            ), 
                            getenv('METHOD')
                        ).Get(
                            getenv('INTERFACE'), getenv('PROPERTIE')
                        )
                    )
                ).items()
            )
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False