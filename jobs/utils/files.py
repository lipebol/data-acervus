import os

def Files():

    directory = os.path.expanduser('~/config_Conky/Scripts/jobs')
    if "jobs.json" not in os.listdir(f'{directory}/utils/others/'):
        with open(f'{directory}/utils/others/jobs.json', 'w') as json_file:
            json_file.write(open(f'{directory}/utils/others/json').read())

    urls = []
    file = open(f'{directory}/utils/others/urls').readlines()
    for url in file:
        url = url.strip()
        urls.append(url)
    
    return urls, directory