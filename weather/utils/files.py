import os

def Files():
    
    directory = os.path.expanduser('~/config_Conky/Scripts/weather')
    region = open(f'{directory}/utils/others/region').read()
    
    if 'weather.png' in f'{directory}/image/current':
        os.remove(f'{directory}/image/current/weather.png')

    return directory, region