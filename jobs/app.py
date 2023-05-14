#!/usr/bin/python3

import os
import requests
from bs4 import BeautifulSoup
import json


# def urlsScrape(url, directory):
#     headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
#     r = requests.get(
#         url, 
#         headers = headers,
#     )
#     soup = BeautifulSoup(r.text, "lxml")
#     a = soup.find_all("a", {"class": "sc-812f417a-1 fijAgW"})
#     n = 0
#     outRemote = f'{directory}/links/remote.txt'
#     outLocal = f'{directory}/links/local.txt'
#     while n < len(a):
#         link = a[n]['href'].split('?')[0]
#         if "remote" in url:
#             with open(outRemote, 'a') as file:
#                 file.write(link + "\n")
#         else:
#             with open(outLocal, 'a') as file:
#                 file.write(link + "\n")
#         n += 1

#     return a

def reportScrape(url):
    headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
    r = requests.get(
        url, 
        headers = headers,
    )
    soup = BeautifulSoup(r.text, "lxml")
    # 'class' do elemento <a>
    a = soup.find_all("a", {"class": "sc-70b75bd4-1 blwed"})
    report = []
    n = 0
    while n < len(a):
        i = a[n]['aria-label'].split("Ir para Vaga ")[1]
        if "|" in i:
            i = i.split(" | ")[1]
        report.append(i)
        n += 1

    return report

def App():
    directory = os.path.expanduser('~/config_Conky/Scripts/jobs')
    # files = os.listdir(f'{directory}/links')
    # if "remote.txt" in files:
        # os.remove(f'{directory}/links/remote.txt')
    # if "local.txt" in files:
        # os.remove(f'{directory}/links/local.txt')
    remote = open(f'{directory}/urls/url-remote.txt').read()
    local = open(f'{directory}/urls/url-local.txt').read()
    # a = urlsScrape(remote, directory)
    remote = reportScrape(remote)
    # a = urlsScrape(local, directory)
    local = reportScrape(local)
    items_remote = []
    items_local = []
    for i in remote:
        i = i.split(". ")[0]
        i = "#Remota: " + i + ";\n"
        items_remote.append(i)
    items = {
        "vagas": items_remote
    }
    items = json.dumps(items, ensure_ascii=False, indent=5)
    with open(f'{directory}/remote.json', 'w') as file:
        file.write(items)

    for i in local:
        i = i.split(". ")[0]
        i = "#Local: " + i +";\n"
        items_local.append(i)
    items = {
        "vagas": items_local
    }

    items = json.dumps(items, ensure_ascii=False, indent=5)
    with open(f'{directory}/local.json', 'w') as file:
        file.write(items)


App()